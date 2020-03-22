import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.textinput import TextInput
from news_links import get_news

import tkinter as tk
#import test3

#This allows the window to be resizable by the user
Config.set('graphics', 'resizable', True)

#Using an instance of Tkinter solely to get the user's screensize, a feature Kivy unfortunately lacks
Tkinter_instance = tk.Tk()
screen_res_width = Tkinter_instance.winfo_screenwidth()
screen_res_height = Tkinter_instance.winfo_screenheight()
#We then use the screen size to help us set the kivy window size (at a ~2/3 ratio for width and height)
Window.size = (screen_res_width/1.5, screen_res_height/1.5)
Window.minimum_height = (screen_res_height/1.5)
Window.minimum_width = (screen_res_width/1.5)

#Should turn the background all white but not working; alternative method in .kv file
#Window.clearcolor = (1, 1 ,1, 1)


class Launch(FloatLayout):
     def testFunction(self):
        print("Executing python code via button is a success")

     def buyCallback(self):
        print('Successfully Purchased Stock')

     def sellCallback(self):
        print('Successfully Sold Stock')
      
     def refresh_news(self):
        get_news('apple')

class TestGUIApp(App):
    def build(self):
        return Launch()

if __name__ == '__main__':
    TestGUIApp().run()


