# End-to-End NLP Bootcamp

This repository contains the material for the **End-To-End NLP** bootcamp, the goal of which is to build a complete end-to-end NLP pipeline for Question Answering application. This bootcamp will introduce participants to multiple NVIDIA® SDKs, most notably NVIDIA NeMo Megatron, NVIDIA TensorRT™, and NVIDIA RIVA. Participants will also have hands-on experience in data preprocessing, model training, optimization, and deployment at scale.

The content is structured in 4 modules, plus an introductory notebook and two challenge notebooks:

- Overview of **End-To-End NLP** bootcamp
- Lab 1: Data preprocessing
- Lab 2: Custom model deployment on RIVA 
- Lab 3: NeMo Megatron
- Lab 4: NeMo Megatron-GPT 1.3B Prompt
- Challenge 1: building SQuAD dataset 
- Challenge 2: deploying custom model on RIVA


## Tutorial duration

The total bootcamp material would take approximately 8 hours. It is recommended to divide the teaching of the material into two days, covering Lab 1 & 2 in one session and Lab 3 & 4 in the next session.

## Running Labs

Lab 1, 3, and 4 are run using singularity while Lab 2 is run using Docker 

**To run the material using Singularity containers, follow the steps below.**

Build the Data Preprocessing Singularity container using: `singularity build --fakeroot --sandbox tao_convai.simg Singularity_convai`

Build the Nemo Megatron Singularity container with: `singularity build --fakeroot --sandbox nemo_23_02.simg.simg Singularity_nemo`


### Run Data Preprocessing Notebooks

Run the first container with: `singularity run --fakeroot --nv -B ~/End-to-End-Computer-NLP/workspace:/workspace tao_convai.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`

The `-B` flag mounts local directories in the container filesystem and ensures changes are stored locally in the project folder. Open jupyter lab in browser: http://localhost:8888

You may now start working on the lab by clicking on the `Start_Here.ipynb` notebook.

When you are done with `Overview.ipynb`, `General_preprocessing.ipynb`, `QandA_data_processing.ipynb`, and `Exercise.ipynb` notebooks, shut down jupyter lab by selecting `File > Shut Down` in the top left corner, then shut down the Singularity container by typing `exit` or pressing `ctrl + d` in the terminal window.

### Run Nemo Megatron and NeMo Megatron-GPT 1.3B Prompt

Run the container with: `singularity run --fakeroot --nv -B ~/End-to-End-Computer-NLP/workspace:/workspace nemo_23_02.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`

Open jupyter lab in browser: http://localhost:8888 and continue the lab by running

`NeMo_Primer.ipynb`, `Multitask_Prompt_and_PTuning.ipynb`, and `demo.ipynb` notebooks.

When you are done with these notebooks, shut down jupyter lab by selecting `File > Shut Down` in the top left corner, then shut down the Singularity container by typing `exit` or pressing `ctrl + d` in the terminal window.


## Running Riva Deployment using Docker

Run Lab 2 via a Docker container. Root privileges are required using `sudo`.

### Installing the prerequisites

1. Install `docker-ce` by following the [official instructions](https://docs.docker.com/engine/install/). Once you have installed docker-ce, follow the [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) or step 2 below to ensure that docker can be run without `sudo`.

2. Run docker without root  

    ```
    sudo groupadd docker
    
    sudo usermod  -aG docker $USER
    
    newgrp docker
    ```    

3. Install `nvidia-container-toolkit` by following the [install-guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

4. Get an NGC account and API key:
    - Go to the [NGC](https://ngc.nvidia.com/) website and click on `Register for NGC`.
    - Click on the `Continue` button where `NVIDIA Account (Use existing or create a new NVIDIA account)` is written.
    - Fill in the required information and register, then proceed to log in with your new account credentials.
    - In the top right corner, click on your username and select `Setup` in the dropdown menu.
    - Proceed and click on the `Get API Key` button.
    - Next, you will find a `Generate API Key` button in the upper right corner. After clicking on this button, a dialog box should appear and you have to click on the `Confirm` button.
    - Finally, copy the generated API key and username and save them somewhere on your local system.


5. Create a new `conda` environment using `miniconda`:

    - Install `Miniconda` by following the [official instructions](https://conda.io/projects/conda/en/latest/user-guide/install/).

    - Once you have installed `miniconda`, create a new environment by setting the Python version to 3.8.10:

        `conda create -n launcher python=3.8.10`

    - Activate the `conda` environment that you have just created:

        `conda activate launcher`

    - When you are done, you may deactivate and reactivate your conda environment using these commands:

        `conda deactivate`
        
        `conda activate launcher`

    - In the launcher environment, please install the following:
    
       ``` 
        pip3 install jupyterlab
        
        pip3 install ipywidgets
        
        pip3 install soundfile
        
        pip install Cython
        
        pip install nemo_toolkit[all]
        
        pip3 install pynini
      ```
        
### Run Riva Notebook       

To run the `qa-riva-deployment.ipynb`(Custom model deployment on RIVA ), run `conda activate launcher`

Launch the jupyter lab with:

`jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=~/End-to-End-NLP/workspace`

Remember to set the `--notebook-dir` to the location where the `project folder` for this material is located.

Then, open jupyter lab in the browser at http://localhost:8888 and start working on the lab.

When you are done with the `qa-riva-deployment.ipynb` and `challenge.ipynb` notebooks, shut down jupyter lab by selecting `File > Shut Down` in the top left corner


Congratulations, you've successfully built and deployed an end-to-end NLP Question Answering pipeline!



## Known issues

If the Riva server fails to start, run `docker logs riva-speech` to identify the errors within the logs

```bash
...
I1101 13:15:43.179256 103 tensorrt.cc:5454] TRITONBACKEND_ModelInstanceInitialize: riva-trt-riva_qa-nn-bert-base-uncased_0 (GPU device 0)
  > Riva waiting for Triton server to load all models...retrying in 1 second
  > Riva waiting for Triton server to load all models...retrying in 1 second
  > Riva waiting for Triton server to load all models...retrying in 1 second
  > Riva waiting for Triton server to load all models...retrying in 1 second
I1101 13:15:47.239278 103 logging.cc:49] [MemUsageChange] Init CUDA: CPU +253, GPU +0, now: CPU 287, GPU 1456 (MiB)
I1101 13:15:47.473845 103 logging.cc:49] Loaded engine size: 208 MiB

...

+------------------+------+
| Repository Agent | Path |
+------------------+------+
+------------------+------+

I1101 13:15:54.687420 103 server.cc:576] 
+--------------------+-------------------------------------------------------------------------------+--------+
| Backend            | Path                                                                          | Config |
+--------------------+-------------------------------------------------------------------------------+--------+
| onnxruntime        | /opt/tritonserver/backends/onnxruntime/libtriton_onnxruntime.so               | {}     |
| tensorrt           | /opt/tritonserver/backends/tensorrt/libtriton_tensorrt.so                     | {}     |
| riva_nlp_qa        | /opt/tritonserver/backends/riva_nlp_qa/libtriton_riva_nlp_qa.so               | {}     |
| riva_nlp_tokenizer | /opt/tritonserver/backends/riva_nlp_tokenizer/libtriton_riva_nlp_tokenizer.so | {}     |
+--------------------+-------------------------------------------------------------------------------+--------+

I1101 13:15:54.687497 103 server.cc:619] 
+---------------------------------------+---------+--------+
| Model                                 | Version | Status |
+---------------------------------------+---------+--------+
| qa_qa_postprocessor                   | 1       | READY  |
| qa_tokenizer-en-US                    | 1       | READY  |
| riva-trt-riva_qa-nn-bert-base-uncased | 1       | READY  |
| riva_qa                               | 1       | READY  |
+---------------------------------------+---------+--------+
...

I1101 13:15:54.841537 103 http_server.cc:180] Started Metrics Service at 0.0.0.0:8002
  > Triton server is ready...
ERROR: illegal value '' specified for bool flag 'asr_service'
ERROR: illegal value '' specified for bool flag 'tts_service'
One of the processes has exited unexpectedly. Stopping container.
Signal (15) received.
/opt/riva/bin/start-riva: line 1: kill: (197) - No such process
I1101 13:16:00.113213 103 server.cc:250] Waiting for in-flight requests to complete.
I1101 13:16:00.113252 103 server.cc:266] Timeout 30: Found 0 model versions that have in-flight inferences
I1101 13:16:00.113277 103 model_repository_manager.cc:1109] unloading: riva_qa:1
I1101 13:16:00.113419 103 model_repository_manager.cc:1109] unloading: riva-trt-riva_qa-nn-bert-base-uncased:1
I1101 13:16:00.113504 103 model_repository_manager.cc:1109] unloading: qa_tokenizer-en-US:1
I1101 13:16:00.113636 103 model_repository_manager.cc:1109] unloading: qa_qa_postprocessor:1
I1101 13:16:00.113837 103 model_repository_manager.cc:1214] successfully unloaded 'riva_qa' version 1

```

**Solution**

The solution is set to `asr_service` and `tts_service` to **false** within the `config.sh` file and ensure that line 93 in the `riva_start.sh` is change from:
```bash
docker_run_args="-p 8000 -p 8001 -p 8002 $image_speech_api start-riva --riva-uri=0.0.0.0:$riva_speech_api_port --asr_service=$service_enabled_asr --tts_service=$service_enabled_tts --nlp_service=$service_enabled_nlp $ssl_args &> /dev/null"

to:

docker_run_args="-p 8000 -p 8001 -p 8002 $image_speech_api start-riva --riva-uri=0.0.0.0:$riva_speech_api_port  --nlp_service=$service_enabled_nlp $ssl_args &> /dev/null"
```

