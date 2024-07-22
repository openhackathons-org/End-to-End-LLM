# Copyright (c) 2023 NVIDIA Corporation.  All rights reserved. 

import gdown
import os

url1 = 'https://drive.google.com/uc?id=1rfMCxT8fUQwQ5Pe6z7kDgK3nAZ6FyEeT&confirm=t'
output = '../model/Llama-2-7b-chat.tar'
gdown.download(url1, output, quiet=False, proxy=None)
