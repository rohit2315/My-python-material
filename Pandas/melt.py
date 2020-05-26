import pandas as pd 
df=pd.read_csv('C:\\Users\\Rohit\\Documents\\data1.csv')
print(df)
df1=pd.melt(df,id_vars=['day'])# id_vars is the thing u want on x axis or the column u wnt intact
print(df1)
print(df1[df1['variable']=='chicago'])# iltering to a particular city
df1=pd.melt(df,id_vars=['day'],var_name='city',value_name='temperature')
print(df1)

n=input('ent')
b=input('engt')
if n[-1]=='1':

    
    a=int(n[-2])*int(b[-1])
    print(str(a)+'1')
     
         
else:
    print('false')  

    
  
      

