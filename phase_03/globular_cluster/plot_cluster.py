import numpy as np 
from matplotlib import pyplot as plt 
import pandas as pd 
from os import system as sys 
sys('ls cluster_obs_data > cl_files.txt')

cl_files = pd.read_csv('cl_files.txt' , names=['cl_name'])['cl_name']
print(cl_files)
def plot_cl(f_name):
    cl_data = pd.read_csv(f_name , comment='#' , delimiter='\t')
    print(cl_data)
    ra = cl_data['ra']
    dec = cl_data['dec']

    text =  '# '+ str(len(cl_data))
    
    plt.style.use('seaborn-dark-palette')
    
    f, ax = plt.subplots(1, 1, sharex=True , figsize=(8,6) ,constrained_layout=False)
    #plt.xticks(rotation=45)
    ax.text(0.0, 0.3, text, 
        bbox={'facecolor': 'black', 'alpha': 0.1, 'pad': 10})

    plt.hexbin(ra , dec , mincnt=1 , label=text)
    plt.text(np.min(ra) , np.min(dec) ,  text)
    plt.xlabel('RA (J2000)',size=13)
    plt.ylabel('DEC(J2000)',size=13)
    plt.title(f_name[19:-4])
    plt.colorbar()
    cl_name = f_name[19:-4]
    plt.savefig('cl_plots/'+cl_name+'.jpg')
    #plt.show()
    plt.close()
for c in cl_files:
    plot_cl('cluster_obs_data/'+c)