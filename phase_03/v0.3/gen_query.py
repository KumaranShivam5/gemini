import pandas as pd 
data  = pd.read_csv('chandra_pulsar_small.csv')
ids = data['name']
search_coll = "SELECT *\nFROM master_source m\nWHERE m.name in ("
for i in ids:
    search_coll += "'"+i+"',"
search_coll =  search_coll[:-1]
search_coll +=')'
print(search_coll)
with open("query.adql", "w") as text_file:
    text_file.write(search_coll)