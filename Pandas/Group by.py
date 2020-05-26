import pandas as pd
df=pd.read_csv('C:\\Users\\Rohit\\Documents\\cityweather.csv')
print(df)
g=df.groupby('city')# we are splitting data in to groups with city as key and all its data as value

for city,city_df in g:#data frame corresponding to city
    print(city)
    print(city_df)

print(g.get_group('mumbai'))  # giving dataframe of mumbai

print(g.max())# gives max temp of each city
print(g.mean())# splitting into smaller groups--->(apply)running analytics------>combining to give finalresult
print(g.describe())
import matplotlib.pyplot as plt

print(g.plot())
plt.show()
# many more groupbby methods on documentation
