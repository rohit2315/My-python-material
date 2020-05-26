import pandas as pd 
df=pd.read_csv('C:\\Users\\Rohit\\Documents\\weather_data.csv')
print(df)
print(type(df.day))
print(type(df.day[0]))# csv file reads as string
df=pd.read_csv('C:\\Users\\Rohit\\Documents\\weather_data.csv',parse_dates=['day'])#coverted into date format
print(df)
print(type(df.day[0]))#<class 'pandas._libs.tslibs.timestamps.Timestamp'>
print(df.set_index('day',inplace=True))



#method to cover nan values
new_df=df.fillna(0)# not modifying original data frame that why taken in a variable
print(new_df)

new_df=df.fillna({'temperature':0,'windspeed':0,'events':'no event'})
print(new_df)
new_df=df.fillna(method='ffill')#ffill means carry fwd that  previousvalue 
print(new_df)
new_df=df.fillna(method='bfill')#bfill means carry bkwd that  previousvalue 
print(new_df)
new_df=df.fillna(method='bfill',axis='columns')#values will be copied horizontally  
print(new_df)
new_df=df.fillna(method='ffill',limit=1)#ffill means carry fwd that  previousvalue but to a limit like see 7 is copied down only once
print(new_df)


new_df=df.interpolate()# it gives a intermediate guess value betn 2 values like 30 betwn 32&28 see documentation
print(new_df)
new_df=df.interpolate(method='time')# time takes date in consideration also and gives the value closer to what date it is near to like
# if 2,6,7 date then 6 value will be somewhat estimated close to 7
print(new_df)


new_df=df.dropna() # only shows value other than na
print(new_df)


new_df=df.dropna(how='all') # only shows value other than which has all na value
print(new_df)

new_df=df.dropna(thresh=1) # it should have atleast 1  value then it will show
print(new_df)

new_df=df.dropna(thresh=2) # it should have atleast 2  value then it will show
print(new_df)


dt=pd.date_range('01-01-2020','01-09-2020')#here i am inserting 1 and 7 jan  all 
idx=pd.DatetimeIndex(dt)# see why day header is missing
df=df.reindex(idx)
print(df)
