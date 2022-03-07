
"""
Trading algorithm using Fibonacci 
"""


import numpy as np
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data as dp
import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


#collect the data 
start1 = datetime.datetime(2021, 5, 22)
end1 = datetime.datetime(2022, 1, 14)

# store the data
df = dp.DataReader('^GSPC', 'yahoo', start=start1, end=end1)


df.to_csv('C:\\Users\\operator\\Documents\\Python\\SP500CFAmonthly.csv')

#Set the date as the index
'''df = df.set_index(pd.DatetimeIndex(df['Date'].values))'''
#print( df )

'''#plot the closing price on a chart
plt.figure(figsize=(15,5)) #width = 15, height = 5
plt.plot(df.Close, color='black')
plt.title('Stock Closing Price')
plt.xlabel('Date')
plt.ylabel(' Price USD')
plt.show()'''

#Calculate the max and min close price
maximum_price = df['Close'].max()
minimum_price = df['Close'].min()
difference = maximum_price - minimum_price        
first_level = maximum_price - difference * 0.236   
second_level = maximum_price - difference * 0.382     
third_level = maximum_price - difference * 0.618 

new_df = df
plt.figure(figsize=(13, 7))
plt.title('Fibonnacci Retracement')
plt.plot(new_df.index, new_df['Close'])
plt.axhline(maximum_price, linestyle='--', alpha=0.7, color = 'red')
plt.axhline(first_level, linestyle='--', alpha=0.7, color = 'orange')
plt.axhline(second_level, linestyle='--', alpha=0.7, color = 'yellow')
plt.axhline(third_level, linestyle='--', alpha=0.7, color = 'green')
plt.axhline(minimum_price, linestyle='--', alpha=0.7, color = 'purple')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price in USD',fontsize=18)
plt.show()