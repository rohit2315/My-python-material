import pandas as pd 
df=pd.read_excel('C:\\Users\\Rohit\\Documents\\stocks1.xlsx',header=[0,1],index_col=[0])# remove index-col and see 
print(df)
print(df.stack())
print(df.stack(level=0))# by default its 1 by 0 it gets transposed
df_stacked=df.stack()
print(df_stacked)
print(df_stacked.unstack())# original 


df1=pd.read_excel('C:\\Users\\Rohit\\Documents\\stocks3.xlsx',header=[0,1,2],index_col=[0])
print(df1)
print(df1.stack())# took inner level row and transformed it
print(df1.stack(level=0))
print(df1.stack(level=1))