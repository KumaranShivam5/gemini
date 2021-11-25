import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 

cv_data = pd.read_csv('cv_data.csv')
xrb_data = pd.read_csv('lmxrb_all_data.csv')
print(cv_data.shape)
print(xrb_data.shape)
#print(cv_data)


all_data =  pd.concat([cv_data , xrb_data] , ignore_index=True)
#print(all_data)
#print(all_data.shape)
#all_data['class']
all_data =  all_data.sample(frac=1).reset_index(drop=True)
all_data.index.name =  "index_compiled"
print('Normalizing data')
#print(all_data)

m, n =  all_data.shape
total = m*n
count = 0

for i in range(m):
    for j in range(n):
        count+=1
        per = ((count/total)*100)
        if(per%5==0):
            print('{:.0f}  done'.format(per))
        if isinstance(all_data.iloc[i,j],str):
            #print(i,j,all_data.iloc[i,j])
            try:
                all_data.iloc[i,j] =  float(all_data.iloc[i,j])
            except:
                #print('ivalid , setting to zero' , i, j, all_data.iloc[i,j])
                all_data.iloc[i,j]=0


np.amax(all_data)

for i in range(2,n):
    max_non_zero = np.amax(all_data.iloc[:,i])
    if(max_non_zero==0):
        continue
    else:
        all_data.iloc[:,i] = all_data.iloc[:,i] / np.amax(all_data.iloc[:,i]) 
    #print(i)

print(np.amax(all_data))

all_data.to_csv('all_data_compiled_v2.csv')