import pandas as  pd
india_weather=pd.DataFrame({'city':['mumbai','delhi','bangalore'],'temperature':[40,45,32],'humidity':[80,60,70]})
print(india_weather)
us_weather=pd.DataFrame({'city':['newyork','chicago','texas'],'temperature':[28,35,48],'humidity':[68,65,75]})
print(us_weather)
df=pd.concat([india_weather,us_weather])
print(df)
df=pd.concat([india_weather,us_weather],ignore_index=True)
print(df)
df=pd.concat([india_weather,us_weather],keys=['india','us'])
print(df)
print(df.loc['india'])# gives location of india using keys


temperature_df=pd.DataFrame({'city':['mumbai','delhi','bangalore'],'temperature':[45,35,49]})
print(temperature_df)
windspeed_df=pd.DataFrame({'city':['mumbai','delhi','bangalore'],'windspeed':[35,41,33]})
print(windspeed_df)

print(pd.concat([temperature_df,windspeed_df]))# appending is rowwise
print(pd.concat([temperature_df,windspeed_df],axis=1))#columnwise


temperature_df=pd.DataFrame({'city':['mumbai','delhi','bangalore'],'temperature':[45,35,49]})
print(temperature_df)
windspeed_df=pd.DataFrame({'city':['delhi','mumbai','bangalore'],'windspeed':[35,41,33]})
print(windspeed_df)
print(pd.concat([temperature_df,windspeed_df],axis=1))# here mumbai and delhi is not in same row

temperature_df=pd.DataFrame({'city':['mumbai','delhi','bangalore'],'temperature':[45,35,49]},index=[0,1,2])
print(temperature_df)
windspeed_df=pd.DataFrame({'city':['delhi','mumbai','bangalore'],'windspeed':[35,41,33]},index=[1,0,2])
print(windspeed_df)
print(pd.concat([temperature_df,windspeed_df],axis=1))# indexing help in arranging the values according to index position



s=pd.Series(['humid','dry','rain'],name='event')
print(s)
print(pd.concat([temperature_df,windspeed_df,s],axis=1))
