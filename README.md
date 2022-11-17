# End-to-End NLP Bootcamp

This repository contains the material for the **End-To-End NLP** bootcamp, the goal of which is to build a complete end-to-end NLP pipeline for Question Answering application. This bootcamp will introduce participants to multiple NVIDIA® SDKs, most notably NVIDIA TAO Toolkit, NVIDIA TensorRT™, and NVIDIA RIVA. Participants will also have hands-on experience in data preprocessing, model training, optimization, and deployment at scale.

The content is structured in 3 modules, plus an introductory notebook and two challenge notebooks:
- Overview of **End-To-End NLP** bootcamp
- Lab 1: Data preprocessing
- Lab 2: Transfer learning with NVIDIA TAO (QA training)
- Lab 3: Custom model deployment on RIVA 
- Challenge 1: building SQuAD dataset 
- Challenge 2: deploying custom dataset on RIVA


## Tutorial duration

The total bootcamp material would take approximately 8 hours. It is recommended to divide the teaching of the material into two days, covering Lab 1 in one session and Lab 2 & 3 in the next session.

## Running using Singularity

To run the material using Singularity containers, follow the steps below.

To build the TAO Toolkit Singularity container, run: `singularity build --fakeroot --sandbox tao_e2enlp.simg Singularity_tao`

To build the RIVA client Singularity container for the Client, run: 


To download the Riva Speech Server Singularity container for the Server run: `singularity pull riva-speech:2.6.0.sif docker://nvidia/nvcr.io/nvidia/riva/riva-speech:2.6.0`

### Run data preprocessing and TAO notebooks

Run the first container with: `singularity run --fakeroot --nv -B workspace:/workspace tao_e2enlp.simg jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=/workspace`

The `-B` flag mounts local directories in the container filesystem and ensures changes are stored locally in the project folder. Open jupyter lab in browser: http://localhost:8888 

You may now start working on the lab by clicking on the `Start_here.ipynb` notebook.

When you are done with `Data preprocessing Lab` and `2.Transfer learning with TAO Lab`, shut down jupyter lab by selecting `File > Shut Down` in the top left corner, then shut down the Singularity container by typing `exit` or pressing `ctrl + d` in the terminal window.

### Run Riva Speech Server

To activate the Riva Server container, run:
```
singularity run \
  --nv \
  
```
 

### Run Riva 



## Running using Docker

Run the material via a python virtual environment and Docker containers. Root privileges are required using `sudo`. If you don't have root privileges on your local system, please follow the above instructions on how to run the lab using Singularity.

### Installing the prerequisites

1. Install `docker-ce` by following the [official instructions](https://docs.docker.com/engine/install/). Once you have installed docker-ce, follow the [post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/) to ensure that docker can be run without `sudo`.

2. Install `nvidia-container-toolkit` by following the [install-guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

3. Get an NGC account and API key:
    - Go to the [NGC](https://ngc.nvidia.com/) website and click on `Register for NGC`.
    - Click on the `Continue` button where `NVIDIA Account (Use existing or create a new NVIDIA account)` is written.
    - Fill in the required information and register, then proceed to log in with your new account credentials.
    - In the top right corner, click on your username and select `Setup` in the dropdown menu.
    - Proceed and click on the `Get API Key` button.
    - Next, you will find a `Generate API Key` button in the upper right corner. After clicking on this button, a dialog box should appear and you have to click on the `Confirm` button.
    - Finally, copy the generated API key and username and save them somewhere on your local system.


4. Install NGC CLI
    - Log in with your account credentials at [NGC](https://ngc.nvidia.com/).
    - In the top right corner, click on your username and select `Setup` in the dropdown menu.
    - Proceed and click on the `Downloads` button in the CLI panel.
    - Select `AMD64 Linux` and follow the instructions.
    - Open the terminal on your local system and log in to the NGC docker registry (`nvcr.io`) using the command `docker login nvcr.io` and enter `$oauthtoken` as Username and your `API Key` as Password.  

### Install TAO Toolkit and dependencies

TAO Toolkit is a Python pip package that is hosted on the NVIDIA PyIndex. The package uses the docker restAPI under the hood to interact with the NGC Docker registry to pull and instantiate the underlying docker containers. You must have an NGC account and an API key associated with your account.

#### Virtualvenwrapper approach

1. Install `nvidia-container-toolkit > 1.3.0-1` from [here](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)

2. Run docker without root 

    - sudo groupadd docker
    - sudo usermod  -aG docker $USER
    - newgrp docker 

3. pip3 install python=3.6.9

4. Create virtualvenwrapper launcher
```
sudo apt update
sudo apt install python-pip python3-pip unzip
pip3 install --upgrade pip

pip3 install virtualenvwrapper

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=/home/user/.virtualenvs
export PATH=/home/user/.local/bin:$PATH
source /home/user/.local/bin/virtualenvwrapper.sh

mkvirtualenv -p /usr/bin/python3 launcher

workon launcher
```
Note that `user` should be replaced with the local machine user

5. TAO and Jupyter notebook installation
    
    `pip3 install jupyterlab`

    `pip3 install nvidia-tao`


6. Invoke the entrypoints using the this command `tao -h`. You should see the following output:
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

#### Install other dependencies to run the lab:
```
    pip3 install spacy-langdetect
    pip3 install -U spacy[cuda114]
    python3 -m spacy download en_core_web_sm 
    pip3 install pyspellchecker
    pip3 install openpyxl
    pip3 install -U transformers==3.0.0
    pip3 install nltk
    #python3 -m nltk.downloader punkt
    #pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
    #pip3 install Cython   
    pip3 install jupyterlab
    pip3 install ipywidgets
    pip3 install gdown
    pip3 install soundfile
    
    #nemo installation
    pip install Cython
    pip install nemo_toolkit[all]
    pip3 install pynini
```

### Run All Notebooks

Activate virtualvenwrapper launcher `workon launcher` (you may be required to export path as executed in 4. above)
    
You are to run the first ALL notebooks in the `launcher` environment.

Launch the jupyter lab with:

`jupyter-lab --no-browser --allow-root --ip=0.0.0.0 --port=8888 --NotebookApp.token="" --notebook-dir=~/End-to-End-NLP/workspace` 

Remember to set the `--notebook-dir` to the location where the `project folder` where this material is located.

Then, open jupyter lab in the browser at http://localhost:8888 and start working on the lab by clicking on the `Start_here.ipynb` notebook.


Congratulations, you've successfully built and deployed an end-to-end computer vision pipeline!

## Known issues

### TAO

a. When installing the TAO Toolkit Launcher to your host machine’s native python3 as opposed to the recommended route of using a virtual environment, you may get an error saying that `tao binary wasn’t found`. This is because the path to your `tao` binary installed by pip wasn’t added to the `PATH` environment variable in your local machine. In this case, please run the following command:

`export PATH=$PATH:~/.local/bin`

b. When training, you can see an error message stating:
```
Resource exhausted: OOM when allocating tensor...
ERROR: Ran out of GPU memory, please lower the batch size, use a smaller input resolution, use a smaller backbone, or enable model parallelism for supported TLT architectures (see TLT documentation).
```
As the error says, you ran out of GPU memory. Try playing with batch size to reduce the memory footprint.

### NGC

You can see an error message stating:

`ngc: command not found ...`

You can resolve this by setting the path to ngc within the conda launcher environment as:

`echo "export PATH=\"\$PATH:$(pwd)/ngc-cli\"" >> ~/.bash_profile && source ~/.bash_profile`

### Riva Speech Server

