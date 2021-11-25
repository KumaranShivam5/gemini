import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import seaborn as sns 

def plot_template(siz=(10,8)):

    fig, ax = plt.subplots(figsize=siz)
    sns.set_theme(style = 'ticks' , font_scale=1)
    plt.style.use('seaborn-dark-palette')
    c = plt.cm.jet(np.linspace(0,0.8,4))
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    return fig , ax 