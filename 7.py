import pandas as pd
Profit={'TCS':{'Qtr1':2500,'Qtr2':2000,'Qtr3':3000,'Qtr4':2000},
        'WIPRO':{'Qtr1':2800,'Qtr2':2400,'Qtr3':3600,'Qtr4':2400},
        'L&T':{'Qtr1':2100,'Qtr2':5700,'Qtr3':35000,'Qtr4':2100}}
df=pd.DataFrame(Profit)
print(df)
print()
print('Column wise sum in datafrae is:::')
print(df.sum(axis=0))
#print mean value of each column
print()
print('Column wise mean value are::::::::')
print(df.mean(axis=0))
#Returns Column with minimum mean value
print()
print('Cloumn with minimum mean value is::::::::::')
df.mean(axis=0).idxmin()
