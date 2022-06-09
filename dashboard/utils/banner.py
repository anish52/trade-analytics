import requests
from bs4 import BeautifulSoup
import ipywidgets as ipw

class Banner:
    def __init__(self):
        pass

    def get_performance(self):
        page  = requests.get("https://www.fool.com/investing/top-stocks-to-buy.aspx")
        soup = BeautifulSoup(page.content, 'html.parser')
        stocks = soup.find(class_='related-tickers')
        stock_picks = stocks.find_all(class_='ticker-text-wrap')
        stock_names = []
        for stock in stock_picks:
            stock_names.append(stock.h3.get_text())
        stock_names
        stock_symbol = []
        for stock in stock_picks:
            stock_symbol.append(stock.a.span.get_text())

        stock_symbol
        price_change = stocks.find_all(class_='price-change-amount')
        # Get Change Price
        percent_change = stocks.find_all(class_='price-change-percent')
        # Get Change Percent
        change_pct = []
        for pct in percent_change:
            price = pct.get_text()
            change_pct.append(price.strip())
        change_pct
        dic = {}
        for i in range(len(change_pct)):
            dic[stock_symbol[i]] = change_pct[i]
        return dic

    def create_banner(self):
        '''
        Function to create moving banner displayed at the top of the dashboard
        Param: stock_list (defualt)
        Return: panel.pane.markup.HTML
        '''
        stocks = self.get_performance()
        html_string = ""
        for key in stocks:
            performance = stocks[key]
            performance = performance.replace('(',"")
            performance = performance.replace(')',"")
            performance = performance.replace('%',"")
            if float(performance) >= 0:
                temp = '&nbsp &nbsp &nbsp <FONT COLOR = "WHITE"> <b>'+ key + '</b>' + ': <FONT COLOR = "GREEN">' + performance + '% </b>'
                html_string+=temp
            else:
                temp = '&nbsp &nbsp &nbsp <FONT COLOR = "WHITE"> <b>'+ key + '</b>' + ': <FONT COLOR = "RED">' + performance + '% </b>'
                html_string+=temp

    #     style_str = "<html><head><style>.code-style {'background-color': '#454545', 'border': '2px solid white','border-radius': '5px', 'padding': '10px'} </style></head>"
        return ipw.HTML('<marquee onmouseover="this.stop();" onmouseout="this.start();" width=1375 bgcolor="#000000", "border": "2px solid white","border-radius": "5px", "padding": "10px">' + html_string +  '</marquee>')


if __name__ == '__main__':
    a = Banner()
    b = a.create_banner()
    print(b)
