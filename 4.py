import pandas as pd 
sales={'InvoiceNo':[1001,1002,1003,1004,1005,1006,1007],
       'ProductName':['LED','AC','Deodrant','Jeans','Books','Shoes','Jacket'],
       'Quantity':[2,1,2,1,2,1,1],
       'Price':[65000,55000,500,2500,950,3000,2200]
       }
df=pd.DataFrame(sales)
print(df['Price'].describe(),round(2))
