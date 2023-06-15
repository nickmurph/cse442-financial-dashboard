import pickle


stock_ticker_file = open('complete_ticker_list.txt', 'r')

list_of_lines = stock_ticker_file.readlines()
list_of_stock_lists = []

for x in range(len(list_of_lines)):
    current_string = list_of_lines[x]
    split_list = current_string.split('|')
    while (len(split_list) > 2):
        split_list.pop()
    list_of_stock_lists.append(split_list)

#print(list_of_stock_lists)
pickled_list_filename = 'pickled_stock_list'
pickled_list = open(pickled_list_filename, 'wb')
pickle.dump(list_of_stock_lists, pickled_list)
pickled_list.close()
