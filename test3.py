import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import numpy as np 

msft = yf.Ticker("MSFT")

msft_monthly_prices = msft.history(period="1mo")
#print(type(msft_monthly_prices))
#print(msft_monthly_prices)

msft_closing_prices_1mo = msft_monthly_prices["Close"]
#print(msft_closing_prices_1mo)
print("\n\n\n")
row_length = len(msft_monthly_prices)
col_length = len(msft_monthly_prices.columns)
print(msft_monthly_prices.iat[row_length-1,3])


# Use this function to get the live price when a previous and recent call has not already been made for a dataframe with the daily or monthly price data
# If such a dataframe has already been loaded (eg, msft_monthly_prices above), simply access the latest price in that DF 
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
    #print(stock_price_dataframe.columns[3]) 
    if type(stock_price_dataframe) == type(dummy_DF) and stock_price_dataframe.columns[3] == "Close":
        return stock_price_dataframe.iat[len(stock_price_dataframe)-1,3]
    else:
        return "Error: Argument passed not a valid dataframe containing Closing price data in the third column"
    
        


print(get_live_price(msft_monthly_prices))
today_price_df = msft.history(period='1d')
print(get_live_price(today_price_df))



def get_month_price_list(stock_ticker):
    monthly_prices = stock_ticker.history(period="1mo")
    monthly_closing_prices = monthly_prices["Close"]
    mcp_row_length = len(monthly_closing_prices)
    price_list = []
    for x in range(mcp_row_length):
        price_list.append(monthly_closing_prices.iat[x])
       # print(monthly_closing_prices.iat[x])
    return price_list

'''
nd_array_of_dates = msft_closing_prices_1mo.index.values
print(type(nd_array_of_dates))
print(nd_array_of_dates)
first_date = nd_array_of_dates[0]
print(type(first_date))
print(str(first_date)[:10])
print(str(first_date)[6:10])
'''

print("\n\n\n")
print("\n\n\n")

def get_month_date_list(stock_ticker):
    stock_ticker_monthly_prices = stock_ticker.history(period="1mo")
    stock_ticker_closing_prices_1mo = stock_ticker_monthly_prices["Close"]
    num_of_dates = len(stock_ticker_closing_prices_1mo)
    date_array = stock_ticker_closing_prices_1mo.index.values
    date_array_string = []
    for x in range(num_of_dates):
        date_array_string.append(str(date_array[x])[6:10])
        date_array_string[x] = date_array_string[x].replace("-", "/")
    #print(date_array_string[0])
    #print(date_array_string[num_of_dates-1])
    return date_array_string


msft_1mo_date_list = get_month_date_list(msft)
msft_1mo_price_list = get_month_price_list(msft)



plt.rcParams["figure.figsize"] = [10, 4.8]
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'xkcd:mint green'
plt_text_color = 'black'
plt.rcParams['text.color'] = plt_text_color
plt.rcParams['axes.labelcolor'] = plt_text_color
plt.rcParams['xtick.color'] = plt_text_color
plt.rcParams['ytick.color'] = plt_text_color
plt.plot(msft_1mo_date_list, msft_1mo_price_list, linestyle = 'dashed', marker = '.')
#plt.xlabel('Date')
#plt.ylabel('Price')
plt.title('Microsoft 1-Month Price Chart')
plt.savefig("testchart.png", bbox_inches = 'tight')
plt.show()


'''
def update_live_price(time):
    if time.ctime() - time > 1
=======
import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import numpy as np 

msft = yf.Ticker("MSFT")

msft_monthly_prices = msft.history(period="1mo")
#print(type(msft_monthly_prices))
#print(msft_monthly_prices)

msft_closing_prices_1mo = msft_monthly_prices["Close"]
#print(msft_closing_prices_1mo)
print("\n\n\n")
row_length = len(msft_monthly_prices)
col_length = len(msft_monthly_prices.columns)
print(msft_monthly_prices.iat[row_length-1,3])


# Use this function to get the live price when a previous and recent call has not already been made for a dataframe with the daily or monthly price data
# If such a dataframe has already been loaded (eg, msft_monthly_prices above), simply access the latest price in that DF 
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
    #print(stock_price_dataframe.columns[3]) 
    if type(stock_price_dataframe) == type(dummy_DF) and stock_price_dataframe.columns[3] == "Close":
        return stock_price_dataframe.iat[len(stock_price_dataframe)-1,3]
    else:
        return "Error: Argument passed not a valid dataframe containing Closing price data in the third column"
    
        


print(get_live_price(msft_monthly_prices))
today_price_df = msft.history(period='1d')
print(get_live_price(today_price_df))



def get_month_price_list(stock_ticker):
    monthly_prices = stock_ticker.history(period="1mo")
    monthly_closing_prices = monthly_prices["Close"]
    mcp_row_length = len(monthly_closing_prices)
    price_list = []
    for x in range(mcp_row_length):
        price_list.append(monthly_closing_prices.iat[x])
       # print(monthly_closing_prices.iat[x])
    return price_list

'''
nd_array_of_dates = msft_closing_prices_1mo.index.values
print(type(nd_array_of_dates))
print(nd_array_of_dates)
first_date = nd_array_of_dates[0]
print(type(first_date))
print(str(first_date)[:10])
print(str(first_date)[6:10])
'''

print("\n\n\n")
print("\n\n\n")

def get_month_date_list(stock_ticker):
    stock_ticker_monthly_prices = stock_ticker.history(period="1mo")
    stock_ticker_closing_prices_1mo = stock_ticker_monthly_prices["Close"]
    num_of_dates = len(stock_ticker_closing_prices_1mo)
    date_array = stock_ticker_closing_prices_1mo.index.values
    date_array_string = []
    for x in range(num_of_dates):
        date_array_string.append(str(date_array[x])[6:10])
        date_array_string[x] = date_array_string[x].replace("-", "/")
    #print(date_array_string[0])
    #print(date_array_string[num_of_dates-1])
    return date_array_string


msft_1mo_date_list = get_month_date_list(msft)
msft_1mo_price_list = get_month_price_list(msft)



plt.rcParams["figure.figsize"] = [10, 4.8]
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'xkcd:mint green'
plt_text_color = 'black'
plt.rcParams['text.color'] = plt_text_color
plt.rcParams['axes.labelcolor'] = plt_text_color
plt.rcParams['xtick.color'] = plt_text_color
plt.rcParams['ytick.color'] = plt_text_color
plt.plot(msft_1mo_date_list, msft_1mo_price_list, linestyle = 'dashed', marker = '.')
#plt.xlabel('Date')
#plt.ylabel('Price')
plt.title('Microsoft 1-Month Price Chart')
plt.savefig("testchart.png", bbox_inches = 'tight')
plt.show()


'''
def update_live_price(time):
    if time.ctime() - time > 1
'''