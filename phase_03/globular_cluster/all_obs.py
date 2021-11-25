import numpy as np 
from matplotlib import pyplot as plt 
import pandas as pd 
from os import system as sys 

use_f = ['var_mean' , 'var_sigma','cnts_aper', 'flux_aper','flux_aper_hilim' , 'flux_aper_lolim' , 'flux_significance']
filters = ['_h' ,'_m' ,'_s' ,'_u' ,'_b']


def hr():
    print('____________________________________________________')


def to_float(d):
    temp = []
    for di in d:
        try:
            temp.append(float(di))
        except Exception as e:
            print(e)
            print('NaN detected resetting value')
            temp.append(np.NAN)
    temp = np.asarray(temp)
    return temp 

def get_obs_val(file):
    data = pd.read_csv(file, delimiter='\t' , comment='#')
    data = data[data['match_type']=='u          ']
    data = data[data['instrument']=='ACIS']
    #------master info 

    hard_hm = np.asarray([float(f) for f in data['hard_hm']])
    hard_ms = np.asarray([float(f) for f in data['hard_ms']])
    hard_ratio =  []
    for h,m in zip(hard_hm , hard_ms):
        if(h/m<np.inf):
            hard_ratio.append(h/m)
        else:
            hard_ratio.append(np.NAN)

    data.sort_values(by=['gti_obs'] , inplace=True)
    rows = ['livetime' ,'gti_obs']
    for f in filters:
        for r in use_f:
            rows.append(r+f)
    #print(rows)
    data_all = data[rows]
    dates =data_all['gti_obs']
    data_all = data_all.drop(columns=['gti_obs'])
    #print(data_all)
    for j in data_all[:10]:
        data_all[j] = to_float(data_all[j])
    #print(data_all)
    data_mean = pd.DataFrame()
    i = 0
    for r in use_f:
        prop = []
        for f in filters:
            prop.append(r+f)
        temp = data_all[prop].mean(axis=1)
        data_mean.insert(i , r , temp)
        i+=1


    data_mean.insert(0 , 'hardness' , hard_ratio)
    data_mean.insert(0 , 'date' , dates)
    data_mean.insert(0 , 'exp_time' , data_all['livetime'])

    #print(data_mean)
    data_mean.dropna(axis=0 , how='any')
    flux = data_mean['flux_aper'].dropna(axis=0)
    hardness = data_mean['hardness'].dropna(axis=0)
    return flux, hardness

sys('ls cluster_obs_data > cl_files.txt')
cl_files = pd.read_csv('cl_files.txt' , names=['cl_name'])['cl_name']
flux = np.asarray([])
hardness = np.asarray([])
for c in cl_files:
    print(c)
    #plot_cl('cluster_obs_data/'+c)
    try:
        f , h =  get_obs_val('cluster_obs_data/'+c)
        #print(f.shape)
        flux = np.append(flux , f)
        hardness = np.append(hardness , h )
    except Exception as e:
        print(e)
        print('problem with ' , c)
print(flux.shape , hardness.shape)
