import numpy as np 
import pandas as pd 
from fits_to_csv import fits_to_csv 
from astropy.io import fits
import sys 
from progressbar import ProgressBar
pbar =  ProgressBar()

import readline, glob

class gen_training_data_mod():
    def complete(text, state):
        return (glob.glob(text+'*')+[None])[state]
    readlaine.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)

    def hr():
        print('_____________________________________________________________')

    def describe_data(data):
        rows , features =  data.shape
        #hr()
        print('Total Number of Sources : ', rows)
        print('Number of Features : ', features)
        classes = np.unique(data['class'])
        for c in classes:
            m , _  = data[data['class']==c].shape
            print('Class {:.0f} sources : {:.0f}'.format(c,m))



    def process_data(all_data):
        print('Reshuffling Data rows')
        all_data =  all_data.sample(frac=1).reset_index(drop=True)
        all_data.index.name =  "index_compiled"
        print('Formatting Data')
        m, n =  all_data.shape
        total = m*n
        count = 0
        for i in pbar(range(m)):
            for j in range(n):
                count+=1
                per = (count/total)*100
                if isinstance(all_data.iloc[i,j],str):
                    try:
                        all_data.iloc[i,j] =  float(all_data.iloc[i,j])
                    except:
                        all_data.iloc[i,j]=0
        hr()
        print('Normalizing Data')
        #np.amax(all_data)
        for i in range(2,n):
            max_non_zero = np.amax(all_data.iloc[:,i])
            if(max_non_zero==0):
                continue
            else:
                all_data.iloc[:,i] = all_data.iloc[:,i] / np.amax(all_data.iloc[:,i]) 
        print(np.amax(all_data))
        if __name__ == '__main__':
            if(sys.argv[2]):
                save_file = str(sys.argv[2])
                all_data.to_csv(save_file)

    def gen_training_data():
        num_of_class = 0 
        more_class = 'y'
        data =  pd.DataFrame()
        if __name__ == '__main__':
            rows_file = str(sys.argv[1])
        else:
            rows_file =  str('Enter rows JSON file : ')
        while(more_class=='y'):
            in_file = str(input('enter Data fits file : '))
            temp_data =  fits_to_csv(in_file, rows_file, num_of_class)
            num_of_class+=1
            print('Data appended')
            data = data.append(temp_data)
            hr()
            more_class =  str(input('More dataset ? y/n : '))

        process_choice =  input('Process Data ? y/n :')
        if(process_choice=='y'):
            process_data(data)
        hr()
        return (data)

    if __name__ == '__main__':
        gen_training_data()
        #progress_bar()