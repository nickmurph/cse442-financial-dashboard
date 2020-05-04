import csv
import pickle

def creating_watchlist_db():
    username_file = open('users.csv','r')
    reader = csv.reader(username_file)
    watch_list_dictionary = {}
    for row in reader:
        watch_list_dictionary[row[0]] = [""]
    return watch_list_dictionary

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

dictionary = creating_watchlist_db()
pickling_init_dump(dictionary)