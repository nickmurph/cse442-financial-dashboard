import kivy
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout

import numpy as numpy

# from portfolio_database import db
from portfolio_database import update_to_amount
from portfolio_database import create_dataframe

portfolio_data = create_dataframe()

update_to_amount(portfolio_data,"Microsoft Corporation", "MSFT", 10, 10)
update_to_amount(portfolio_data,"Apple","APPL",10,10)

x = portfolio_data.to_numpy()

class Table(BoxLayout):
    pass

class PortfolioScreen(RecycleView):
    def __init__(self, **kwargs): 
        super(PortfolioScreen, self).__init__(**kwargs) 
        self.data = [{'label1_text': str(x[i][0]), 'label2_text': str(x[i][1]), 'label3_text': str(x[i][2]), 'label4_text': str(x[i][3])} for i in range(len(x))]

class PortfolioGUI(App):
    def build(self):
        self.title = "Portfolio"
        return PortfolioScreen()

if __name__ == "__main__":
    PortfolioGUI().run()