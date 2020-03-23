import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import numpy as np 
from pandas.plotting import register_matplotlib_converters
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

#print(time.ctime())
register_matplotlib_converters()
default_time_value = 3
current_stock = yf.Ticker("MSFT")
stock_info_dict = current_stock.info
stock_short_name = stock_info_dict.get("shortName")
chart_timeframes = ['1-Day', '1-Month', '6-Month', '1-Year', '5-Year', 'Max Length']
current_timeframe = chart_timeframes[default_time_value]
chart_periods = ['1d','1mo','6mo','1y','5y','max']
current_period = chart_periods[default_time_value]
#print(time.ctime())

#print(msft_monthly_prices.iat[row_length-1,3])




def set_current_stock(stock_ticker_string):
    global current_stock
    global stock_info_dict
    global stock_short_name
    current_stock = yf.Ticker(stock_ticker_string)
    stock_info_dict = current_stock.info
    stock_short_name = stock_info_dict.get("shortName")
    build_chart()

def set_current_timeframe(timeframe):
    global current_timeframe
    current_timeframe = timeframe

def set_current_period(period):
    global current_period
    current_period = period

def get_stock_name(tickerSymbol):
    current_stock = yf.Ticker(tickerSymbol)
    stock_info_dict = current_stock.info
    stock_short_name = stock_info_dict.get("shortName")
    return stock_short_name




# Use this function to get the live price when a previous and recent call has not already been made for a dataframe with the daily or monthly price data
# If such a dataframe has already been loaded, simply access the latest price in that DF 
# We do this to prevent unnecessary calls to the Yahoo API which slow us down
# A function for finding the current/most recent price from an already loaded dataframe is below this function
def get_live_price_first(stock_ticker):
    current_price_df = stock_ticker.history(period="1d")
    return current_price_df.iat[0,3]


#Use this function to get the live price when you have recently loaded a dataframe with price history via the ____.history() call
#Useful for situations where the cost of making an API call is not justified by any new data
#May configure future logic to swap between these two functions if market is open (9-4 M-F) or closed, will depend on how often the API is queried by the finished app
def get_live_price(stock_price_dataframe):
    dummy_DF = pd.DataFrame()
    if type(stock_price_dataframe) == type(dummy_DF) and stock_price_dataframe.columns[3] == "Close":
        return stock_price_dataframe.iat[len(stock_price_dataframe)-1,3]
    else:
        return "Error: Argument passed not a valid dataframe containing Closing price data in the third column"
    


current_price_dataframe = pd.DataFrame()

def request_price_dataframe(stock_ticker):
    global current_price_dataframe
    if current_period == '1d':
         current_price_dataframe = stock_ticker.history(period= current_period, interval = '15m')
    elif current_period == '5y':
        current_price_dataframe = stock_ticker.history(period= current_period, interval = '1wk')
    elif current_period == 'max':
        current_price_dataframe = stock_ticker.history(period= current_period, interval = '1mo')
    else:   
        current_price_dataframe = stock_ticker.history(period= current_period)

def get_closing_price_list(stock_ticker):
    closing_prices = current_price_dataframe["Close"]
    return closing_prices

def get_date_list(stock_ticker):
    closing_prices = current_price_dataframe["Close"]
    date_array = closing_prices.index.values
    return date_array

def build_chart():
    request_price_dataframe(current_stock)
    price_list = get_closing_price_list(current_stock)
    date_list = get_date_list(current_stock)
    build_chart_image(date_list, price_list)


#plt.tick_params(pad = 30)
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.yticks(np.arange(price_list.min(), price_list.max(), step= 10 ))


def build_chart_image(date_list, price_list):
    plt.clf()
    plt.rcParams["figure.figsize"] = [10, 4.8]
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'xkcd:light grey'
    plt_text_color = 'black'
    plt.rcParams['text.color'] = plt_text_color
    plt.rcParams['axes.labelcolor'] = plt_text_color
    plt.rcParams['xtick.color'] = plt_text_color
    plt.rcParams['ytick.color'] = plt_text_color
    plt.rcParams['axes.formatter.useoffset'] = False
    #plt.yscale('log')
    plt.plot(date_list, price_list)
    plt.title(stock_short_name + ' ' + current_timeframe + ' Price Chart')
    plt.savefig("current_chart.png", bbox_inches = 'tight')
    #plt.show()



#build_chart()
#print(time.ctime())



#calling the following two lines will show you the error message caused by the yFinance headers bug
#There is a potential fix available on the issues tab of the YFinance github's issue page
#After this push, will attempt to integrate this hotfix and begin testing for any errors

#test_stock = yf.Ticker("SPCE")
#stock_info_dict = test_stock.info.get("shortName")
