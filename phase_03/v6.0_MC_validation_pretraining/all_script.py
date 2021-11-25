import numpy as np 
import pandas as pd 

src_class = input('BH/NS : ')
frac = 1

data = pd.read_csv('source_list/'+src_class+'_data_clean_source_list.csv')
data =  data.sample(frac=1)
print(data.describe())
frac_no = int(len(data)*frac)
train_data = data.iloc[:frac_no]
test_data = data.iloc[frac_no:]
print(train_data)
print(test_data)
train_data.to_csv('source_list/final_list/'+src_class+'_train.csv')
test_data.to_csv('source_list/final_list/'+src_class+'_test.csv')



import os

ctg = src_class

def hr():
    print('----------------------------------------------------------------------------')


data= pd.read_csv('source_list/final_list/'+ctg+'_train.csv')
ch_names = [di.replace(' ' ,'_')[:-1] for di in data['B_NAME']]
a_names = [di.replace(' ' ,'_')[:-1]+'.csv' for di in data['A_NAME']]
src_id = [si[:6] for si in data['SRC_ID']]
#print(src_id)
os.system('rm -r '+ctg+'_data/train/')
os.system('mkdir '+ctg+'_data/train/')
for c,s ,a in zip(ch_names , src_id , a_names):
    try:
        src = ctg+'_data_all/'+c+'.csv' 
        ## adding source_id in file names
        dest = ctg+'_data/train/'+ s+'-'+c+'#'+a 
        print('Copying' , c )
        os.system('cp '+src+' '+dest)
    except:
        hr()
        print('check source : ' , c )
        hr()

hr()
print('TRAINING DATA STORED')
hr()

data= pd.read_csv('source_list/final_list/'+ctg+'_test.csv')
ch_names = [di.replace(' ' ,'_')[:-1] for di in data['B_NAME']]
a_names = [di.replace(' ' ,'_')[:-1]+'.csv' for di in data['A_NAME']]
src_id = [si[:6] for si in data['SRC_ID']]
#print(src_id)

os.system('rm -r '+ctg+'_data/test/')
os.system('mkdir '+ctg+'_data/test/')
for c,s ,a in zip(ch_names , src_id , a_names):
    try:
        src = ctg+'_data_all/'+c+'.csv' 
        ## adding source_id in file names
        dest = ctg+'_data/test/'+ s+'-'+c+'#'+a 
        print('Copying' , c )
        os.system('cp '+src+' '+dest)
    except:
        hr()
        print('check source : ' , c )
        hr()




from ipywidgets import IntProgress
from IPython.display import display

src_class = src_class

def hr():
    print('_______________________________________________________________________________________')


def to_float(d):
    temp = []
    for di in d:
        
        try:
            temp.append(float(di))
        except Exception as e:
            print(e)
            print('NaN detected resetting value')
            temp.append(np.NAN)
    temp = np.asarray(temp)
    return temp 

def correct_bool(arr):
    temp = []
    for a in arr:
        #print(a , type(a))
        if(type(a) == bool):
            temp.append(a)
        else:
            if(a==' TRUE'):
                temp.append(True)
            elif(a=='FALSE'):
                temp.append(False)
            else:
                temp.append(np.NaN)  
    return temp

def run_script(set_type):
    #os.system('rm -r '+src_class+'_data/'+set_type+'/')
    #os.system('mkdir ')
    os.system('ls '+src_class+'_data/'+set_type+'/ > file_list')
    file_list = pd.read_csv('file_list' , names=['names'])['names']
    display(file_list)

    hr()

    data = pd.DataFrame()

    for file in file_list:
        data_temp =  pd.read_csv(src_class+'_data/'+set_type+'/'+file)
        ## extracting source_id from file names 
        src_id_name = file[:6]
        src_id = [src_id_name]*len(data_temp)
        src_id = np.asarray(src_id)
        data_temp.insert(0 ,'src_id' , src_id)
        src_n_name = file[29:-4].replace('_' , ' ')
        src_n = [src_n_name]*len(data_temp)
        src_n = np.asarray(src_n)
        data_temp.insert(0 ,'src_n' , src_n)
        data =  data.append(data_temp)


    data.describe()
    hr()
    #print(data['src_id'])

    # next we will combine all bands data. SOme parameters like pfotometry , variability are in different bands  , we will combine them as mean to reomve sparsity in data

    band_params = [ 'photflux_aper' ,'photflux_aper_lolim' , 'photflux_aper_hilim' , 'flux_aper' , 'flux_aper_lolim' , 'flux_aper_hilim' , 'var_index' ,'var_prob' , 'ks_prob' , 'kp_prob' ,'var_sigma' ,'var_mean' , 'var_min' ,  'var_max' , 'var_inter_index' , 'var_inter_prob' , 'var_inter_sigma']



    filters = ['_b' ,'_h' ,'_m' ,'_u' ,'_s']

    band_params_var = ['var_mean']
    data_band_mean = pd.DataFrame()
    data_band_mean.index.name = 'name '
    for param in band_params:
        temp_row = [param+f for f in filters]
        data_temp = data[temp_row]
        for j in data_temp:
            data_temp[j] = to_float(data_temp[j].to_numpy())
        #display(data_temp)
        #temp_mean = to_float(data_temp)
        temp_mean =  data_temp.mean(axis=1)
        data_band_mean.insert(0 , param , temp_mean)
        
        #display(temp_mean)
    #display(data_band_mean)
    #data_band_mean =  data_band_mean.dropna(axis=0 , how='all')
    data_band_mean =  data_band_mean.dropna(axis=1 , how='all')
    data_band_mean.to_csv('temp.csv')
    #data_band_mean.describe()
    display(data_band_mean)



    data_band_mean.describe()

    # ## Non-Band Params
    # Next we will add all the parameters which are band independent 
    flux_params = ['photflux_aper' ,'photflux_aper_lolim' , 'photflux_aper_hilim' , 'flux_aper' , 'flux_aper_lolim' , 'flux_aper_hilim' ]
    flux_params_extend = []
    for fp in flux_params:
        for f in filters:
            temp = fp+f
            flux_params_extend.append(temp)


    single_params = flux_params_extend+ ['hard_hm' ,  'hard_hs' , 'hard_ms' , 'flux_powlaw'  , 'powlaw_gamma' ,  'powlaw_gamma_rhat' , 'powlaw_nh' , 'powlaw_nh_rhat' , 'powlaw_ampl' , 'powlaw_ampl_rhat' , 'powlaw_stat' , 'flux_bb' , 'flux_bb_hilim' , 'flux_bb_lolim' , 'bb_kt' , 'bb_nh' , 'bb_nh_rhat' , 'bb_ampl' ,  'bb_stat' , 'flux_brems' , 'brems_kt' , 'brems_nh' ,'brems_nh_rhat' ,'brems_stat' , 'flux_apec' ,  'apec_kt' , 'apec_abund' , 'apec_abund_rhat' ,'apec_z' ,  'apec_norm' , 'apec_nh' , 'apec_stat']

    obs_info_params = [ 'livetime','significance','likelihood','pileup_flag','mstr_sat_src_flag','mstr_streak_src_flag'   ,'gti_obs' ]
    single_params_lim = ['hard_hm_hilim' ,'hard_hm_lolim' ,'hard_hs_hilim' ,'hard_hs_lolim' ,'hard_ms_hilim' ,'hard_ms_lolim', 'flux_powlaw_hilim' ,'flux_powlaw_lolim', 'powlaw_gamma_hilim' , 'powlaw_gamma_lolim' ,'powlaw_nh_hilim' , 'powlaw_nh_lolim' ,'powlaw_ampl_hilim' , 'powlaw_ampl_lolim' , 'bb_ampl_lolim' ,'bb_ampl_hilim' ,  'flux_brems_lolim' , 'flux_brems_hilim' , 'brems_kt_hilim' ,'brems_kt_lolim' ,'brems_nh_hilim' ,'brems_nh_lolim' , 'bb_kt_hilim' , 'bb_kt_lolim' ,'bb_nh_hilim' , 'bb_nh_lolim' , 'flux_apec_hilim' , 'flux_apec_lolim' ,'apec_kt_hilim' ,'apec_kt_lolim' ,'apec_abund_hilim' , 'apec_abund_lolim' ,'apec_z_hilim' , 'apec_z_lolim' ,'apec_norm_hilim' ,'apec_norm_lolim' , 'apec_nh_hilim' ,'apec_nh_lolim' ]



    #print(single_params)
    #print(len(single_params))


    # ### FIlter by flux
    # > Choose only flux below a certain threshold as found out by globular cluster analysis


    data_single = data[single_params+single_params_lim]
    for d in data_single:
        data_single[d] = to_float(data_single[d])
    #data_single = data_single.dropna(axis=1 , how='all')
    #data_single.describe()
    display(data_single)



    data_single.describe()
    data_info = data[obs_info_params]
    data_combine = pd.concat([data_info , data_band_mean , data_single] , axis=1)
    data_combine.describe()

    # ## Flux Scaling 
    # We need to take log values of all flux columns 
    # (not sure about error propogation in hilim and lolim)

    flux_rows = flux_params_extend+['flux_aper' , 'flux_aper_lolim' , 'flux_aper_hilim' ,'flux_powlaw'  , 'flux_bb'  , 'flux_brems' ,  'flux_apec' , 'flux_bb_hilim' , 'flux_bb_lolim',  'flux_powlaw_hilim' ,'flux_powlaw_lolim', 'flux_brems_lolim' , 'flux_brems_hilim' , 'flux_apec_hilim' , 'flux_apec_lolim' ]

    for f in flux_rows:
        try:
            data_combine[f] =  -np.log10(data_combine[f])
        except Exception as e:
            print('Not found:' , e)
    data_combine.describe()



    data_combine=  data_combine.dropna(axis=1 , how='all')
    data_combine.describe()

    data_combine.insert(0,'src_name' , data['src_n'])
    data_combine.insert(0,'src_id' , data['src_id'])


    hr()
    print('ALL DATA COMBINED')
    hr()
    display(data_combine)
    hr()




    data_final = data_combine[data_combine['pileup_flag']==False]
    data_final =  data_final[data_final['mstr_sat_src_flag']==False]
    data_final =  data_final[data_final['mstr_streak_src_flag']==False]
    data_final.insert(0 , 'class' ,len(data_final)*[src_class])

    #data_final.insert(0 , 'src_id' , data['src_id'])
    print(data_final)

    data_final.index.name = 'index'
    data_final = data_final.drop(columns=['mstr_sat_src_flag' , 'mstr_streak_src_flag' , 'pileup_flag'])
    data_final.index.name = 'index'
    print(data_final.describe())

    data_final.to_csv('processed_data/'+src_class+'_'+set_type+'.csv')



print('TRAIN DATA')
run_script('train')
hr()
#print('TEST DATA')
#hr()
#run_script('test')