import pandas as pd
#df=pd.read_excel("C:\\Users\\Rohit\\Documents\\Pandas.xlsx")#imported or 
weather_data={'Day':['1/1/2020','2/2/2020','5/4/2020','21/5/2020','8/6/2020','12/7/2020','20/8/2020','17/9/2020'],'Temperature':[18,19,30,
-5,20,21,35,45],'Events':['Rainy','Cloudy','Sunny','Snowy', 'Rainy','Rainy','Sunny','Sunny'],
'Windspeed':[80,90,40,20,50,70,45,39]}
df=pd.DataFrame(weather_data)#dataframe is about rows and coloumns
print(df)
print(df.shape)
rows,columns=df.shape
print(rows)
print(df.head())#head gives convinence of printing only few rows or pass in some value
print(df.head(2))
print(df.tail(2))# tail last two rows
print(df[2:5])
print(columns)
print(df.Day)
print(df['Events'])
print(type(df['Events']))#<class 'pandas.core.series.Series'>
print(df[["Day","Events"]])#printing the columns we want
print(df['Temperature'].max())
print(df['Temperature'].mean())
print(df['Temperature'].min())
print(df.describe())# gives the whole req description
print(df[df.Temperature>=32])
print(df[df.Temperature==df.Temperature.max()])# the whole row of max temp df[df.Temperature==df['Temperature'].max()
print(df[['Day','Temperature']][df.Temperature==df.Temperature.max()])


print(df.set_index('Day',inplace=True))# if not write inplace it will not change the original  
print(df)
print(df.loc['21/5/2020'])
print(df.reset_index(inplace=True))
print(df)


#Other operation see pandas documentation on google