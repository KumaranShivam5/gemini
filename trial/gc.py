from matplotlib import pyplot as plt 
import numpy as np 
from astropy.io import fits
#fits_image_filename = fits.util.get_testdata_filepath('result.fits.gz')
import matplotlib.cm as cm
import pandas as pd

hdu = fits.open('result_v7.fits.gz')
data = hdu[1].data
ra = np.asarray(data['ra'])
dec = np.asarray(data['dec'])
mag = data['phot_g_mean_mag']
par = data['parrallex']

ra_n = ra[(ra>4)]
dec_n = dec[ra>4]
ra = ra_n[ra_n<8]
dec = dec_n[ra_n<8]
#dec = dec[(ra>4) or (ra<8)]

ra = [r-360 if r>180 else r for r in ra]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect(2.5)
ax.scatter(ra,dec ,marker='+' , s=1)
plt.show()

from astropy.io.votable import parse_single_table
table = parse_single_table("coneSearch.xml")

xdata = table.array
x_ra = [x[1] for x in xdata]
x_dec = [x[2] for x in xdata]
#print(x_ra)

plt.rcParams.update({'font.size': 12})
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.set_aspect(3.0)
lab_opt = '{} Gaia sources '.format(len(ra))
lab_x = '{} Chandra sources '.format(len(x_ra))
ax.scatter(ra,dec ,marker='.' , s=8 , color='k' , label=lab_opt)
ax.scatter(x_ra,x_dec ,marker='.' , s=8 , color='red' , label=lab_x)
plt.legend()
plt.savefig('gaia_chandra_sources.png')
plt.show()

xm_data = np.loadtxt('cross_match_ra_dec.csv' , delimiter=',')
xm_ra = xm_data[:,0]
xm_dec = xm_data[:,1]

plt.rcParams.update({'font.size': 12})
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
ax.set_aspect(3.0)
lab_opt = '{} Gaia sources '.format(len(ra))
lab_x = '{} cross matched Chandra sources '.format(len(xm_ra))
ax.scatter(ra,dec ,marker='.' , s=8 , color='k' , label=lab_opt)
ax.scatter(xm_ra,xm_dec ,marker='.' , s=8 , color='red' , label=lab_x)
plt.legend()
plt.title('NGC 104 , cone search, 30.5arcsec radius ')
plt.savefig('gaia_chandra_xm.png')
plt.show()

import pandas as pd


dist_data = pd.read_csv('dist_info.csv')
r_est = dist_data['r_est'].to_numpy()/1000
r_low = dist_data['r_lo'].to_numpy()/1000
r_hi = dist_data['r_hi'].to_numpy()/1000
dec = dist_data['dec'].to_numpy()

plt.rcParams.update({'font.size': 14})
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
#ax.set_aspect(3.0)
##lab_opt = '{} Gaia sources '.format(len(ra))
#lab_x = '{} cross matched Chandra sources '.format(len(xm_ra))
ax.errorbar(r_est , dec , xerr=(r_est-r_low , r_hi-r_est) , marker='o', markersize=8,linestyle='none' , capsize=4 , color='k')
#plt.legend()
plt.title('Cross Matched sources , distance estimates / 47 Tuc ')
#plt.savefig('gaia_chandra_xm.png')
ax.set_xlabel('distance (kPc)')
ax.set_ylabel('dec (deg)')
plt.savefig('47_tuc_dist.png')
plt.show()

