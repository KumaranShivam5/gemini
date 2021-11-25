import pandas as pd 
import numpy as  np 
import astropy.units as u
from astropy.coordinates import SkyCoord
import os 
#os.system('clear')


obj = pd.read_csv('source_list/NS_data_clean_source_list.csv')
obj_pos = obj[['B_RA' , 'B_DEC']]
obj_ra = obj['B_RA']
obj_dec = obj['B_DEC']

gc =  pd.read_csv('gc_cat.csv')

def find_sep(ra1,dec1 , ra2, dec2):
    c1 = SkyCoord(ra1, dec1, frame='icrs' , unit=(u.deg))
    c2 = SkyCoord(ra2, dec2, frame='icrs' , unit="deg")
    sep = c1.separation(c2)
    return (sep)

i = 0

for ra , dec in zip(obj_ra , obj_dec):
    #ra1 ,dec1 = gc['RA(2000)'][0] , gc['DEC'][0]
    #ra2 , dec2 = obj['B_RA'][0] , obj['B_DEC'][0] 
    #print(i)
    i+=1
    sep = [find_sep(ra , dec , ra_o, dec_o).arcmin for ra_o , dec_o in zip(gc['RA'],gc['DEC'])]    
    sep_min = np.amin(sep)
    print(sep_min)