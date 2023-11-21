# Copyright (c) 2023 NVIDIA Corporation.  All rights reserved. 

import gdown
import os


url_nemo = 'https://drive.google.com/uc?id=1-6Dk_v4_DhZmjDVkoDSXad76FUPlB3C3&confirm=t'
output = '../../source_code/nemo_gpt5B_fp16_tp1.nemo'
gdown.download(url_nemo, output, quiet=False, proxy=None)

#gdown.cached_download(url, output, quiet=False,proxy=None,postprocess=gdown.extractall)
