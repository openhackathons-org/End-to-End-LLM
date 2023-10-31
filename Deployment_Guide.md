# End-to-End LLM Bootcamp

The End-to-End LLM Bootcamp is designed from a real-world perspective that follows the data processing, development, and deployment pipeline paradigm. Attendees walk through the workflow of preprocessing the SQuAD (Stanford Question Answering Dataset) dataset for Question Answering task, train the dataset using BERT (Bidirectional Encoder Representations from Transformers), and execute prompt learning strategy using NeMo Megatron-GPT (a transformer-based language model). Attendees will also learn to optimize LLM (Large Language Model) using NVIDIA® TensorRT™ (an SDK for high-performance deep learning inference), guardrail prompts and responses from the LLM model using NeMo Guardrails, and deploy the AI pipeline using NVIDIA Triton™ Inference Server an open-source software that standardizes AI model deployment and execution across every workload.


## Deploying the Labs

### Prerequisites

To run this tutorial you will need a Laptop/Workstation/DGX machine with NVIDIA GPU.

- Install the latest [Docker](https://docs.docker.com/engine/install/) or [Singularity](https://sylabs.io/docs/).


### Tested environment

All Labs were tested and is set to run on a DGX machine equipped with an Ampere A100 GPU and MIG instance 32GB. It was also tested using a workstation equipped with an NVIDIA® Quadro® GV100 GPU with 32GB of VRAM. 


### Deploying with container

This material can be deployed with either Docker or Singularity container, refer to the respective sections for the instructions.

#### Running Docker Container

##### Lab 1, 2, and 3 


To run the NeMo Megatron-GPT content, build a Docker container by following these steps:  

- Open a terminal window and navigate to the directory where `Dockerfile_nemo` file is located (e.g. `cd ~/End-to-End-NLP`)
- Run `sudo docker build -f Dockerfile_nemo --network=host -t <imagename>:<tagnumber> .`, for instance: `sudo docker build -f Dockerfile_nemo --network=host -t nemo_23_06:1.0 .`
- Next, execute the command: `sudo docker run --rm -it --gpus=all -v ~/End-to-End-LLM/workspace:/workspace --network=host -p 8888:8888 deepstream:1.0`

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

Congratulations, you've successfully built and deployed an end-to-end LLM pipeline!


#### Running Singularity Container

###### Lab 1, 2, and 3

- Build the Nemo Megatron-GPT Singularity container with: `singularity build --fakeroot --sandbox nemo_23_06.simg Singularity_nemo`


**Run the Labs (1,2, and 3)**

- Run the container for Lab 1 with: `singularity run --fakeroot --nv -B ~/End-to-End-LLM/workspace:/workspace nemo_23_06.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`


The `-B` flag mounts local directories in the container filesystem and ensures changes are stored locally in the project folder. Open jupyter lab in browser: http://localhost:8888

You may now start working on the lab by clicking on the `Start_Here.ipynb` notebook.

When you are done with these notebooks, shut down jupyter lab by selecting `File > Shut Down` in the top left corner, then shut down the Singularity container by typing `exit` or pressing `ctrl + d` in the terminal window.


Congratulations, you've successfully built and deployed an end-to-end LLM pipeline!



## Known issues

Before running the `Prompt Tuning/P-Tuning` notebook, please shut down and close previous notebooks and the Jupyter notebook terminal (if opened) to avoid the error: errno: 98 - Address already in use.