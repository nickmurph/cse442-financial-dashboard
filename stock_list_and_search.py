import pickle

pickled_list_filename = 'pickled_stock_list'
imported_pickled_stock_list = open(pickled_list_filename, 'rb')
new_list_of_stock_lists = pickle.load(imported_pickled_stock_list)
imported_pickled_stock_list.close()

#searches all the companies in the list of lists at position [x], looking for a partial string match with the ticker at [x][0] or name at [x][1]

# Note that some companies have official corporate names different from a more well-known past name or popular moniker (eg, Google is not the name
# of the corporation, it's Alphabet, Incorporated. Since the stock ticker is GOOGL, searching "Google" will not return any valid results. A simple 
# if statement can be added for "Google" in light of it's popularity, but hardcoding exceptions for an insignificant portion of the >8000 stocks in 
# the list is not feasible.)

def search_for_company(search_string):
    search_string = search_string.casefold()
    list_of_matches = []

    for x in range(len(new_list_of_stock_lists)):
        lowercase_ticker_compare = new_list_of_stock_lists[x][0].casefold()
        lowercase_company_compare = new_list_of_stock_lists[x][1].casefold()
        if search_string in lowercase_ticker_compare or search_string in lowercase_company_compare:
            list_of_matches.append(new_list_of_stock_lists[x])
    
    if len(list_of_matches) == 0:
        return ["No matches found!"]
    else:
        return(list_of_matches)
