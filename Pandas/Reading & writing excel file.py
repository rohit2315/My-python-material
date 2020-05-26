import pandas as pd 
   
#df=pd.read_excel('C:\\Users\\Rohit\\Documents\\stock.xlsx','Sheet1')# sheet 1 is the second argument as it is insheet1 of excel
# i wrote sheet as in small s and it showed error bcoz name is in caps s
#print(df)

#def convert_people_cell(cell):
    #if cell=='n.a':
     #   return 'sam walton'
    #return cell 

##def convert_eps_cell(cell):
   # if cell=='not available':
       # return None
    #return cell 

#df=pd.read_excel('C:\\Users\\Rohit\\Documents\\stock.xlsx','Sheet1',converters={'people':convert_people_cell,
#'eps':convert_eps_cell})
#print(df)







#print(df.to_excel('C:\\Users\\Rohit\\Documents\\new.xlsx',sheet_name='stocks'))
#print(df.to_excel('C:\\Users\\Rohit\\Documents\\new.xlsx',sheet_name='stocks',startrow=1,startcol=2,index=False))





# writing 2 dataframes in same excel file in diff sheets using  class excelwriter
df_stocks=pd.DataFrame({'tickers':['google','WMT','MSFT',"RIL",'TATA'],
'eps':[2.155,65,98,88,8],'revenue':[66,87,36,41,54],'price':[65,67,358,82,98]})
df_weather=pd.DataFrame({'Day':['1/1/2020','2/2/2020','5/4/2020','21/5/2020','8/6/2020','12/7/2020','20/8/2020','17/9/2020'],'Temperature':[18,19,30,
-5,20,21,35,45],'Events':['Rainy','Cloudy','Sunny','Snowy', 'Rainy','Rainy','Sunny','Sunny'],
'Windspeed':[80,90,40,20,50,70,45,39]})
with pd.ExcelWriter('C:\\Users\\Rohit\\Documents\\Stocks_weather.xlsx') as writer:

    df_stocks.to_excel(writer,sheet_name='stocks')
    df_weather.to_excel(writer,sheet_name='weather')
    