import kivy
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
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

from news_links import get_news

import tkinter as tk
from tkinter import messagebox

import webbrowser

#This allows the window to be resizable by the user
Config.set('graphics', 'resizable', True)

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

news_articles = []
current_stock_name = "Microsoft"
news_articles = get_news(current_stock_name)

def get_window_size():
   return Window.size

class Launch(FloatLayout):
<<<<<<< HEAD
   def testFunction(self):
      print("Executing python code via button is a success")
   
   def get_window_size_percent_adjusted_width(self, width_fraction):
      return ( Window.size[0] * width_fraction)

   def get_window_size_percent_adjusted_height(self, height_fraction):
      return ( Window.size[1] * height_fraction)

   def buyCallback(self):
      print('Successfully Purchased Stock')

   def sellCallback(self):
      print('Successfully Sold Stock')

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
      self.ids.live_price.text = Launch.get_dict_value_as_string(self, "Live Price: ", "regularMarketPrice")
      self.ids.mkt_cap.text = Launch.get_dict_value_as_string(self, "Market Cap: ", "marketCap")
      self.ids.div_rate.text = Launch.get_dict_value_as_string(self, "Dividend Rate: ", "dividendRate")
      self.ids.fiftytwo_wk_high.text = Launch.get_dict_value_as_string(self, "52 Week High: ", "fiftyTwoWeekHigh")
      self.ids.fiftytwo_wk_low.text = Launch.get_dict_value_as_string(self, "52 WeekLow: ", "fiftyTwoWeekLow")
      self.ids.trailing_pe.text = Launch.get_dict_value_as_string(self, "Trailing P/E: ", "trailingPE")
      self.ids.trailing_eps.text = Launch.get_dict_value_as_string(self, "Trailing EPS: ", "trailingEps")
      self.ids.beta.text = Launch.get_dict_value_as_string(self, "Beta: ", "beta")
      self.ids.earn_growth.text = Launch.get_dict_value_as_string(self, "Earnings Growth: ", "earningsQuarterlyGrowth")

=======
    def testFunction(self):
        print("Executing python code via button is a success")

    def buyCallback(self):
        entered_number = self.ids.Purchase.text
        entered_text = self.ids.input_field.text
        if entered_text == "":
            x = "You have successfully purchased " + entered_number + " shares of " + current_stock.ticker + "!"
        else:
            x = "You have successfully purchased " + entered_number + " shares of " + entered_text + "!" 
        messagebox.showinfo("Successfully Purchased", x)

    def sellCallback(self):
        entered_number = self.ids.Sell.text
        entered_text = self.ids.input_field.text
        if entered_text == "":
            x = "You have successfully sold " + entered_number + " shares of " + current_stock.ticker + "!"
        else:
            x = "You have successfully sold " + entered_number + " shares of " + entered_text + "!" 
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
            
        except:
            # Factory.MyPopup().open()
            messagebox.showinfo(
                "Error Occured!", "Error in retrieving this stock's information from YFinance! \n\n Make sure it is a valid stock ticker or try again later.")
>>>>>>> miren_sprint2

class GUIApp(App):
    def build(self):
        self.title = 'MnMs Finance Tool'
        return Launch()


class CustomizedTextInput(TextInput):
   
   '''
   Leave this commented out. Will eventually be used as part of an autosuggestion feature for the search bar
    def insert_text(self, substring, from_undo=False):
      #print(Launch.ids.input_field.text)
      if substring.endswith('a') or substring.endswith('A'):
         new_string = substring.upper()
         new_string = 'new_string' + 'APL'
         return super(CustomizedTextInput, self).insert_text(new_string, from_undo=from_undo)
      else:
         return super(CustomizedTextInput, self).insert_text(substring, from_undo=from_undo)
   '''

if __name__ == '__main__':
    GUIApp().run()
