# Copyright (c) 2021 NVIDIA Corporation.  All rights reserved. 

import gdown
import os

## alk.traj.dcd input file 
#url = 'https://drive.google.com/uc?id=1WZ0rtXZ-uMLfy7htT0gaU4EQ_Rq61QTF&export=download'

url1 = 'https://drive.google.com/uc?id=1l769asMKe7TYlahcurZkFgYiZc6JCr7E&confirm=t'
output1 = '../source_code/data/coqa-train-v1.0.json'
gdown.download(url1, output1, quiet=False, proxy=None)

url2 = 'https://drive.google.com/uc?id=1i_qockpjY8MM5wbabDRkcICLVwTEHO3n&confirm=t'
output2 = '../source_code/data/train-v2.0.json'
gdown.download(url2, output2, quiet=False, proxy=None)

url3 = 'https://drive.google.com/uc?id=11fNwTWL1kKrYJ-SgeTZ8q2C67p-JEcEZ&confirm=t'
output3 = '../source_code/data/v1.0-simplified_simplified-nq-train.jsonl.gz'
gdown.download(url3, output3, quiet=False, proxy=None)

url_qa = 'https://drive.google.com/uc?id=1Yq5xbjTddupmz-jFszdWqAo_l4xl7hyC&confirm=t'
output4 = '../results/questions_answering/export_riva/qa-model.riva'
gdown.download(url_qa, output4, quiet=False, proxy=None)

#gdown.cached_download(url, output, quiet=False,proxy=None,postprocess=gdown.extractall)
