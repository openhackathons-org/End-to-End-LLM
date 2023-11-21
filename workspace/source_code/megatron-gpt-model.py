# Copyright (c) 2023 NVIDIA Corporation.  All rights reserved. 

import gdown
import os


url_nemo = 'https://drive.google.com/uc?id=1mTQjczmQQTm-TL0lxxfzoq3EEFoKQ2l6&confirm=t'
output = '../../source_code/nemo_gpt1.3B_fp16.nemo'
gdown.download(url_nemo, output, quiet=False, proxy=None)

#gdown.cached_download(url, output, quiet=False,proxy=None,postprocess=gdown.extractall)
