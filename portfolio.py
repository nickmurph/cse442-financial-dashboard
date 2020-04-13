import kivy
from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout

stocks = [{'R1': 'Stock Ticker', 'R2': 'Amount', 'R3': 'Current Price', 'R4': 'Total Price'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'TSLA', 'R2': '10', 'R3': '573', 'R4': '5730'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'TSLA', 'R2': '10', 'R3': '573', 'R4': '5730'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'TSLA', 'R2': '10', 'R3': '573', 'R4': '5730'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'TSLA', 'R2': '10', 'R3': '573', 'R4': '5730'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'},
         {'R1': 'AAPL', 'R2': '10', 'R3': '267', 'R4': '2670'},
         {'R1': 'MSFT', 'R2': '50', 'R3': '165', 'R4': '8250'}
         ]

class Table(BoxLayout):
    pass

class PortfolioScreen(RecycleView):
    def __init__(self, **kwargs): 
        super(PortfolioScreen, self).__init__(**kwargs) 
        self.data = [{'label1_text': str(x['R1']), 'label2_text': str(x['R2']), 'label3_text': str(x['R3']), 'label4_text': str(x['R4'])} for x in stocks]

class PortfolioGUI(App):
    def build(self):
        self.title = "Portfolio"
        return PortfolioScreen()

if __name__ == "__main__":
    PortfolioGUI().run()