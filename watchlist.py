import csv
from stocks_and_charts import get_stock_name
import pickle



def pickling_init_dump(dictionary):
    pickled_list_filename = 'pickled_watch_list'
    pickled_list = open(pickled_list_filename, 'wb')
    pickle.dump(dictionary, pickled_list)
    pickled_list.close()

def pickling_init_load(dictionary):
    pickled_list_filename = 'pickled_watch_list'
    pickled_list = open(pickled_list_filename, 'rb')
    dictionary = pickle.load(pickled_list)
    pickled_list.close()


pickle_file = open('pickled_watch_list', 'rb')
dictionary = pickle.load(pickle_file)

def add_to_watchlist(dictionary, username, desired_stock):
    for (key, value) in dictionary.items():
        if username == key:
            for i in value:
                if i != desired_stock:
                    value.append(desired_stock)
                    value = list(dict.fromkeys(value))
    return dictionary

updated_dictionary = add_to_watchlist(dictionary, "miren", "MSFT")
updated_dictionary = add_to_watchlist(dictionary, "abcdef", "MSFT")



pickling_init_load(dictionary)
pickling_init_dump(updated_dictionary)

def getting_watch_list(username, updated_dictionary):
    for key, value in updated_dictionary.items(): 
        if key == username:
            value = value[1:]
            value = list(dict.fromkeys(value))
            value = sorted(value)
            return value

def get_full_name(username, updated_dictionary):
    global get_stock_name
    array = getting_watch_list(username, updated_dictionary)
    full_array = []
    for i in array:
        x = get_stock_name(i)
        y = i + ": " + x
        full_array.append(y)
        
    return full_array