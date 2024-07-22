# Copyright (c) 2023 NVIDIA Corporation.  All rights reserved. 

import gdown
import os

url1 = 'https://drive.google.com/uc?id=1kRyLpeg1ur8HC-wgsskR2dPmpmvL8qi6&confirm=t'
output = '../model/Llama-2-7b.tar'
gdown.download(url1, output, quiet=False, proxy=None)
