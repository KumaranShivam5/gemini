import numpy as np 
from tensorflow.keras.utils import to_categorical
def conf_mat(model , x , y ):
    '''
    parameters :
        model , x ,y 
    y not as one-hot-encoded
    returns confusion matrix
    '''
    
    oh_y_true = to_categorical(y)
    y_pred =  model.predict(x)
    oh_y_pred = np.zeros_like(y_pred)
    oh_y_pred[np.arange(len(y_pred)),y_pred.argmax(1)] = 1
    #print(oh_y_pred.shape)
    #print(oh_y_true.shape)
    mat =  np.matmul(oh_y_true.T , oh_y_pred)
    return mat


import seaborn as sns
from matplotlib import pyplot as plt
n_colors = 256 # Use 256 colors for the diverging color palette
palette = sns.diverging_palette(20, 220, n=n_colors) # Create the palette
color_min, color_max = [-1, 1] # Range of values that will be mapped to the palette, i.e. min and max possible correlation

def value_to_color(val):
    val_position = float((val - color_min)) / (color_max - color_min) # position of value in the input range, relative to the length of the input range
    ind = int(val_position * (n_colors - 1)) # target index in the color palette
    return palette[ind]

def heatmap(x,y,size):
    fig , ax = plt.subplots(figsize=(18,14))

    x_labels = [v for v in sorted(x.unique())]
    y_labels = [v for v in sorted(y.unique())]
    x_to_num = {p[1]:p[0]for p in enumerate(x_labels)}
    #display(x_to_num)
    y_to_num = {p[1]:p[0]for p in enumerate(y_labels)}

    color = [value_to_color(c) for c in size]
    size_scale = 200 
    ax.scatter(
        x = x.map(x_to_num),
        y = y.map(y_to_num),
        s = size * size_scale,
        marker = 's',
        
        c = color
    )

    ax.set_xticks([x_to_num[v] for v in x_labels])
    ax.set_xticklabels(x_labels, rotation=45 , horizontalalignment='right')

    ax.set_yticks([y_to_num[v] for v in y_labels])
    ax.set_yticklabels(y_labels)
    plt.savefig('plots/top_corr_30_lmxb.jpg')
    plt.show()

from tensorflow import keras 
from scipy.signal import correlate 
def nodes_imp(model , x_test_flat):
    y_pred =  model.predict(x_test_flat)
    activation = extractor.predict(x_test_flat)
    #print(activation.shape)
    imp = []
    for act in activation:
        v1 = y_pred.T[1]
    #print(cl.shape)
        c = np.asarray([[correlate(v1,v2 , mode='valid')[0] for v2 in act.T] for v1 in y_pred.T]) 
    #print(c.shape)
        imp.append(c)
    return imp