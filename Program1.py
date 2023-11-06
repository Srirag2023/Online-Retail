import numpy as np
import pandas as pd
features=pd.read_csv("Features data set.csv")
sales=pd.read_csv("sales data-set.csv")
stores=pd.read_csv("stores data-set.csv")
#print(type(features))
#print("\nFirst 5 elements of features:\n",features.head())
#print("\nFirst 5 elements of sales:\n",sales.head())
#print("\nFirst 5 elements of stores:\n",stores.head())
#print("\nLast 5 elements of features:\n",features.tail())
#print("\nLast 5 elements of sales:\n",sales.tail())
#print("\nLastt 5 elements of stores:\n",stores.tail())
features['Date']=pd.to_datetime(features["Date"])
sales['Date']=pd.to_datetime(sales["Date"])
#print("Feature :",features.shape)
#print("Sales :",sales.shape)
#print("Stores :",stores.shape)
#features.info()
#sales.info()
#stores.info()
#print("\nColoumn in features table:\n",features.columns)
#print("\nColoumn in sales table:\n",sales.columns)
#print("\nColoumn in stores table:\n",stores.columns)
df=pd.merge(sales,features,on=['Store','Date','IsHoliday'],how='left')
df=pd.merge(df,stores,on=['Store'],how="left")
df=df.fillna(0)
df.sort_values(['Date','Weekly_Sales'],ascending=[True,False],inplace=True)
#print(df)
#print(df.shape)
#print(df.columns)
#print(df.describe())
#print(df.index)
#print(df.values)
subset=df[['Store','Date','Weekly_Sales','Fuel_Price','CPI','Unemployment']]
#print(subset.head())
#print(df.head())
#print(df.loc[0])
#print(df.loc[[0,99]])
#print(df.iloc[0])
#print(df.iloc[[0,99]])
#print(df.iloc[-1])
subset=df.loc[:,['Store','Date','Weekly_Sales']]
#print(subset.head())
subset=df.iloc[:,[2,4]]
#print(subset.head())
subset=df.iloc[-5::2,:]
#print(subset.head())
#print(df.head())
#rint(df.groupby('Date')['CPI'].mean().head(10))
#print(df.groupby(['Store','Date'])[['Weekly_Sales','Unemployment']].mean())
#print(df.groupby(['Store','Date'])[['Weekly_Sales','Unemployment']].mean().reset_index().head(10))
import matplotlib.pyplot as plt
df.groupby(['Store'])[['Weekly_Sales']].mean().plot()
df.plot(kind='scatter',x='Store',y='Weekly_Sales',rot=70)
df.boxplot(column='Weekly_Sales',by='Store')
plt.show()