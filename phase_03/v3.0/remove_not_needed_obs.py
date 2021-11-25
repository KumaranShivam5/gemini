import numpy as np 
import pandas as pd 

import os

ctg = 'NS'

def hr():
    print('--------------------')
data= pd.read_csv(ctg+'_data_clean_source_list.csv')
ch_names = [di.replace(' ' ,'_')[:-1] for di in data['B_NAME']]
a_names = [di.replace(' ' ,'_')[:-1]+'.csv' for di in data['A_NAME']]
src_id = [si[:6] for si in data['SRC_ID']]
#print(src_id)

for c,s ,a in zip(ch_names , src_id , a_names):
    try:
        src = ctg+'_data_all/'+c+'.csv' 
        ## adding source_id in file names
        dest = ctg+'_data/'+ s+'-'+c+'#'+a 
        print('Copying' , c )
        os.system('cp '+src+' '+dest)
    except:
        hr()
        print('check source : ' , c )
        hr()

