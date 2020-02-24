import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
from kivy.config import Config 
import kivy as kv 
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button  
from kivy.core.window import Window
from kivy.uix.image import Image
import tkinter as tk


#Using an instance of Tkinter solely to get the screensize, a feature Kivy lacks
#We then use the screen size to help us set the kivy window size (at a ~2/3 ratio for width and height)
Tkinter_instance = tk.Tk()
screen_res_width = Tkinter_instance.winfo_screenwidth()
screen_res_height = Tkinter_instance.winfo_screenheight()

Config.set('graphics', 'resizable', True)  
Window.size = (screen_res_width/1.5, screen_res_height/1.5)
#Window.maximize()


class GUITestApp(App):
    
    def build(self):
        Float_Test = FloatLayout()

        #test_button = Button(text= "TESTING", size_hint=(.6,.32), pos =(25,75))
        #Float_Test.add_widget(test_button)

        test_image = Image(source = 'testchart.png', pos =(25,75))
        Float_Test.add_widget(test_image)

        return Float_Test

if __name__ == "__main__":
    GUITestApp().run()

=======
import pandas as pd
import time
import requests
import yfinance as yf
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np 
from kivy.config import Config 
import kivy as kv 
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button  
from kivy.core.window import Window
from kivy.uix.image import Image
import tkinter as tk


#Using an instance of Tkinter solely to get the screensize, a feature Kivy lacks
#We then use the screen size to help us set the kivy window size (at a ~2/3 ratio for width and height)
Tkinter_instance = tk.Tk()
screen_res_width = Tkinter_instance.winfo_screenwidth()
screen_res_height = Tkinter_instance.winfo_screenheight()

Config.set('graphics', 'resizable', True)  
Window.size = (screen_res_width/1.5, screen_res_height/1.5)
#Window.maximize()


class GUITestApp(App):
    
    def build(self):
        Float_Test = FloatLayout()

        #test_button = Button(text= "TESTING", size_hint=(.6,.32), pos =(25,75))
        #Float_Test.add_widget(test_button)

        test_image = Image(source = 'testchart.png', pos =(25,75))
        Float_Test.add_widget(test_image)

        return Float_Test

if __name__ == "__main__":
    GUITestApp().run()

