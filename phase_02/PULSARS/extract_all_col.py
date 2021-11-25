import numpy as np 
obs_ids = np.loadtxt('chandra_fermi_pulsars.csv' , usecols=[0] , dtype='str' , delimiter=',')
print(obs_ids)
st = '('
for i in obs_ids:
    #print(i)
    if(i[0]==' '):
        i = i[1:]
    st += "'"+i+"',"
st = st[:-1]
st+=')'
q = "SELECT * \nFROM master_source m \nWHERE m.name IN "+st
#q = "SELECT *\n FROM master_source m \nWHERE m.name IN "+st
f = open('query.adql' , 'w')
f.write(q)
f.close()