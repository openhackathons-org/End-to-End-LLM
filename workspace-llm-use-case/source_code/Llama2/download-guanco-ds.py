# Copyright (c) 2024 NVIDIA Corporation.  All rights reserved. 

import gdown
import os

url_eva = 'https://drive.google.com/uc?id=1PFLTYBJi0rLQlFjWrr8ioaIgoNbiffXx&confirm=t'
url_train = 'https://drive.google.com/uc?id=1tAJI0z_dyZAX9MW6tYmv3znH_561BDVY&confirm=t'

output_eva = '../data/openassistant_best_replies_eval.jsonl'
output_train = '../data/openassistant_best_replies_train.jsonl'

gdown.download(url_eva, output_eva, quiet=False, proxy=None)
gdown.download(url_train, output_train, quiet=False, proxy=None)
