import pandas as pd 
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv")
print(df)
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv",skiprows=1)# if u add a row on top and u dont need that use skip
print(df)# see by adding a row ontop 
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv",header=1)# same as skip starts from row 1 ie 2 as index is 0,1
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv",header=None)
print(df)
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv",header=None,names=['ticker','eps','revenue','price','people'])
print(df)
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv",nrows=3)
print(df)
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv",na_values=['not available','n.a'])# replaced n.a and not avai with nan
print(df)
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\stock.csv",na_values={'eps':['not available','n.a'],'revenue':['not available','n.a',-1],
'people':['not available','n.a']})
print(df)
print(df.to_csv('C:\\Users\\Rohit\\Documents\\new.csv',index=False)) #writing to csv created a new csv file if not write indexit will show 0123 srno
print(df.to_csv('C:\\Users\\Rohit\\Documents\\new.csv',columns=['tickers','eps']))# the columns u want
print(df.to_csv('C:\\Users\\Rohit\\Documents\\new.csv',header=False)) # if u want no header dont write capital Header
