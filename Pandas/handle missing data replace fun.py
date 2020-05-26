import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\weatherdata.csv")
print(df)
#new_df=df.replace(-99999,np.nan)#-99999 is a special value which u can get whileimporting a data from a source its like a empty value
#print(new_df)
new_df=df.replace({'temperature':-99999,'windspeed':-99999,'events':'0'},np.nan)
#print(new_df)
new_df=df.replace({-99999:np.nan,'0':'sunny'})
#print(new_df)
new_df=df.replace({'temperature':'[A-Za-z]','windspeed':'[A-Za-z]'},'',regex=True) 
#if want to replace a pattern use regex 
print(new_df)
df=pd.DataFrame({'marks':['exceptional','good','poor','average','good'],'students':['son','rob','bob','sob','lob']})
print(df)
new_df=df.replace(['poor','average','good','exceptional'],[1,2,3,4])#replacing list with list by mapping
print(new_df)