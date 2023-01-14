import pandas as pd
Profit={'TCS':{'Qtr1':2500,'Qtr2':2000,'Qtr3':3000,'Qtr4':2000},
        'WIPRO':{'Qtr1':2800,'Qtr2':2400,'Qtr3':3600,'Qtr4':2400},
        'L&T':{'Qtr1':2100,'Qtr2':5700,'Qtr3':35000,'Qtr4':2100}}
df=pd.DataFrame(Profit)
print(df)
print()
print('Mean of each row is:::::')
print(df.mean(axis=1))
print()
print('Dataframe after subtracting mean value of each row from each element of that row is:::')
print(df.sub(df.mean(axis=1),axis=0))