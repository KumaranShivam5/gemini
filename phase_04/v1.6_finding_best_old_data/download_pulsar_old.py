from posixpath import join
from astropy.io.fits import hdu
import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np 
from ciao_contrib.runtool import search_csc 

from astropy.io import fits 
from fields import fields 
from tqdm import tqdm


df = pd.read_csv('../source_list/PULSAR_data_clean_source_list.csv' , delimiter=',' , comment='#' ,)
df = df.replace(' ' , '_' ,regex=True)
df.insert(0  , 'type' , ['PULSAR']*len(df))



start = int(input('Start number : '))
end = int(input('End number : '))

#start = 0 
#end = 3

df_select = df.iloc[start:end].reset_index(drop=True)

ra = df_select['B_RA']
dec = df_select['B_DEC']
name = df_select['A_NAME']
num_obs = [] 
offset = []
for index in tqdm(range(len(df_select))):
    try :
        s = search_csc(
                        radunit="arcsec", 
                        columns=fields, 
                        bands="broad",
                        clobber="yes" ,
                        radius= 3 , 
                        pos= str(ra[index])+','+str(dec[index])  ,
                        outfile='temp.csv')
                    #sys('search_csc outfile=trial.csv radunit=arcsec columns="SOS,SOP,SOV , o.gti_obs m.flux_aper_b" bands=broad clobber=yes radius=1 pos="65.428058,32.907468"')
                    #print(s)
                    
        data = pd.read_csv('temp.csv', delimiter='\t' , comment='#')
        data = data[data['match_type']=='u          ']
        data = data[data['instrument']=='ACIS']
        data.index.name= 'index'
        #f_name_fits = data_fits['A_NAME']
        n = len(data)
        num_obs.append(n)
        if(n>0):
            print('Match found --' , len(data))
            data.to_csv('../data/all_data/pulsar_old_all/'+name[index]+'.csv')
    except:
        print('Manual ispection needed :' , name[index])
        num_obs.append(-1)

df_updated = df_select.copy()
df_updated.insert(8 , 'num_obs' , num_obs)

df_updated.to_csv('../source_list/pulsar_old_updated/'+str(start)+'-'+str(end)+'.csv')