import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import numpy as np 
import unittest
from pandas.plotting import register_matplotlib_converters
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
from stocks_and_charts import set_current_period
from stocks_and_charts import set_current_stock
from stocks_and_charts import set_current_timeframe
from stocks_and_charts import get_live_price_first
from stocks_and_charts import get_closing_price_list
from stocks_and_charts import get_date_list
from stocks_and_charts import chart_periods
from stocks_and_charts import chart_timeframes


test_stock = yf.Ticker("TSLA")
test_stock_dict = test_stock.info
set_current_stock("TSLA")
from stocks_and_charts import current_stock
from stocks_and_charts import stock_info_dict
from stocks_and_charts import stock_short_name


def test_set_current_stock_isin():
    assert test_stock.isin == current_stock.isin     
    #check that both objects have the same International Securities Identification Number
    #this ensures set_current_stock correctly set the value of the current_stock variable in stocks_and_charts


def test_set_current_stock_info():
    assert set(stock_info_dict.keys()) == set(test_stock_dict.keys()) 
    #check that both objects have the same info dictionary
    #this ensures set_current_stock correctly set the value of the stock_info_dict variable in stocks_and_charts
    
    
def test_set_current_stock_name():
    assert stock_short_name == test_stock.info.get("shortName")
    #check that both objects have the same company name
    #this ensures set_current_stock correctly set the value of the stock_short_name variable in stocks_and_charts



def test_set_current_period():
    #valid chart periods are: '1d','1mo','6mo','1y','5y','max', as contained in the chart_periods list
    #these assignment tests ensure the set_current_period function properly changes the value of the current_period variable
    set_current_period(chart_periods[0])
    from stocks_and_charts import current_period
    assert current_period == '1d'

    set_current_period(chart_periods[1])
    from stocks_and_charts import current_period
    assert current_period == '1mo'

    set_current_period(chart_periods[2])
    from stocks_and_charts import current_period
    assert current_period == '6mo'

    set_current_period(chart_periods[3])
    from stocks_and_charts import current_period
    assert current_period == '1y'

    set_current_period(chart_periods[4])
    from stocks_and_charts import current_period
    assert current_period == '5y'

    set_current_period(chart_periods[5])
    from stocks_and_charts import current_period
    assert current_period == 'max'


def test_set_current_timeframe():
    #valid chart timeframes are: '1-Day', '1-Month', '6-Month', '1-Year', '5-Year', 'Max Length', 
    #these assignment tests ensure the set_current_timeframe function properly changes the value of the current_timeframe variable
    set_current_timeframe(chart_timeframes[0])
    from stocks_and_charts import current_timeframe
    assert current_timeframe == '1-Day'

    set_current_timeframe(chart_timeframes[1])
    from stocks_and_charts import current_timeframe
    assert current_timeframe == '1-Month'

    set_current_timeframe(chart_timeframes[2])
    from stocks_and_charts import current_timeframe
    assert current_timeframe == '6-Month'

    set_current_timeframe(chart_timeframes[3])
    from stocks_and_charts import current_timeframe
    assert current_timeframe == '1-Year'

    set_current_timeframe(chart_timeframes[4])
    from stocks_and_charts import current_timeframe
    assert current_timeframe == '5-Year'

    set_current_timeframe(chart_timeframes[5])
    from stocks_and_charts import current_timeframe
    assert current_timeframe == 'Max Length'



test_live_price = test_stock.history(period="1d", interval="1m").iat[0,3]

def test_get_live_price_first():
    assert test_live_price == get_live_price_first(current_stock)



if __name__ == "__main__":
    test_set_current_stock_isin()
    test_set_current_stock_info()
    test_set_current_stock_name()
    print("All tests for set_current_stock passed")
    test_set_current_period()
    print("Test for set_current_period passed")
    test_set_current_timeframe()
    print("Test for set_current_timeframe passed")
    test_get_live_price_first
    print("Test for get_live_price_first passed")