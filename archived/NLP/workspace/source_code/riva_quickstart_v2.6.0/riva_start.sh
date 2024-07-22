#!/bin/bash
# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

check_docker_version() {
    version_string=$(docker version --format '{{.Server.Version}}')
    if [ $? -ne 0 ]; then
        echo "Unable to run Docker. Please check that Docker is installed and functioning."
        exit 1
    fi
    maj_ver=$(echo $version_string | awk -F. '{print $1}')
    min_ver=$(echo $version_string | awk -F. '{print $2}')
    if [ "$maj_ver" -lt "19" ] || ([ "$maj_ver" -eq "19" ] && [ "$min_ver" -lt "03" ]); then
        echo "Docker version insufficient. Please use Docker 19.03 or later"
        exit 1;
    fi
}

block_until_server_alive() {
    # determine if TLS/SSL key & cert are provided
    grpc_tls_args=""
    if [ -n "$ssl_server_key" ] && [ -n "$ssl_server_cert" ]; then
        # DO not verify since self-signed/no CA
        grpc_tls_args+="-tls -tls-client-cert /ssl/server.crt -tls-client-key /ssl/server.key -tls-no-verify "
    fi
    for i in {1..30}
    do
    docker exec $1 /bin/grpc_health_probe -addr=:$riva_speech_api_port $grpc_tls_args 2> /dev/null
    rc=$?
    if [ $rc -ne 0 ]; then
      echo "Waiting for Riva server to load all models...retrying in 10 seconds"
      sleep 10
    else
      echo "Riva server is ready..."
      return
    fi
    done
    echo "Health ready check failed."
    echo "Check Riva logs with: docker logs $riva_daemon_speech"
    exit 1
}

# BEGIN SCRIPT
check_docker_version

# load config file
script_path="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
if [ -z "$1" ]; then
    config_path="${script_path}/config.sh"
else
    config_path=$(readlink -f $1)
fi

if [[ ! -f $config_path ]]; then
    echo 'Unable to load configuration file. Override path to file with -c argument.'
    exit 1
fi
source $config_path

# determine required LD_PRELOAD & model_repos based on desired services
ld_preload=""
if [ "$service_enabled_asr" = true ] || [ "$service_enabled_nlp" = true ] || [ "$service_enabled_tts" = true ]; then
    model_repos+=" --model-repo=/data/models/"
    # generate ld_preload based on what's deployed in /data/plugins...
    ld_preload+=$(docker run --init -it --rm -v $riva_model_loc:/data --entrypoint "/bin/bash" $image_speech_api -c "find /data/plugins/*.so -type f ! -size 0 2>/dev/null" | sed 's/\r//g' | paste -sd ':' -)
fi

ssl_vol_args=""
ssl_args=""
# determine if TLS/SSL key & cert are provided
if [ -n "$ssl_server_key" ] && [ -n "$ssl_server_cert" ]; then
  ssl_vol_args+="-v $ssl_server_cert:/ssl/server.crt -v $ssl_server_key:/ssl/server.key "
  ssl_args+="--use_ssl --ssl_server_cert /ssl/server.crt --ssl_server_key /ssl/server.key "
  if [ -n "$ssl_root_cert" ]; then
      ssl_vol_args+="-v $ssl_root_cert:/ssl/root_server.crt "
      ssl_args+=" --ssl_root_cert /ssl/root_server.crt "
  fi
fi

# speech server is required
# check if it's already running first...
if [ $(docker ps -q -f "name=^/$riva_daemon_speech$" | wc -l) -eq 0 ]; then
    echo "Starting Riva Speech Services. This may take several minutes depending on the number of models deployed."
    docker rm $riva_daemon_speech &> /dev/null
    if [[ $riva_target_gpu_family == "tegra" ]]; then
        docker_run_args="-p 8000:8000 -p 8001:8001 -p 8002:8002 -p 8888:8888 --device /dev/bus/usb --device /dev/snd $image_speech_api riva_server $ssl_args"
    else
        docker_run_args="-p 8000 -p 8001 -p 8002 $image_speech_api start-riva --riva-uri=0.0.0.0:$riva_speech_api_port --nlp_service=$service_enabled_nlp $ssl_args &> /dev/null"
        #docker_run_args="-p 8000 -p 8001 -p 8002 $image_speech_api start-riva --riva-uri=0.0.0.0:$riva_speech_api_port --asr_service=$service_enabled_asr --tts_service=$service_enabled_tts --nlp_service=$service_enabled_nlp $ssl_args &> /dev/null"
    fi
    docker run -d \
        --init \
        --gpus '"'$gpus_to_use'"' \
        -p $riva_speech_api_port:$riva_speech_api_port \
        -e "LD_PRELOAD=$ld_preload" \
        -e "RIVA_API_KEY=$RIVA_API_KEY" \
        -e "RIVA_API_NGC_ORG=$RIVA_API_NGC_ORG" \
        -e "RIVA_EULA=$RIVA_EULA" \
        -v $riva_model_loc:/data \
        $ssl_vol_args \
        --ulimit memlock=-1 --ulimit stack=67108864 \
        --name $riva_daemon_speech $docker_run_args

    if [[ $riva_target_gpu_family == "tegra" ]]; then
        docker exec $riva_daemon_speech /opt/tritonserver/bin/tritonserver --model-store /data/models --model-control-mode="poll" --log-info=true &
    fi
else
    echo "Riva Speech already running. Skipping..."
fi
block_until_server_alive $riva_daemon_speech

# Give terminal access for arm64/embedded to try clients, use -s (server only) to disable
if [[ $riva_target_gpu_family == "tegra" ]]; then
    if [[ "$2" != "-s" ]]; then
        echo "Use this container terminal to run applications:"
        docker exec -it $riva_daemon_speech /bin/bash
    fi
fi
