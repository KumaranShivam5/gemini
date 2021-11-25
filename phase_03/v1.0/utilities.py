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
