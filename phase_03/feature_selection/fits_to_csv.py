import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt 

from astropy.io import fits
#fits_image_filename = fits.util.get_testdata_filepath()
def fits_to_csv(in_file , out_file , rows_file, class_int):
    hdu = fits.open(in_file)
    #hdu = fits.open('../data/CVs/CV_heasarc_x_chandra.fits')
    data = hdu[1]
    d = pd.DataFrame(data.data)
    d.index.name = 'index'
    print(d.index.name)
    print('Loaded data table has shape')
    print(d.shape)  

    d_clean = d.dropna(how='any' , axis=0)
    d_clean = d.dropna(how='any' , axis=1)
    print(d.shape)

    #flags =  d_clean[['B_CONF_FLAG' ,'B_PILEUP_FLAG','B_SAT_SRC_FLAG' ]]

    import json 
    #f = open('rows_non_str.json')
    f = open(rows_file)
    rows = json.load(f)['rows']
    data =  d_clean[rows]
    print(data.shape)
    data.insert(int(0),'class',int(class_int)*np.ones(len(data)))
    data.to_csv(out_file)
    rows_matrix = []
    l = 0
    for i in rows:
        temp = [l,i]
        rows_matrix.append(temp)
        l+=1
    rows_matrix = np.asarray(rows_matrix )
    np.savetxt("rows/current_rows.csv", rows_matrix , fmt='%s')
    #data.insert(int(0),'class',np.zeros(len(data)))
    #data['class'] = int(1)
print('CSV data')
fits_to_csv('../data/CVs/CV_heasarc_x_chandra.fits', 'cv_data.csv', 'rows/rows_filter_level_1.json', 0)
#print('LMXRB data')
fits_to_csv('../data/binaries/LMXB_all.fits', 'lmxrb_all_data.csv', 'rows/rows_filter_level_1.json', 1)