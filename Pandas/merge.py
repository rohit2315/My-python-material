import pandas as pd 
df1=pd .DataFrame({'city':['newyork','chicago','orlando'],'temperature':[25,30,33]})
df2=pd.DataFrame({'city':['newyork','chicago','orlando'],'humidity':[20,33,40]})
print(pd.merge(df1,df2,on='city'))



df1=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[25,30,33,41]})
df2=pd.DataFrame({'city':['newyork','chicago',],'humidity':[20,33]})
print(pd.merge(df1,df2,on='city')) #it wont print balti and orlan bcoc how=inner by def  which means intersection or innerjoin



df1=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[25,30,33,41]})
df2=pd.DataFrame({'city':['newyork','chicago',],'humidity':[20,33]})
print(pd.merge(df1,df2,on='city',how='outer'))# outer join means union

#left and right decided by order

df1=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[25,30,33,41]})
df2=pd.DataFrame({'city':['newyork','chicago','san-fransisco'],'humidity':[20,33,24]})
print(pd.merge(df1,df2,on='city',how='left'))#left join means only first union of first df





df1=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[25,30,33,41]})
df2=pd.DataFrame({'city':['newyork','chicago','san-fransisco'],'humidity':[20,33,24]})
print(pd.merge(df1,df2,on='city',how='right'))



df1=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[25,30,33,41]})
df2=pd.DataFrame({'city':['newyork','chicago','san-fransisco'],'humidity':[20,33,24]})
print(pd.merge(df1,df2,on='city',how='outer',indicator=True))# indicator tells which value comes from which df






df1=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[25,30,33,41],
'humidity':[20,33,24,25]})
df2=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[28,29,36,40],'humidity':[32,22,26,18]})
print(pd.merge(df1,df2,on='city'))#append x and y as suffix 



df1=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[25,30,33,41],
'humidity':[20,33,24,25]})
df2=pd .DataFrame({'city':['newyork','chicago','orlando','baltimore'],'temperature':[28,29,36,40],'humidity':[32,22,26,18]})
print(pd.merge(df1,df2,on='city',suffixes=['_left','_right']))