
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
df = df.set_index(pd.DatetimeIndex(df['Date'].values))
#print( df )

#plot the closing price on a chart
plt.figure(figsize=(15,5)) #width = 15, height = 5
plt.plot(df.Close, color='black')
plt.title('Stock Closing Price')
plt.xlabel('Date')
plt.ylabel(' Price USD')
plt.show()

#Calculate the max and min close price
maximum_price = df['Close'].max()
minimum_price = df['Close'].min()

difference = maximum_price - minimum_price
first_level = maximum_price - difference * 0.236
second_level = maximum_price - difference * 0.382
third_level = maximum_price - difference * 0.5
fourth_level = maximum_price - difference * 0.618



#Short term exponential moving average
ShortEMA = df.Close.ewm(span=12, adjust=False).mean()
#Long term exponential moving average
LongEMA = df.Close.ewm(span=26, adjust=False).mean()
#Clac MACD
MACD = ShortEMA - LongEMA
#Calc Signal Line
signal = MACD.ewm(span=9, adjust = False).mean()


new_df = df
plt.figure(figsize=(13, 7))
plt.title('Fibonnacci Retracement')
plt.plot(new_df.index, new_df['Close'])
plt.axhline(maximum_price, linestyle='--', alpha=0.7, color = 'red')
plt.axhline(first_level, linestyle='--', alpha=0.7, color = 'orange')
plt.axhline(second_level, linestyle='--', alpha=0.7, color = 'yellow')
plt.axhline(third_level, linestyle='--', alpha=0.7, color = 'green')
plt.axhline(third_level, linestyle='--', alpha=0.7, color = 'blue')
plt.axhline(minimum_price, linestyle='--', alpha=0.7, color = 'purple')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price in USD',fontsize=18)
plt.show()

# new column for the data
df['MACD'] = MACD
df['Signal Line'] = signal

#function for our strategy to get upper and lower fib level of the current price
def getLevels(price):
    if price >= first_level:
        return(maximum_price, first_level)
    elif price >= second_level:
        return (first_level, second_level)
    elif price >= third_level:
        return(second_level, third_level)
    elif price >= fourth_level:
        return(third_level, fourth_level)
    else:
        return (fourth_level, minimum_price)

#function tradingbot: buy when the signal line crossed above or below the MACD line and
#the current price crosses above or below the last fib level

def strategy(df):
    buy_list = []
    sell_list=[]
    flag = 0
    last_buy_price = 0

    #loop through data
    for i in range(0, df.shape[0]):
        price = df['Close'][i]

        if i == 0:
            upper_level, lower_level = getLevels(price)
            buy_list.append(np.nan)
            sell_list.append(np.nan)
        #check if current price is greater than or equal to the upper level
        #or less than or equal to lower level
        elif price >= upper_level or price <+ lower_level:

        #ck MACD line crossed above or below the signal line
            if df['Signal Line'][i]> df['MACD'][i] and flag == 0:
                last_buy_price = price
                buy_list.append(price)
                sell_list.append(np.nan)
                #set flag to one to when share is bought
                flag = 1
            elif df['Signal Line'][i] < df['MACD'][i] and flag == 1 and price >= last_buy_price:
                buy_list.append(np.nan)
                sell_list.append(price)
                #set flag to zero when share is sold
                flag = 0
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)

    #Update new levels
    upper_level, lower_level = getLevels(price)
    return buy_list, sell_list

#Create buy and sell columns
buy, sell = strategy(df)
df['Buy_Signal_Price'] = buy
df['Sell_Signal_Price'] = sell

df













