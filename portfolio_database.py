import pandas as pd
import numpy as numpy
import pickle

# user = "ming"

def create_dataframe(user):
    db = pd.DataFrame({
        "Stock Name" : [],
        "Stock Ticker": [],
        "Amount of Shares": [],
        "Market Value": []
    })
    db.to_pickle("./portfolio_dataframe_" + user + ".pkl")
    unpickled_db = pd.read_pickle("./portfolio_dataframe_" + user + ".pkl")
    return unpickled_db

# x = create_dataframe(user)
# x = pd.read_pickle("./portfolio_dataframe_" + user + ".pkl")

def add_to_database(user,db,sn,st,a,mv):
    db.loc[len(db.index)] = [sn,st,a,mv]
    db.to_pickle("./portfolio_dataframe_" + user + ".pkl")

def update_to_amount(user,db,sn,st,a,mv):
    if(st in db.values):
        x = db.loc[db["Stock Ticker"] == st, "Amount of Shares"]
        db.loc[db["Stock Ticker"] == st, "Amount of Shares"] = x + a
        db.drop(db[db['Amount of Shares'] <= 0].index, inplace = True)
        db.loc[db["Stock Ticker"] == st, "Market Value"] = mv
        db.to_pickle("./portfolio_dataframe_" + user + ".pkl")
        print(db)
    else:
        if(a > 0):
            add_to_database(user,db,sn,st,a,mv)
            print(db)

# update_to_amount(user,x,"Microsoft","MSFT",10,10)
# update_to_amount(user,x,"Apple","APPL",10,10)
# update_to_amount(user,x,"Microsoft","MSFT",0,20)
# update_to_amount(user,x,"Apple","APPL",-10,10)
# update_to_amount(user,x,"Apple","APPL",10,10)
# update_to_amount(user,x,"Microsoft", "MSFT", -10, 30)

# unpickled_db = pd.read_pickle("./portfolio_dataframe_" + user + ".pkl")
# print(unpickled_db)

def get_dataframe_to_numpy(user,db):
    unpickled_db = pd.read_pickle("./portfolio_dataframe_" + user + ".pkl")
    return unpickled_db.to_numpy()

# npy = get_dataframe_to_numpy(user,unpickled_db)
# print(npy)
