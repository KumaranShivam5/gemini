from matplotlib import pyplot as plt 
import numpy as np 
from astropy.io import fits
#fits_image_filename = fits.util.get_testdata_filepath('result.fits.gz')
import matplotlib.cm as cm
import pandas as pd
xdta = pd.read_csv('xray.csv')
print(xdata)

hdu = fits.open('result_v7.fits.gz')
data = hdu[1].data
ra = np.asarray(data['ra'])
dec = np.asarray(data['dec'])
mag = data['phot_g_mean_mag']


ra_n = ra[(ra>4)]
dec_n = dec[ra>4]
ra = ra_n[ra_n<8]
dec = dec_n[ra_n<8]
#dec = dec[(ra>4) or (ra<8)]

ra = [r-360 if r>180 else r for r in ra]
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_aspect(2.5)
ax.scatter(ra,dec ,marker='+' , s=0.8)
plt.show()

plt.hist(mag)
plt.show()