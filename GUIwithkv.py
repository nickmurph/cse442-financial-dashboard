import kivy
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label 
from kivy.factory import Factory
from stocks_and_charts import current_stock
from stocks_and_charts import build_chart
from stocks_and_charts import financials_update
from stocks_and_charts import set_current_stock
from stocks_and_charts import chart_timeframes
from stocks_and_charts import set_current_timeframe
from stocks_and_charts import chart_periods
from stocks_and_charts import set_current_period
from stocks_and_charts import get_stock_name
from stocks_and_charts import get_live_price_first
from stocks_and_charts import get_current_stock
from stocks_and_charts import get_stock_info_dict
from finance_num_formatting import format_financial_number
from stock_list_and_search import search_for_company

from news_links import get_news

import tkinter as tk
from tkinter import messagebox

import webbrowser
import csv

#This allows the window to be resizable by the user
Config.set('graphics', 'resizable', True)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

#Using an instance of Tkinter solely to get the user's screensize, a feature Kivy unfortunately lacks
Tkinter_instance = tk.Tk()
screen_res_width = Tkinter_instance.winfo_screenwidth()
screen_res_height = Tkinter_instance.winfo_screenheight()
Tkinter_instance.withdraw()
#We then use the screen size to help us set the kivy window size (at a ~2/3 ratio for width and height)
Window.size = (screen_res_width/1.5, screen_res_height/1.5)
Window.minimum_height = (screen_res_height/1.5)
Window.minimum_width = (screen_res_width/1.5)

#Should turn the background all white but not working; alternative method in .kv file
#Window.clearcolor = (1, 1 ,1, 1)

username = ""
news_articles = []
current_stock_name = "Microsoft"
news_articles = get_news(current_stock_name)
list_of_ticker_search_results = []
launch_obj = None

def get_window_size():
   return Window.size

def int_or_not(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

class Launch(FloatLayout):
    def testFunction(self):
        print("Executing python code via button is a success")

    def get_window_size_percent_adjusted_width(self, width_fraction):
        return ( Window.size[0] * width_fraction)

    def get_window_size_percent_adjusted_height(self, height_fraction):
        return ( Window.size[1] * height_fraction)

    def buyCallback(self):
        entered_number = self.ids.Purchase.text
        entered_text = self.ids.input_field.text
        global current_stock_name
        if int_or_not(entered_number) == True:
            if entered_text == "":
                current_stock_name = get_stock_name(current_stock.ticker)
                x = "You have successfully purchased " + entered_number + " share(s) of " + current_stock_name
            else:
                current_stock_name = get_stock_name(entered_text)
                x = "You have successfully purchased " + entered_number + " share(s) of " + current_stock_name
        else:
            x = "Please enter a valid integer value."
            return messagebox.showinfo("Error!", x)
        messagebox.showinfo("Successfully Purchased", x)

    def sellCallback(self):
        entered_number = self.ids.Sell.text
        entered_text = self.ids.input_field.text
        global current_stock_name
        if int_or_not(entered_number) == True:
            if entered_text == "":
                current_stock_name = get_stock_name(current_stock.ticker)
                x = "You have successfully sold " + entered_number + " share(s) of " + current_stock_name
            else:
                current_stock_name = get_stock_name(entered_text)
                x = "You have successfully sold " + entered_number + " share(s) of " + current_stock_name
        else:
            x = "Please enter a valid integer value."
            return messagebox.showinfo("Error!", x)
        messagebox.showinfo("Successfully Sold", x)

    def clicked_one_day_button(self):
        set_current_timeframe(chart_timeframes[0])
        set_current_period(chart_periods[0])
        build_chart()
        self.ids.chart_image.reload()

    def clicked_one_month_button(self):
        set_current_timeframe(chart_timeframes[1])
        set_current_period(chart_periods[1])
        build_chart()
        self.ids.chart_image.reload()

    def clicked_six_month_button(self):
        set_current_timeframe(chart_timeframes[2])
        set_current_period(chart_periods[2])
        build_chart()
        self.ids.chart_image.reload()

    def clicked_one_year_button(self):
        set_current_timeframe(chart_timeframes[3])
        set_current_period(chart_periods[3])
        build_chart()
        self.ids.chart_image.reload()

    def clicked_five_year_button(self):
        set_current_timeframe(chart_timeframes[4])
        set_current_period(chart_periods[4])
        build_chart()
        self.ids.chart_image.reload()

    def clicked_max_time_button(self):
        set_current_timeframe(chart_timeframes[5])
        set_current_period(chart_periods[5])
        build_chart()
        self.ids.chart_image.reload()

    def enter_stock_ticker(self):
        entered_text = self.ids.input_field.text
        try:
            set_current_stock(entered_text)
            self.ids.chart_image.reload()
            self.ids.financials_image.reload()
            Launch.update_all_quick_info(self)
            Launch.change_current_stock(self)
            self.ids.input_field.text = ""
        except:
            #Factory.MyPopup().open()
            messagebox.showinfo("Error Occured!", "Error in retrieving this stock's information from YFinance! \n\n Make sure it is a valid stock ticker or try again later.")

    

    def change_current_stock(self):
        entered_text = self.ids.input_field.text
        global current_stock_name
        current_stock_name = get_stock_name(entered_text)
        global news_articles
        news_articles = get_news(current_stock_name)
        Launch.refresh_news(self)

    def change_current_stock_via_RV_search(self, ticker_from_RV_search):
            global current_stock_name
            current_stock_name = get_stock_name(ticker_from_RV_search)
            global news_articles
            news_articles = get_news(current_stock_name)
            Launch.refresh_news(self)

    def refresh_news(self):
        # global news_articles
        # news_articles = get_news(current_stock_name)
        #for i in range(len(news_articles)):
        #   print (i + 1, news_articles[i].title)
        #   print (news_articles[i].url, '\n')
        try:
            self.ids.link0.text = Launch.get_article_title(self, 0)
        except:
            self.ids.link0.text = "No recent news articles found for this stock."
        try:
            self.ids.link1.text = Launch.get_article_title(self, 1)
        except:
            self.ids.link1.text = "No recent news articles found for this stock."
        try:
            self.ids.link2.text = Launch.get_article_title(self, 2)
        except:
            self.ids.link2.text = "No recent news articles found for this stock."


    def get_article_title(self, article_num):
        tempStr = news_articles[article_num].title
        tempStr = tempStr[:100] 
        return tempStr


    def go_to_link0(self):
        try:
            webbrowser.open(news_articles[0].url)
        except:
            messagebox.showinfo("No articles")

    def go_to_link1(self):
        try:
            webbrowser.open(news_articles[1].url)
        except:
            messagebox.showinfo("No articles")

    def go_to_link2(self):
        try:
            webbrowser.open(news_articles[2].url)
        except:
            messagebox.showinfo("No articles")

    # def get_live_price_string(self):
    #    tempStr = "Live Price: "
    #    tempDict = get_stock_info_dict()
    #    livePrice = tempDict.get("regularMarketPrice")
    #    return tempStr + str(livePrice)

    def get_dict_value_as_string(self, labelText, dictKey):
        tempStr = labelText
        tempDict = get_stock_info_dict()
        tempData = tempDict.get(dictKey)
        if tempData is not None and dictKey == "marketCap":
            tempData = format_financial_number(tempData)
        return tempStr + str(tempData)


    def update_all_quick_info(self):
        #print(self)
        self.ids.live_price.text = Launch.get_dict_value_as_string(self, "Live Price: ", "regularMarketPrice")
        self.ids.mkt_cap.text = Launch.get_dict_value_as_string(self, "Market Cap: ", "marketCap")
        self.ids.div_rate.text = Launch.get_dict_value_as_string(self, "Dividend Rate: ", "dividendRate")
        self.ids.fiftytwo_wk_high.text = Launch.get_dict_value_as_string(self, "52 Week High: ", "fiftyTwoWeekHigh")
        self.ids.fiftytwo_wk_low.text = Launch.get_dict_value_as_string(self, "52 WeekLow: ", "fiftyTwoWeekLow")
        self.ids.trailing_pe.text = Launch.get_dict_value_as_string(self, "Trailing P/E: ", "trailingPE")
        self.ids.trailing_eps.text = Launch.get_dict_value_as_string(self, "Trailing EPS: ", "trailingEps")
        self.ids.beta.text = Launch.get_dict_value_as_string(self, "Beta: ", "beta")
        self.ids.earn_growth.text = Launch.get_dict_value_as_string(self, "Earnings Growth: ", "earningsQuarterlyGrowth")
    
    def welcome(self):
        return ("Welcome " + username)

    def logout(self):
        global username
        if username != "":
            username = ""
            App.get_running_app().root.ids.Welcome.text = Launch.welcome(self)
        else:
            invalidLogout()
        
def invalidLogout():
    pop = Popup(title='Invalid Logout', content=Label(text='You are already logged out.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form', content=Label(text='Please fill in all inputs with valid information.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()

def invalidName():
    pop = Popup(title='Invalid Username', content=Label(text='This username already exists.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()

def invalidLogin():
    pop = Popup(title='Invalid Login', content=Label(text='Invalid username or password.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()

def welcomePop(usename):
    pop = Popup(title='Welcome', content=Label(text='Welcome '+ usename + '!'),
                size_hint=(None, None), size=(400, 400))

    pop.open()

class CustomPopup(Popup):
    def login_btn(self, uname, password):
        global username
        csv_file = csv.reader(open('users.csv', "rt"), delimiter=",")
        check = 0
        if uname != "" and password != "":
            for row in csv_file:
                if row[0] == uname and row[2] == password:
                    check = 1
                    welcomePop(uname)
                    CustomPopup.dismiss(self)
                    username = uname
                    App.get_running_app().root.ids.Welcome.text = Launch.welcome(self)
                                                   
        else:
            invalidLogin()

        if check == 0 and uname != "" and password != "":
            invalidLogin()
            

class CreatePopup(Popup):
    def create_login(self, createname, email, createpass):
        csv_file = csv.reader(open('users.csv', "rt"), delimiter=",")
        check = 0
        for row in csv_file:
            if row[0] == createname:
                    check = 1
        if check == 1:
            invalidName()
            return

        if createname != "" and email != "" and email.count("@") == 1 and email.count(".") > 0:
            if createpass != "":
                rowsAppended = []
                rowsAppended.append([createname, email, createpass])
                with open('users.csv', 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(rowsAppended)

                CreatePopup.dismiss(self)               

            else:
                invalidForm()
        else:
            invalidForm()

class CustomizedTextInput(TextInput):
   
   '''
   Leave this commented out. Will eventually be used as part of an autosuggestion feature for the wh bar
    def insert_text(self, substring, from_undo=False):
      #print(Launch.ids.input_field.text)
      if substring.endswith('a') or substring.endswith('A'):
         new_string = substring.upper()
         new_string = 'new_string' + 'APL'
         return super(CustomizedTextInput, self).insert_text(new_string, from_undo=from_undo)
      else:
         return super(CustomizedTextInput, self).insert_text(substring, from_undo=from_undo)
   '''


class TickerSearchPopup(Popup):
    def enter_stock_search_string(self):
        global list_of_ticker_search_results
        entered_text = self.ids.ticker_search.text
        list_of_ticker_search_results = search_for_company(entered_text)  
        self.ids.searched_stocks_rv.update_data(list_of_ticker_search_results)
        #print(list_of_ticker_search_results)


class SearchResultRV(RecycleView):
    def __init__(self, **kwargs): 
        super(SearchResultRV, self).__init__(**kwargs) 
        self.data = []

    def update_data(self, new_data):
        self.data = [{'text': str(x)} for x in new_data]


class SearchRVButton(Button):
    global launch_obj

    def on_press(self):
        try:
            button_text = self.text
            button_text = button_text[2:]
            button_text = button_text.split("'")[0]
            set_current_stock(button_text)
            App.get_running_app().root.ids.chart_image.reload()
            App.get_running_app().root.ids.financials_image.reload()
            launch_obj.change_current_stock_via_RV_search(button_text)
            launch_obj.update_all_quick_info()
            App.get_running_app().root.ids.input_field.text = ""
            self.parent.parent.parent.parent.parent.parent.dismiss()
        except:
            messagebox.showinfo("Error Occured!", "Error in retrieving this stock's information from YFinance! \n\n Not all tickers are part of the YFinance database. Try another!")


class GUIApp(App):
    def build(self):
        global launch_obj
        self.title = 'MnMs Finance Tool'
        launch_obj = Launch()
        return launch_obj


if __name__ == '__main__':
    GUIApp().run()
