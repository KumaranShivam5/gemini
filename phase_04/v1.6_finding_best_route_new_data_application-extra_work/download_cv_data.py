from posixpath import join
from astropy.io.fits import hdu
import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np 
from ciao_contrib.runtool import search_csc 

from astropy.io import fits 
from fields import fields 
from tqdm import tqdm

df = pd.read_csv('../source_list/all_cv_catalogue.csv')
df = df.replace(' ' , '_' , regex=True)


start = int(input('Start number : '))
end = int(input('End number : '))

df_select = df[df['Type'].isin(['CataclyV', 'Candidate_CV', 'known_CV', 'N', 'Candidate',
       'Candidate_Nova', 'Known_CV', 'DN', 'AntiNova',
       'Cataclysmic_Variable'])].iloc[start:end].reset_index(drop=True)

ra = df_select['R.A.']
dec = df_select['Dec.']
name = df_select['Name']
num_obs = [] 
offset = []
type = df_select['Type']
for index in tqdm(range(len(df_select))):
    try :
        s = search_csc(
                        radunit="arcsec", 
                        columns=fields, 
                        bands="broad",
                        clobber="yes" ,
                        radius= 15 , 
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
            data.to_csv('../data/all_data/CV_v2_all/'+name[index]+'.csv')
    except:
        print('Manual ispection needed :' , name[index])
        num_obs.append(-1)
    #data.to_csv('temp_v2.csv')
df_updated = df_select.copy()
df_updated.insert(5 , 'num_obs' , num_obs)

df_updated.to_csv('../source_list/cv_updated/'+str(start)+'-'+str(end)+'.csv')