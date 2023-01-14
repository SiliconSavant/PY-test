import pandas as pd
dic={'Name':['Rohit','Mohit','Deepak','Rohit','Deepak','Sohit','Geeta'],
     'MarksinIP':[85,45,92,85,92,96,84]}
marks=pd.DataFrame(dic)
#Find duplicate rows
duplicaterow=marks[marks.duplicated(keep=False)]
print(duplicaterow)
