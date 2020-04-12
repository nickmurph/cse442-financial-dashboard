import kivy
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.factory import Factory
from stocks_and_charts import current_stock
from stocks_and_charts import build_chart
from stocks_and_charts import financials_update
from stocks_and_charts import set_current_stock
from stocks_and_charts import chart_timeframes
from stocks_and_charts import set_current_timeframe
from stocks_and_charts import chart_periods
from stocks_and_charts import set_current_period
import tkinter as tk
from tkinter import messagebox

# This allows the window to be resizable by the user
Config.set('graphics', 'resizable', True)

# Using an instance of Tkinter solely to get the user's screensize, a feature Kivy unfortunately lacks
Tkinter_instance = tk.Tk()
screen_res_width = Tkinter_instance.winfo_screenwidth()
screen_res_height = Tkinter_instance.winfo_screenheight()
Tkinter_instance.withdraw()
# We then use the screen size to help us set the kivy window size (at a ~2/3 ratio for width and height)
Window.size = (screen_res_width/1.5, screen_res_height/1.5)
Window.minimum_height = (screen_res_height/1.5)
Window.minimum_width = (screen_res_width/1.5)

# Should turn the background all white but not working; alternative method in .kv file
#Window.clearcolor = (1, 1, 1, 1)

class Launch(FloatLayout):
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
            self.ids.financial_image.reload()
            
        except:
            # Factory.MyPopup().open()
            messagebox.showinfo(
                "Error Occured!", "Error in retrieving this stock's information from YFinance! \n\n Make sure it is a valid stock ticker or try again later.")

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
    #DataFrameApp().run()
    GUIApp().run()
