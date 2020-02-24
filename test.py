
import kivy
import kivy_deps
import matplotlib
import numpy
import pandas
import requests
import time
import yfinance as yf



print("\n\n\n\n")
print(time.ctime())
print("Assigning ticker for MSFT")
msft = yf.Ticker("MSFT")
print("\n")

print(time.ctime())
print("Retrieving data for max")
msft.history(period="max"   )
print("\n")

print(time.ctime())
print("Retrieving data for 1 month")
msft.history(period="1mo")
print("\n")

print(time.ctime())
print("Retrieving data for 1 day")
msft.history(period="1d")
print("\n")

print(time.ctime())

print("\n\n")
print (msft.history(period="1d", interval="1m"))
print(time.ctime())


print(time.ctime())
print("Retrieving data for max")
print("")
msft_max_price_history = msft.history(period="max")
num_max_price_entries = len(msft_max_price_history)
print(msft_max_price_history.iat[num_max_price_entries-1, 3])



print("\n")
print(time.ctime())

'''
Ran test at 1:23 AM Tuesday morning 2/18/2020
First ctime print 1:22:48
last ctime print 1:22:48


if these retrieval times hold during busier hours tomorrow, will not need to worry about time cost of API calls multiple times in test3.py functions



Ran test at 2:55 PM Tuesday afternoon 2/18/2020
First ctime print 14:54:50
Last ctime print 14:54:52
'''
