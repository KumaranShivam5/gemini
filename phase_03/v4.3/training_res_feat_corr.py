import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd 
import seaborn as sns
import os 

from tqdm import tqdm
font = {'size'   : 14}
plt.rc('font', **font)
plt.style.use('seaborn-dark-palette')
def hr():
    print('--------------------------------------------')

data = pd.read_csv('pred_result/NS_BH_train.csv')

h_params= ['hard_hm_hilim' ,'hard_hm_lolim' ,'hard_hs_hilim' ,'hard_hs_lolim' ,'hard_ms_hilim' ,'hard_ms_lolim', 'hard_hm' ,  'hard_hs' , 'hard_ms' ]

single_params_lim = ['hard_hm_hilim' ,'hard_hm_lolim' ,'hard_hs_hilim' ,'hard_hs_lolim' ,'hard_ms_hilim' ,'hard_ms_lolim', 'flux_powlaw_hilim' ,'flux_powlaw_lolim', 'powlaw_gamma_hilim' , 'powlaw_gamma_lolim' ,'powlaw_nh_hilim' , 'powlaw_nh_lolim' ,'powlaw_ampl_hilim' , 'powlaw_ampl_lolim' , 'bb_ampl_lolim' ,'bb_ampl_hilim' ,  'flux_brems_lolim' , 'flux_brems_hilim' , 'brems_kt_hilim' ,'brems_kt_lolim' ,'brems_nh_hilim' ,'brems_nh_lolim' , 'bb_kt_hilim' , 'bb_kt_lolim' ,'bb_nh_hilim' , 'bb_nh_lolim' ,  ]


data = data.drop(single_params_lim , axis=1)
print(data)
rows = [t for t in data][13:]
#print(rows)
#plt.figure( figisze=(8,6))


def prob_feat_corr():
    os.system('rm -r pred_result/plots/feat_prob_corr')
    os.system('mkdir pred_result/plots/feat_prob_corr')
    for r in rows:
    #plt.figure( figisze=(8,6))
        hr()
        print('DOING : ' , r)
        
        s = sns.displot(
            data= data, x='prob' , y=r,
            hue='pred_class' , 
            kind='kde' , 
            cumulative = 0,
            rug=True, height=6 , aspect=8/6 ,
            palette='copper',
            col='is_ok',
            )
        #s.set_titles("Predicted prob distribution")
        #plt.xlim(0.5 , 1.0)
        #plt.title("Empirical cumulative distribution")
        plt.savefig('pred_result/plots/feat_prob_corr/'+r+'.jpg')
        #plt.show()
        plt.close()



def feat_feat_corr(data):
    os.system('rm -r pred_result/plots/feat_feat_corr')
    os.system('mkdir pred_result/plots/feat_feat_corr')
    nr = len(rows)
    for i in tqdm(range(1,nr)):
    #plt.figure( figisze=(8,6))
        #lr = int(len(rows)/2+1)
        for j in tqdm(range(i)):
            r1 = rows[i]
            r2 = rows[j]
            if(r1!=r2):
                
                #print('DOING : ' , r1 , 'X' , r2)
                data_curr = data.copy()
                
                try:
                    s = sns.displot(
                        data= data_curr, x=r1 , y=r2,
                        hue='pred_class' , 
                        kind='kde' , 
                        cumulative = 0,
                        rug=True, height=4 , aspect=8/6 ,
                        palette='copper',
                        col='is_ok',
                        )
                    #s.set_titles("Predicted prob distribution")
                    #plt.xlim(0.5 , 1.0)
                    #plt.title("Empirical cumulative distribution")
                    plt.savefig('pred_result/plots/feat_feat_corr/'+r1+'_X_'+r2+'.jpg')
                    #plt.show()
                    plt.close()
                except:
                    print('could not do it')



def feat_feat_prob_corr(data):
    os.system('rm -r pred_result/plots/feat_feat_prob_corr')
    os.system('mkdir pred_result/plots/feat_feat_prob_corr')
    nr = len(rows)
    for i in tqdm(range(1,nr)):
    #plt.figure( figisze=(8,6))
        #lr = int(len(rows)/2+1)
        for j in tqdm(range(i)):
            r1 = rows[i]
            r2 = rows[j]
            if(r1!=r2):
                
                #print('DOING : ' , r1 , 'X' , r2)
                data_curr = data.copy()
                
                try:
                    s = sns.displot(
                        data= data_curr, x=r1 , y=r2,
                        hue='is_ok' , 
                        kind='kde' , 
                        cumulative = 0,
                        rug=True, height=3 , aspect=8/6 ,
                        palette='copper',
                        )
                    #s.set_titles("Predicted prob distribution")
                    #plt.xlim(0.5 , 1.0)
                    #plt.title("Empirical cumulative distribution")
                    plt.savefig('pred_result/plots/feat_feat_prob_corr/'+r1+'_X_'+r2+'.jpg')
                    #plt.show()
                    plt.close()
                except:
                    print('could not do it')




#feat_feat_corr(data)

feat_feat_prob_corr(data)