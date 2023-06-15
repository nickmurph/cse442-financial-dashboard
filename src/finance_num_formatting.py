import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mplcolors
import numpy as np 




msft = yf.Ticker("MSFT")
msft_info_dict = msft.info
msft_beta = msft_info_dict.get("beta")
#print("Microsoft Beta value: " + str(msft_beta))
#print("\n\n\n")

#for x in msft_info_dict:
#  print(x + ": " + str(msft_info_dict[x]))


'''
   5        4         3        2         1
trillion, billion, million, thousand, hundred
15-14-13, 12-11-10,    987,      654,    321
'''
def get_num_digits_of_int(raw_num):
    raw_num = str(raw_num)
    return len(raw_num)

def commify_int_to_string(raw_num):
    raw_num = f"{raw_num:,}"
    return raw_num


#still need to edit in check and handle for negative numbers
def format_financial_number(raw_num):
    num_length = get_num_digits_of_int(raw_num)
    if raw_num < 0:
        print("Cannot use this function on negative numbers YET")
        return raw_num
    if num_length < 4:
        return raw_num
        #raise Exception("Can't use this function on numbers with less than 4 digits!")
    if num_length > 15:
        return "{:e}".format(raw_num)
        #raise Exception("Can't use this function on numbers with more than 15 digits!")
    raw_num = commify_int_to_string(raw_num)
    #print(raw_num)
    num_header = raw_num.split(',')[0]
    num_mod_value = int( (num_length+2)/3 )
    num_decimal = raw_num[len(num_header)+1] 
    num_modifiers = ['Hundred', 'Thousand', 'Million', 'Billion', 'Trillion']
    formatted_num = num_header +"." + num_decimal + " " + num_modifiers[num_mod_value-1]
    #print(formatted_num)
    return formatted_num


msft_mkt_cap = format_financial_number(msft_info_dict.get("marketCap"))
#print(msft_mkt_cap)




'''
These calls, along with the currently commented out print statements in the function, demonstrate the correctness(and incompleteness) of format_financial_number
format_financial_number(-58384935225)
format_financial_number(554)
format_financial_number(5549)
format_financial_number(55495)
format_financial_number(554950)
format_financial_number(5549500)
format_financial_number(55495758)
format_financial_number(554957584)
format_financial_number(5549575840)
format_financial_number(55495758400)
format_financial_number(554957584000)
format_financial_number(5549575840000)
format_financial_number(55495758400000)
format_financial_number(554957584000000)
format_financial_number(5549575840000000)
'''
