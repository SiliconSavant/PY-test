import pandas as pd
dic={'itemcat':['car','Ac','Aircoller','Washing Machine'],
     'itemname':['Ford','Hitachi','Symphony','LG'],
     'expenditure':[7000000,50000,12000,14000]}
quartsales=pd.DataFrame(dic)
print(quartsales)
qs=quartsales.groupby('itemcat')
print('Result after filtering DataFrame')
print(qs['itemcat','expenditure'].sum())