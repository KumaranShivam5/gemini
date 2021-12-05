import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
from IPython.display import display
import seaborn as sns

def filter_data(data_sent , max_flux= -12):
    data = data_sent.copy()
    max_flux = -12
    min_flux = 26
    data = data[data['flux_aper']<max_flux]

    data = data[data['significance']>2]
    data_class = data[['class']]

    data_sig = data['significance']
    data_id = data['src_id']
    data_name = data['src_n']
    obs_info_params = [ 'livetime','likelihood','pileup_flag','mstr_sat_src_flag','mstr_streak_src_flag'   ,'gti_obs' , 'flux_significance_b'  , 'flux_significance_m' , 'flux_significance_s' , 'flux_significance_h' , 'flux_significance_u'    ]
    data_val = data.drop(columns=obs_info_params)
    return data_val

def norm_data(data_sent):
    data = data_sent.copy()
    #data.replace()
    for d in data:
        max_val = np.amax(data[d])
        min_val =  np.amin(data[d])
        data[d] = (data[d]-min_val)/(max_val-min_val)
    return data
def std_data(data_sent):
    data = data_sent.copy()
    for d in data:
        mean =  np.mean(data[d])
        std = np.sqrt(np.var(data[d]))
        data[d] = (data[d]-mean)/std 
    return data
def do_nothing(data_sent):
    return data_sent


def extract_data(data_sent , impute_fn = '',reduce_fn = ' ' , rf_impute=False):
    data = data_sent.copy()
    data = data.sample(frac=1)
    data = filter_data(data)
    #display(data)
    data_id = data[[ 'class' ,'src_n' , 'src_id' ,'significance' , ]]
    data_id = data_id
    data_val = data.drop([ 'class' ,'src_n' , 'src_id' ,'significance' ,] , axis=1)
    data_val = reduce_fn(data_val)
    return data_val , data_id
    #if(rf_impute):
    #    data_val  , random_forest_imputer = impute_fn(data_val , data_id)
    #else:
    #    data_val = impute_fn(data_val)
    data_val = reduce_fn(data_val)
    data_val = data_val.reset_index(drop=True)
    data_reduced = pd.concat([data_id , data_val] , axis=1)
    if(rf_impute):
        return(data_reduced , random_forest_imputer)
    else:
        return data_reduced


train = pd.read_csv('../processed_data/'+'BH'+'_.csv' , index_col='obs_id')
df_bh = train.sample(frac=1)


train = pd.read_csv('../processed_data/'+'NS'+'_.csv' , index_col='obs_id')
df_ns = train.sample(frac=1)

train = pd.read_csv('../processed_data/'+'CV'+'_.csv' , index_col='obs_id')
df_cv = train.sample(frac=1)

train = pd.read_csv('../processed_data/'+'PULSAR'+'_.csv' , index_col='obs_id')
df_plsr = train.sample(frac=1)

train = pd.read_csv('../processed_data/'+'TUC'+'_.csv' , index_col='obs_id')
df_tuc = train.sample(frac=1)
src = pd.read_csv('../source_list/TUC_data_clean_source_list.csv')
display(src.head())
tuc_class = ['CV           ','MSP          ', 'QLX          ']
src_list = src[src['A_SOURCE_TYPE'].isin(tuc_class)]['SRC_ID']
df_tuc = df_tuc[df_tuc['src_id'].isin(src_list)]

train = pd.concat([df_bh , df_ns , df_cv, df_plsr , df_tuc])
train

num_src = len(np.unique(train['src_id']))
print('Total Num of sources : ' , num_src)


obs_count = train['src_id'].value_counts().to_frame(name = 'num_obs')
obs_count[obs_count['num_obs']==1]


train['class'].value_counts()

import sklearn.neighbors._base
from os import sys
sys.modules['sklearn.neighbors.base'] = sklearn.neighbors._base


from missingpy import MissForest 

def rf_impute(d, i ):
    data = pd.concat([i , d] , axis=1)
    data = data.drop(columns=['src_n' , 'src_id' , 'significance' ,])
    rf_imputer = MissForest(verbose=0)
    #new_data = d.drop(columns= ['class'])
    new_data = rf_imputer.fit_transform(d)
    return new_data , rf_imputer



from features import features as feat 
all_feat = list(feat['info'])+list(feat['flux']['photon'])+list(feat['flux']['energy'])+list(feat['variability'])+list(feat['hardness'])+list(feat['model_fit']['powerlaw'])+list(feat['model_fit']['bb'])+list(feat['model_fit']['brems'])+list(feat['info_pre_filter'])


feat_to_drop = list(feat['model_fit']['powerlaw']) + list(feat['model_fit']['bb']) + list(feat['model_fit']['brems']) 
#feat_to_drop = []
feat_used = [item for item in all_feat if item not in feat_to_drop]

sp = [] 
for f in feat_used:
    #print(f)
    na = train[feat_used][f].isna().value_counts()
    try:
        sp.append([f , 1-na[0]/(na[0]+na[1])])
    except:
        sp.append([f , 0])
sp =  np.asarray(sp)
sparsity = pd.DataFrame(sp , columns=['feat' , 'sparsity']).sort_values(by='sparsity' , ascending=False).reset_index()


u_band = ['flux_aper_lolim_u' , 'flux_aper_hilim_u' , 'flux_aper_u', 'photflux_aper_u' ,'photflux_aper_lolim_u' , 'photflux_aper_hilim_u' ]

top_sparse = sparsity[:4]['feat']
top_sparse

train_set = train[feat_used]
train_set = train_set.drop(columns=u_band)
train_set 

from tqdm import tqdm 
cl = str(input('Enter class :'))
source_list = np.unique(train_set[train_set['class']==cl]['src_n'].to_list())
all_imp_data = pd.DataFrame()
all_imp_id = pd.DataFrame()
all_imp_data_norm = pd.DataFrame()
#s  = source_list[8]
for s in tqdm(source_list[:]):
    #s = 'PSR J1413-6205'
    #print(s)
    train_now = train_set[train_set['src_n']==s]
    data_val , data_id   = extract_data(train_now ,  impute_fn= rf_impute , reduce_fn= do_nothing , rf_impute=True )
    print('Source :' ,  s)
    print('Num of obs : ' , len(data_val))
    try:
        new_data , random_forest_imputer = rf_impute(data_val, data_id)
        imp_data =  pd.DataFrame(new_data , columns = data_val.columns.to_list()  , index=data_val.index.to_list())
        imp_data.index.name = 'obs_id'
        normalized_df=(imp_data-imp_data.mean())/imp_data.std()
    except :
        print('all columns missing')
        imp_data = data_val.copy()
        imp_data.index.name = 'obs_id'
        normalized_df = data_val.copy()
    #display(imp_data)
    #normalized_df.describe()
    all_imp_data = all_imp_data.append(imp_data)
    all_imp_data_norm = all_imp_data_norm.append(normalized_df)
    all_imp_id = all_imp_id.append(data_id)


final_data =  pd.concat([all_imp_id , all_imp_data] , axis=1)
final_data_norm = pd.concat([all_imp_id , all_imp_data_norm] , axis=1)
display(final_data)
display(final_data_norm)

final_data.to_csv('imp_data/'+cl+'_src_imp.csv')
final_data_norm.to_csv('imp_data/'+cl+'_src_imp_norm.csv')