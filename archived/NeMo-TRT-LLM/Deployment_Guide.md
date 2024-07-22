# End-to-End LLM Bootcamp

The End-to-End LLM (Large Language Model) Bootcamp is designed from a real-world perspective that follows the data processing, development, and deployment pipeline paradigm. Attendees walk through the workflow of preprocessing the SQuAD (Stanford Question Answering Dataset) dataset for Question Answering task, training the dataset using BERT (Bidirectional Encoder Representations from Transformers), and executing prompt learning strategy using NVIDIA® NeMo™ and a transformer-based language model, NVIDIA Megatron. Attendees will also learn to optimize an LLM using NVIDIA TensorRT™, an SDK for high-performance deep learning inference, guardrail prompts and responses from the LLM model using NeMo Guardrails, and deploy the AI pipeline using NVIDIA Triton™ Inference Server, an open-source software that standardizes AI model deployment and execution across every workload.

## Deploying the Labs

### Prerequisites

To run this tutorial, you will need a Laptop/Workstation/DGX machine with a minimum of 20GB NVIDIA GPU.

- Install the latest [Docker](https://docs.docker.com/engine/install/) or [Singularity](https://sylabs.io/docs/).


### Tested environment

We tested and ran all labs on a DGX machine equipped with an Ampere A100 GPU and MIG instance 20GB. We also execute the same process using a workstation equipped with an NVIDIA® Quadro® GV100 GPU with 32GB of VRAM.


### Deploying with container

You can deploy this material using either Docker or Singularity containers. Please refer to the respective sections for the instructions.

#### Running Docker Container

##### Lab 1, 2, and 3 


To run the Megatron-GPT and NeMo Guardrails contents (Lab 1 & 3), build a Docker container by following these steps:  

- Open a terminal window and navigate to the directory where `Dockerfile_nemo` file is located (e.g. `cd ~/End-to-End-LLM`)
- Run `sudo docker build -f Dockerfile_nemo --network=host -t <imagename>:<tagnumber> .`, for instance: `sudo docker build -f Dockerfile_nemo --network=host -t nemo_23_06:1.0 .`
- Next, execute the command: `sudo docker run --rm -it --gpus=all -v ~/End-to-End-LLM/workspace:/workspace --network=host -p 8888:8888 nemo_23_06:1.0`

To run the TensorRT-LLM and Triton Deployment content (Lab 2), build a Docker container by following these steps: 

- Obtain the LLaMA-v2 7B checkpoints from [here](https://github.com/facebookresearch/llama) and setup your dataset in `End-to-End-LLM/workspace/source_code/llama-2-7b`
- Open a terminal window and navigate to the directory where `Dockerfile_trtllm` file is located (e.g. `cd ~/End-to-End-LLM`)
- To build the docker container, run : `sudo docker build -t openhackathons:llm-trt_llm -f Dockerfile_trtllm .`
- To run the built container : `sudo docker run --gpus all --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --rm -p 8888:8888 -p 8000:8000 -it openhackathons:llm-trt_llm`



flags:
- `--rm` will delete the container when finished.
- `-it` means run in interactive mode.
- `--gpus` option makes GPUs accessible inside the container.
- `-v` is used to mount host directories in the container filesystem.
- `--network=host` will share the host’s network stack to the container.
- `-p` flag explicitly maps a single port or range of ports.

When you are inside the container, launch jupyter lab: 
`jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`. 

Open the browser at `http://localhost:8888` and click on the `Start_here.ipynb` notebook.
As soon as you are done with the lab, shut down jupyter lab by selecting `File > Shut Down` and the container by typing `exit` or pressing `ctrl d` in the terminal window.

Congratulations, you've successfully built and deployed an end-to-end LLM pipeline!


#### Running Singularity Container

###### Lab 1, 2, and 3

- Build the Megatron-GPT and NeMo Guardrails (Lab 1 & 3) Singularity container with: `singularity build --fakeroot --sandbox nemo_23_06.simg Singularity_nemo`

- Build the TensorRT-LLM and Triton (Lab 2) Singularity container through the following steps:
    - Obtain the LLaMA-v2 7B checkpoints from [here](https://github.com/facebookresearch/llama) and setup your dataset in End-to-End-LLM/workspace/source_code/llama-2-7b 
    - Open a terminal window and navigate to the directory where `Singularity_trtllm` file is located (e.g. `cd ~/End-to-End-LLM`)
    - Build this TRT-LLM Singularity continaer with :  `singularity build --sandbox tensorrt_llm.sif Singularity_trtllm`


**Run The Labs (1,2, and 3)**

- Run the container for Lab 1 & 3 with: `singularity run --nv -B ~/End-to-End-LLM/workspace:/workspace nemo_23_06.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`

- Run the container for Lab 2 with: `singularity run --writable --nv --env HTTP_PORT=8000 tensorrt_llm.sif jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/code/tensorrt_llm`
 


The `-B` flag mounts local directories in the container filesystem and ensures changes are stored locally in the project folder. Open jupyter lab in the browser: http://localhost:8888

You may start working on the lab by clicking the `Start_Here.ipynb` notebook.

When you finish these notebooks, shut down jupyter lab by selecting `File > Shut Down` in the top left corner, then shut down the Singularity container by typing `exit` or pressing `ctrl + d` in the terminal window.


Congratulations, you've successfully built and deployed an end-to-end LLM pipeline!




## Known issues

#### Megatron-GPT Lab

i. When running the cell below in the `Lab Activity 2` notebook,

```python
!python /workspace/source_code/challenge_ptuning/megatron_gpt_prompt_learning_eval.py \
            virtual_prompt_model_file=" " \
            gpt_model_file=" " \
            inference.greedy=True \
            inference.add_BOS=False \
            trainer.devices=1 \
            trainer.num_nodes=1 \
            tensor_model_parallel_size=1 \
            pipeline_model_parallel_size=1 \
            pred_file_path="/workspace/results/activity2/predictions/cuad_predictions.txt"\
            data_paths=["/workspace/data/cuad/cuad_short_test.jsonl"]
````

you can experience the error `errno: 98 - Address already in use` as shown below

```python
...
[NeMo I 2023-11-03 18:35:44 save_restore_connector:249] Model MegatronGPTPromptLearningModel was successfully restored from /workspace/jupyter_notebook/nemo/nemo_experiments/p_tuning/2023-11-03_14-50-49/checkpoints/p_tuning.nemo.
Initializing distributed: GLOBAL_RANK: 0, MEMBER: 1/1
[W socket.cpp:426] [c10d] The server socket has failed to bind to [::]:53394 (errno: 98 - Address already in use).
[W socket.cpp:426] [c10d] The server socket has failed to bind to ?UNKNOWN? (errno: 98 - Address already in use).
[E socket.cpp:462] [c10d] The server socket has failed to listen on any local network address.
Error executing job with overrides: ['virtual_prompt_model_file=/workspace/jupyter_notebook/nemo/nemo_experiments/p_tuning/2023-11-03_14-50-49/checkpoints/p_tuning.nemo', 'gpt_model_file=/workspace/source_code/nemo_gpt1.3B_fp16.nemo', 'inference.greedy=True', 'inference.add_BOS=False', 'trainer.devices=1', 'trainer.num_nodes=1', 'tensor_model_parallel_size=1', 'pipeline_model_parallel_size=1', 'pred_file_path=/workspace/results/challenge_ptuning/predictions/cuad_predictions.txt', 'data_paths=[/workspace/data/cuad/cuad_short_test.jsonl]']
Traceback (most recent call last):
  File "/workspace/source_code/challenge_ptuning/megatron_gpt_prompt_learning_eval.py", line 121, in main
    model.trainer.strategy.setup_environment()
  File "/usr/local/lib/python3.10/dist-packages/pytorch_lightning/strategies/ddp.py", line 152, in setup_environment
    self.setup_distributed()
  File "/usr/local/lib/python3.10/dist-packages/nemo/collections/nlp/parts/nlp_overrides.py", line 100, in setup_distributed
    super().setup_distributed()
  File "/usr/local/lib/python3.10/dist-packages/pytorch_lightning/strategies/ddp.py", line 203, in setup_distributed
    _init_dist_connection(self.cluster_environment, self._process_group_backend, timeout=self._timeout)
  File "/usr/local/lib/python3.10/dist-packages/lightning_fabric/utilities/distributed.py", line 245, in _init_dist_connection
    torch.distributed.init_process_group(torch_distributed_backend, rank=global_rank, world_size=world_size, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/distributed_c10d.py", line 145, in wrapper
    return func(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/distributed_c10d.py", line 1025, in init_process_group
    store, rank, world_size = next(rendezvous_iterator)
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/rendezvous.py", line 245, in _env_rendezvous_handler
    store = _create_c10d_store(master_addr, master_port, rank, world_size, timeout)
  File "/usr/local/lib/python3.10/dist-packages/torch/distributed/rendezvous.py", line 176, in _create_c10d_store
    return TCPStore(
RuntimeError: The server socket has failed to listen on any local network address. The server socket has failed to bind to [::]:53394 (errno: 98 - Address already in use). The server socket has failed to bind to ?UNKNOWN? (errno: 98 - Address already in use).

Set the environment variable HYDRA_FULL_ERROR=1 for a complete stack trace.

```
  
The solution is to shut down the kernel of all previously opened notebooks and close them, including the Jupyter notebook terminal (if opened), to avoid the error below. You do not need to run the notebook from the start; please continue running from the same cell.    

ii. Sometimes, running the cell below in the `Prompt Tuning/P-Tuning` and `Lab Activity 2` notebooks can get frozen with no changes in the output seen for over 10mins:

` trainer.fit(model)`

To resolve the issue, please clear off all outputs displayed on the notebook, shut down the kernel, and restart it again. 







