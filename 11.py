import pandas as pd
import numpy as np
empdata={'empid':[101,102,103,104,105,106],
         'ename':['Sachin','Vinod','Lakhbir',np.nan,'Devinder','UnaSelvi'],
         'Doj':['12-01-2012','15-01-2012','05-09-2007','17-01-2012',np.nan,'16-01-2012']}
df=pd.DataFrame(empdata)
print(df)
df=df.fillna({'ename':999,'Doj':999})
print()
print(df)