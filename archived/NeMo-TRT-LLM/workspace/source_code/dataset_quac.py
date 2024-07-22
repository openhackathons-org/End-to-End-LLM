# Copyright (c) 2023 NVIDIA Corporation.  All rights reserved. 

import gdown
import os

url1 = 'https://drive.google.com/uc?id=1dd6Nw9IwStqDAne1Hq_ZmIywvS98heYD&confirm=t'
output = '../../data/activity1/quac/quac_v0.2.json'
gdown.download(url1, output, quiet=False, proxy=None)