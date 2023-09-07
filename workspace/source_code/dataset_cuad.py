# Copyright (c) 2023 NVIDIA Corporation.  All rights reserved. 

import gdown
import os

url1 = 'https://drive.google.com/uc?id=1C5T6Na63oATxn8rBmZ5YT55mjrs7WTEG&confirm=t'
output = '../../data/CUAD_v1.json'
gdown.download(url1, output, quiet=False, proxy=None)
