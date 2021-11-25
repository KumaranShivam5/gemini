# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython


# %%
import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical


# %%
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 


# %%
data_bh = pd.read_csv('processed_data/BH.csv')
#print(data_bh)
print(data_bh.describe())
data_ns = pd.read_csv('processed_data/NS.csv')
#print(data_ns)
print(data_ns.describe())


data_pulsar = pd.read_csv('processed_data/PULSAR.csv')
print(data_pulsar.describe())
data_cv = pd.read_csv('processed_data/CV.csv')
data_cv.describe()
data = pd.concat([data_bh , data_ns ] , axis=0)
#print(data)
data =  data.sample(frac=1)
max_flux = 13
min_flux = 22
data = data[data['flux_aper']>max_flux]
data = data[data['flux_aper']<min_flux]
data = data[data['flux_aper_lolim']<min_flux]
data = data[data['flux_aper_hilim']>(max_flux-1)]
print(data.describe())
data_class = data[['class']]
data_val = data.drop(columns=['index' , 'livetime' , 'gti_obs' , 'significance' , 'likelihood' , 'class'])
#print(data_val)
import missingno as msno
msno.matrix(data_val)
plt.show()
'''
rows = []
for d in data_val:
    rows.append(d)
print(rows)


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
for r in rows:
    try:
        data_val[[r]] = imputer.fit_transform(data_val[[r]])
    except:
        print(r)
'''
data_val = data_val.replace(np.nan , 0)

for d in data_val:
    mean = np.mean(data_val[d])
    var = np.var(data_val[d])
    data_val[d] = (data_val[d]-mean)/var
    data_val[d] = data_val[d] / np.amax(data_val[d])
msno.matrix(data_val)
plt.show()


# %%
data[['flux_aper_hilim' , 'flux_aper_lolim' ,'flux_aper']].describe()


# %%
data_bh_clean = data[data_class['class']=='BH']
print(data_bh_clean.describe())
data_ns_clean = data[data_class['class']=='NS']
print(data_ns_clean.describe())


# %%
def split_data(x,y,frac):
    split_no = int(len(y)*frac )
    x_train = x[:split_no]
    x_test = x[split_no:]
    y_train = y[:split_no]
    y_test = y[split_no:]
    return (x_train , y_train) , (x_test , y_test)

x = data_val.to_numpy()
y = data_class.to_numpy()
(x_train , y_train) , (x_test , y_test) =  split_data(x, y, 0.8)
print(x_train.shape , y_train.shape)
print(x_test.shape , y_test.shape)

# %% [markdown]
# # Neural Network

# %%
def class_to_int(label , cl):
    temp = []
    for i in range(len(label)):
        #print(label[i])
        for j in range(len(cl)):
            if(label[i]==cl[j]):
                temp.append(j) 
    return temp
classes = ['BH' ,'NS' ]
y_train_int = class_to_int(y_train, classes)
y_test_int = class_to_int(y_test, classes)
one_hot_y_train =  to_categorical(y_train_int)
one_hot_y_test =  to_categorical(y_test_int)
#for y_i , y_j in zip(y_train , one_hot_y_train):
##    print(y_i , y_j)


# %%
np.random.seed(903378735)
def model_gen(shape , input_len):

    inputs =  keras.Input(shape=(input_len,))
    dense =  layers.Dense(48, activation='relu')
    x = dense(inputs)
    #x =  layers.BatchNormalization(axis=-1)(x)
    
    for s in shape:
        x = layers.Dense(s, activation='relu')(x)
    #x =  layers.BatchNormalization(axis=-1)(x)
    #x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(2 , activation='softmax')(x)
    model = keras.Model(inputs=inputs , outputs=outputs , name='trial_model')
    np.random.seed(903378735)
    model.compile(
        loss = "categorical_crossentropy",
        optimizer = keras.optimizers.Adam(learning_rate=0.005),
        metrics = ["accuracy"],
    )
    return model
model = model_gen([32,16,4] , x_train.shape[1])
history = model.fit(x_train, one_hot_y_train, batch_size=128, epochs=70, validation_split=0.2)


# %%
hist = history.history
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(hist['accuracy'] , label = 'accuracy' , color='k')
plt.plot(hist['val_accuracy'] , label = 'val_accuracy' , color='crimson')
plt.xlabel('No of epochs')
plt.legend()
plt.subplot(1,2,2)
plt.plot(hist['loss'] , label = 'loss' , color='k')
plt.plot(hist['val_loss'] , label='val_loss' , color='crimson')
plt.xlabel("No of Epochs")
plt.legend()
plt.savefig('plots/NS_BH.png')
plt.show()


# %%
y_pred_prob = model.predict(x_train)
#y_pred=  [np.argmax(yi) for yi in y_pred]
y_pred = []
for yi in y_pred_prob:
    temp = [0]*len(yi)
    temp[np.argmax(yi)] = 1
    y_pred.append(temp)
y_pred =  np.asarray(y_pred)
#print(y)


# %%
print(one_hot_y_test.shape)
print(y_pred.shape)
cf = np.matmul(one_hot_y_test.T , y_pred)
print(cf)


# %%
import seaborn as sns


# %%
y_pred_prob = model.predict(x_test)
#y_pred=  [np.argmax(yi) for yi in y_pred]
y_pred = []
for yi in y_pred_prob:
    temp = [0]*len(yi)
    temp[np.argmax(yi)] = 1
    y_pred.append(temp)
y_pred =  np.asarray(y_pred)
#print(y)
cf = np.matmul(one_hot_y_test.T , y_pred)

ax= plt.subplot()
sns.heatmap(cf, annot=True, fmt='g', ax=ax);  #annot=True to annotate cells, ftm='g' to disable scientific notation

# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix'); 
ax.xaxis.set_ticklabels(['BH', 'NS']); ax.yaxis.set_ticklabels(['BH', 'NS']);
plt.savefig('plots/cf_ns_bh_test.jpg')


# %%
get_ipython().run_line_magic('reload_ext', 'autoreload')


# %%
get_ipython().run_line_magic('autoreload', '2')
from my_utils.score import test_func , conf_matrix
from my_utils.print_lines import *


# %%
cf = conf_matrix(model , x_train , one_hot_y_train)

ax= plt.subplot()
sns.heatmap(cf, annot=True, fmt='g', ax=ax);  #annot=True to annotate cells, ftm='g' to disable scientific notation

# labels, title and ticks
ax.set_xlabel('Predicted labels');ax.set_ylabel('True labels'); 
ax.set_title('Confusion Matrix'); 
ax.xaxis.set_ticklabels(['BH', 'NS']); ax.yaxis.set_ticklabels(['BH', 'NS']);
#plt.savefig('plots/cf_ns_bh_test.jpg')


