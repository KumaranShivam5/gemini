import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd 
import seaborn as sns
import os 
font = {'size'   : 14}
plt.rc('font', **font)
plt.style.use('seaborn-dark-palette')
def hr():
    print('--------------------------------------------')

data = pd.read_csv('pred_result/NS_BH_train.csv')
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
    for r1 in rows:
    #plt.figure( figisze=(8,6))
        lr = np.int(len(rows)/2+1)
        for r2 in rows[:lr]:
            if(r1!=r2):
                hr()
                print('DOING : ' , r1 , 'X' , r2)
                data_curr = data.copy()
                

                s = sns.displot(
                    data= data_curr, x=r1 , y=r2,
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
                plt.savefig('pred_result/plots/feat_feat_corr/'+r1+'X'+r2+'.jpg')
                #plt.show()
                plt.close()

feat_feat_corr(data)