import pandas as pd 
import numpy as np 
s=pd.Series(np.array([1,3,4,7,8,9]))
print(s)
res=s.quantile(q=0.75)
print()
print('75th Percentile of the series is:::')
print(res)
print()
print('The elements that are above the 75th percentile::')
print(s[s>res])