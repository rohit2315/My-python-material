import pandas as pd 
df=pd.read_csv('add of the file')
df=pd.read_excel('')
weather_data={'Day':['1/1/2020','2/2/2020','5/4/2020','21/5/2020','8/6/2020','12/7/2020','20/8/2020','17/9/2020'],'Temperature':[18,19,30,
-5,20,21,35,45],'Events':['Rainy','Cloudy','Sunny','Snowy', 'Rainy','Rainy','Sunny','Sunny'],
'Windspeed':[80,90,40,20,50,70,45,39]}#dictionary
df=pd.DataFrame(weather_data)

weather_data=[('1/2/2020',20,15,'Rain'),('2/5/2020',30,60,'Sunny')]# list and tuple
df=pd.DataFrame(weather_data,columns=['Day','Temp','Windspeed','event'])
weather_data=[{'day':'1/2/2020','temperature':32,'windspeed':6,'event':'rain'},
{'day':'1/3/2020','temperature':40,'windspeed':25,'event':'snowy'}] #dictionary but in list
# there are diff ways google  it