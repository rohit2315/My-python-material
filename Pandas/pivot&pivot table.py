# it allows to reshape or transform shape
import pandas as pd 

df=pd.read_csv("C:\\Users\\Rohit\\Documents\\weather1.csv")
print(df)
print(df.pivot(index='day',columns='city'))# index is row and columns 
print(df.pivot(index='day',columns='city',values='humidity'))# values allows u to see what u want


#pivot table allows you to summarize and aggregate data inside dataframe
df=pd.read_csv("C:\\Users\\Rohit\\Documents\\weather2.csv")
print(df.pivot_table(index='city',columns='day')) # it gives the avg of same date temp 
print(df.pivot_table(index='city',columns='day',aggfunc='sum'))# gives sum of same day by def its mean like above

#see documentation for other fun

print(df.pivot_table(index='city',columns='day',margins=True))# gives all column and row to give avg


df=pd.read_csv("C:\\Users\\Rohit\\Documents\\weather3.csv")
df['day']=pd.to_datetime(df['day'])
print(df)
# here need to  convert it into date format bcoz grouper method takes it as a strng
print(df.pivot_table(index=pd.Grouper(freq='M',key='day'),columns='city'))# gives avg of that month see end dates is shown in result values of 2 months
#grouper docm
