import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd 

import json 

def load_tester(path):
    with open(path) as f:
        data = json.load(f)
    #print(data)
    return np.asarray(data)

data = np.asarray(load_tester('1624627989220O-result.json')).reshape(1,)
#clprint(data)
for d in data:
    print(d)
#print(data.shape)
ra_list = data[:,1]
dec_list = data[:,2]

plt.scatter(ra_list , dec_list)
plt.show()