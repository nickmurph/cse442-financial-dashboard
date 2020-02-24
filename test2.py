import pandas
import time
import requests
import yfinance as yf


print(time.ctime())
msft = yf.Ticker("MSFT")
aapl = yf.Ticker("AAPL")
tsla = yf.Ticker("TSLA")
intc = yf.Ticker("INTC")
#print(msft)

#msft.info
#msft.history(period="max")
#msft.actions
#msft.history(period="1mo")
#print (msft.history(period="max"))

print(time.ctime())
#print (msft.history(period="1d"))
print(time.ctime())
#time.sleep(60)
#print(msft.cashflow)
print(time.ctime())
print("\n \n Balance Sheet for Microsoft \n")
print(msft.balance_sheet)
print(time.ctime())

'''
print(time.ctime())
print("\n \n Balance Sheet for Apple \n")
print(aapl.balance_sheet)
print(time.ctime())


print(time.ctime())
print("\n \n Balance Sheet for Tesla \n")
print(tsla.balance_sheet)
print(time.ctime())


print(time.ctime())
print("\n \n Balance Sheet for Intel \n")
print(intc.balance_sheet)
print(time.ctime())
'''

print( "\n \n \n")
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print( "\n \n \n")
print(time.ctime())
print (msft.history(period="1mo"))








=======
import pandas
import time
import requests
import yfinance as yf


print(time.ctime())
msft = yf.Ticker("MSFT")
aapl = yf.Ticker("AAPL")
tsla = yf.Ticker("TSLA")
intc = yf.Ticker("INTC")
#print(msft)

#msft.info
#msft.history(period="max")
#msft.actions
#msft.history(period="1mo")
#print (msft.history(period="max"))

print(time.ctime())
#print (msft.history(period="1d"))
print(time.ctime())
#time.sleep(60)
#print(msft.cashflow)
print(time.ctime())
print("\n \n Balance Sheet for Microsoft \n")
print(msft.balance_sheet)
print(time.ctime())

'''
print(time.ctime())
print("\n \n Balance Sheet for Apple \n")
print(aapl.balance_sheet)
print(time.ctime())


print(time.ctime())
print("\n \n Balance Sheet for Tesla \n")
print(tsla.balance_sheet)
print(time.ctime())


print(time.ctime())
print("\n \n Balance Sheet for Intel \n")
print(intc.balance_sheet)
print(time.ctime())
'''

print( "\n \n \n")
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print (msft.history(period="1d"))
time.sleep(30)
print( "\n \n \n")
print(time.ctime())
print (msft.history(period="1mo"))









