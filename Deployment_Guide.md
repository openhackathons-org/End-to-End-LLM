# End-to-End NLP Bootcamp

The End-to-End Natural Language Processing (NLP) Bootcamp is designed from a real-world perspective that follows the data processing, development, and deployment pipeline paradigm. Attendees walk through the workflow of preprocessing raw text data and learn how to build a SQuAD (Stanford Question Answering Dataset) dataset format for Question Answering, train the dataset using NeMo Megatron-GPT (a transformer-based language model) and BERT (Bidirectional Encoder Representations from Transformers), an open source machine learning framework for NLP, and deploy the AI pipeline using a GPU-accelerated speech AI SDK.  


## Deploying the Labs

### Prerequisites

To run this tutorial you will need a Laptop/Workstation/DGX machine with NVIDIA GPU.

- Install the latest [Docker](https://docs.docker.com/engine/install/) or [Singularity](https://sylabs.io/docs/).
    - Once you have installed **docker**, follow the [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) to ensure that docker can be run without `sudo`.

- Get an NGC account and API key:

    - Go to the [NGC](https://ngc.nvidia.com/) website and click on `Register for NGC`.
    - Click on the `Continue` button where `NVIDIA Account (Use existing or create a new NVIDIA account)` is written.
    - Fill in the required information and register, then proceed to log in with your new account credentials.
    - In the top right corner, click on your username and select `Setup` in the dropdown menu.
    - Proceed and click on the `Get API Key` button.
    - Next, you will find a `Generate API Key` button in the upper right corner. After clicking on this button, a dialog box should appear and you have to click on the `Confirm` button.
    - Finally, copy the generated API key and username and save them somewhere on your local system.

### Tested environment

All Labs were tested and is set to run on a DGX machine equipped with an Ampere A100 GPU and MIG instance 32GB. It was also tested using a workstation equipped with an NVIDIA® Quadro® GV100 GPU with 32GB of VRAM. 


### Deploying with container

This material can be deployed with either Docker or Singularity container, refer to the respective sections for the instructions.

#### Running Docker Container

##### Lab 1, 2, and 3 

**Install dependencies**


1. Create a new `conda` environment using `miniconda`:

    - Install `Miniconda` by following the [official instructions](https://conda.io/projects/conda/en/latest/user-guide/install/).
    - Once you have installed `miniconda`, create a new environment by setting the Python version to 3.6:
    
        `conda create -n launcher python=3.8.10`
    
    - Activate the `conda` environment that you have just created:
    
        `conda activate launcher`
    
    - When you are done with your session, you may deactivate your `conda` environment using the `deactivate` command:
    
        `conda deactivate`
   

2. Install the TAO Launcher Python package called `nvidia-tao` into the conda launcher environment:
    
    `conda activate launcher`
    
    `pip3 install nvidia-tao`

3. Invoke the entrypoints using the this command `tao -h`. You should see the following output:
```
usage: tao 
         {list,stop,info,augment,bpnet,classification,detectnet_v2,dssd,emotionnet,faster_rcnn,fpenet,gazenet,gesturenet,
         heartratenet,intent_slot_classification,lprnet,mask_rcnn,punctuation_and_capitalization,question_answering,
         retinanet,speech_to_text,ssd,text_classification,converter,token_classification,unet,yolo_v3,yolo_v4,yolo_v4_tiny}
         ...

Launcher for TAO

optional arguments:
-h, --help            show this help message and exit

tasks:
      {list,stop,info,augment,bpnet,classification,detectnet_v2,dssd,emotionnet,faster_rcnn,fpenet,gazenet,gesturenet,heartratenet
      ,intent_slot_classification,lprnet,mask_rcnn,punctuation_and_capitalization,question_answering,retinanet,speech_to_text,
      ssd,text_classification,converter,token_classification,unet,yolo_v3,yolo_v4,yolo_v4_tiny}
```

   For more info, visit the [TAO Toolkit documentation](https://docs.nvidia.com/tao/tao-toolkit/text/tao_toolkit_quick_start_guide.html).

4. Install other dependencies needed to run the lab:
```

pip3 install jupyterlab
        
pip3 install ipywidgets
        
pip3 install soundfile
        
pip install Cython
        
pip install nemo_toolkit[all]
        
pip3 install pynini

```

**Run the Labs (1,2, and 3)**

Activate the conda launcher environment: `conda activate launcher`
    
You are to run all the `data preprocessing` notebooks, `question-answering-training.ipynb` and `qa-riva-deployment.ipynb` in the `launcher` environment.

Launch the jupyter lab with:

`jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=~/End-to-End-NLP/workspace` 

Remember to set the `--notebook-dir` to the location where the `project folder` where this material is located.

Then, open jupyter lab in the browser at http://localhost:8888 and start working on the lab by clicking on the `Start_here.ipynb` notebook.


##### Lab 4

To run the NeMo Megatron-GPT content, build a Docker container by following these steps:  

- Open a terminal window and navigate to the directory where `Dockerfile_nemo` file is located (e.g. `cd ~/End-to-End-NLP`)
- Run `sudo docker build -f Dockerfile_nemo --network=host -t <imagename>:<tagnumber> .`, for instance: `sudo docker build -f Dockerfile_nemo --network=host -t nemo_23_06:1.0 .`
- Next, execute the command: `sudo docker run --rm -it --gpus=all -v ~/End-to-End-NLP/workspace:/workspace --network=host -p 8888:8888 deepstream:1.0`

flags:
- `--rm` will delete the container when finished.
- `-it` means run in interactive mode.
- `--gpus` option makes GPUs accessible inside the container.
- `-v` is used to mount host directories in the container filesystem.
- `--network=host` will share the host’s network stack to the container.
- `-p` flag explicitly maps a single port or range of ports.

When you are inside the container, launch jupyter lab: 
`jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`. 

Open the browser at `http://localhost:8888` and click on the `Start_here.ipynb` notebook. Start working on the NeMo Megatron-GPT lab by clicking on `Nemo Fundamentals` notebook.
As soon as you are done with the lab, shut down jupyter lab by selecting `File > Shut Down` and the container by typing `exit` or pressing `ctrl d` in the terminal window.

Congratulations, you've successfully built and deployed an end-to-end NLP pipeline!


#### Running Singularity Container

###### Lab 1, 2, and 4

- Build the Data Preprocessing and TAO toolkit training Singularity container using: `singularity build --fakeroot --sandbox tao_convai.simg Singularity_convai`

- Build the Nemo Megatron-GPT Singularity container with: `singularity build --fakeroot --sandbox nemo_23_06.simg Singularity_nemo`


** Run the Labs (1,2, and 4)**


- Run the container for Lab 1 and 2 with: `singularity run --fakeroot --nv -B ~/End-to-End-Computer-NLP/workspace:/workspace tao_convai.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`

- Run the container for Lab 4 with: `singularity run --fakeroot --nv -B ~/End-to-End-Computer-NLP/workspace:/workspace nemo_23_06.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`


The `-B` flag mounts local directories in the container filesystem and ensures changes are stored locally in the project folder. Open jupyter lab in browser: http://localhost:8888

You may now start working on the lab by clicking on the `Start_Here.ipynb` notebook.

When you are done with these notebooks, shut down jupyter lab by selecting `File > Shut Down` in the top left corner, then shut down the Singularity container by typing `exit` or pressing `ctrl + d` in the terminal window.


###### Lab 3

Lab 3 (Riva Deploynemt) has no singularity container.



Congratulations, you've successfully built and deployed an end-to-end NLP pipeline!



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

