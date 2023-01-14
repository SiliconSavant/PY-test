import pandas as pd
disc={'Data1':[-5,-2,5,8,9,-6],
      'Data2':[2,4,10,15,-5,-8]}
df=pd.DataFrame(disc)
print(df)
print()
print("Dataframe after replacing negative values with 0::::")
df[df<0]=0
print(df)