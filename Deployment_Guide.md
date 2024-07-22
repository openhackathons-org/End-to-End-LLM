# End-to-End LLM Bootcamp

The End-to-End LLM (Large Language Model) Bootcamp is designed from a real-world perspective that follows the data processing, development, and deployment pipeline paradigm. Attendees walk through the workflow of preprocessing the openassistant-guanaco dataset for the Text Generation task and training the dataset using the LLAMA 2 7Billion Model (a pre-trained and fine-tuned Large Language Model). Attendees will also learn to optimize an LLM using NVIDIA TensorRT™ LLM, an SDK for high-performance large language model inference, guardrail prompts and responses from the LLM model using NeMo Guardrails, and deploy the AI pipeline using NVIDIA TensorRT™ LLM Backend (powered by Triton™ Inference Server), open-source software that standardizes LLM deployment and execution across every workload. Furthermore, we introduced a challenge notebook to test your understanding of the material and solidify your experience in the Text Generation domain.

## Deploying the Labs

### Prerequisites

To run this tutorial, you will need a Laptop/Workstation/DGX machine with a minimum of 20GB NVIDIA GPU.

- Install the latest [Docker](https://docs.docker.com/engine/install/) and [Singularity](https://sylabs.io/docs/).
- The challenge lab requires a Huggingface security token. Steps can be found [in the link here]( https://huggingface.co/docs/hub/en/security-tokens).


### Tested environment

We tested and ran all labs on a DGX machine equipped with an Ampere A100 GPU and MIG instance 20GB. We also execute the same process using a workstation equipped with an NVIDIA® Quadro® GV100 GPU with 32GB of VRAM.


### Deploying with container

You can deploy this material using Singularity and Docker containers. Please refer to the respective sections for the instructions.


#### Running Singularity Container

###### Finetuning Llama2 With Custom Data (Lab 1 )

- Build the Lab 1 Singularity container with: `singularity build --fakeroot --sandbox nemo_llama2.simg Singularity_llama`

- Run the container for Lab 1 with: `singularity run --nv -B ~/End-to-End-LLM/workspace-llm-use-case:/workspace nemo_llama2.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`

 
 The `-B` flag mounts local directories in the container filesystem and ensures changes are stored locally in the project folder. Open jupyter lab in the browser: http://localhost:8888

You may start working on the labs by clicking the `LLM-Use-Case.ipynb` notebook.

When you finish these notebooks, shut down jupyter lab by selecting `File > Shut Down` in the top left corner, then shut down the Singularity container by typing `exit` or pressing `ctrl + d` in the terminal window.


#### Running Docker Container

##### TensorRT-LLM and Triton Deployment (Lab 2 & 3)


To run the Labs 2 & 3, build a Docker container by following these steps:  

- Open a terminal window and navigate to the directory where `Dockerfile_llama` file is located (e.g. `cd ~/End-to-End-LLM`)
- To build the docker container, run : `sudo docker build -f Dockerfile --network=host -t <imagename>:<tagnumber> .`, for instance: `sudo docker build -f Dockerfile_llama --network=host -t tensorrtllm:v08 .`
- To run the built container : `sudo docker run --gpus all -it --rm --shm-size=1g -p 8888:8888 -p 8000:8000 --ulimit memlock=-1 --ulimit stack=67108864 -v ~/End-to-End-LLM/workspace-llm-use-case:/workspace/app tensorrtllm:v08 jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace/app`


flags:
- `--rm` will delete the container when finished.
- `-it` means run in interactive mode.
- `--gpus` option makes GPUs accessible inside the container.
- `-v` is used to mount host directories in the container filesystem.
- `--network=host` will share the host’s network stack to the container.
- `-p` flag explicitly maps a single port or range of ports.
- `---shm-size` size of shared memory.

Open the browser at `http://localhost:8888` and click on the `LLM-Use-Case.ipynb`. Go to the table of content and clicke on Lab 2, `Building TensorRT Engine With Finetune Model`.
As soon as you are done with the rest of the labs, shut down jupyter lab by selecting `File > Shut Down` and the container by typing `exit` or pressing `ctrl d` in the terminal window.

Congratulations, you've successfully built and deployed an end-to-end LLM pipeline!



## Known issues







