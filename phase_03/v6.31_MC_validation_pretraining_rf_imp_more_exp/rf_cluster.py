import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np 
import seaborn as sns
from IPython.display import display
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
df= pd.read_csv('result/rf_clustering.csv' , index_col=0)
display(df)

bh = df[df['class']=='BH']
ns = df[df['class']=='NS']

# axes instance
fig = plt.figure(figsize=(8,8))
ax = Axes3D(fig)
fig.add_axes(ax)

# get colormap from seaborn
cmap = ListedColormap(sns.color_palette("husl", 256).as_hex())

# plot
ax.scatter(
    bh['c1'] , bh['c2'] , bh['c3'] , 
    s=10,
    marker='o',  
    alpha=0.5 , 
    color='k'
    )
ax.scatter(
    ns['c1'] , ns['c2'] , ns['c3'] , 
    s=10,
    marker='o',  
    alpha=0.5 , 
    color='r'
    )

plt.show()