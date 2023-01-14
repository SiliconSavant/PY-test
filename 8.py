import pandas as pd
dic={'Name':['Rchit','Mohit','Deepak','Anil','Pankaj','Sohit','Geeta'],
     'MarksinIP':[85,45,92,85,98,96,84]}
marks=pd.DataFrame(dic)
#Find 3 largest value for MarksinIP Column
print(marks.nlargest(3,['MarksinIP']))