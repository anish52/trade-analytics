from utils.banner import *
from utils.sector import *
from utils.cube import *
from utils.vanilla_dataloader import * 
import ipywidgets
import pandas as pd
import pytest

sector_market_share = {'AAPL': ['Electronics Technology', 2455053795328],
     'AMZN': ['Retail Trade', 1167926362112],
     'AZN': ['Healthcare', 208860000000],
     'CVS': ['Healthcare', 129431887872],
     'EA': ['Consumer Durables', 39177392128],
     'META': ['Technology Servies', 532804836352],
     'GOOGL': ['Technology Servies', 1482231906304 ],
     'INTC': ['Electronics Technology', 181184856064],
     'MSFT': ['Technology Servies', 2051480354816],
     'NVDA': ['Electronics Technology', 468770127872],
     'QCOM': ['Electronics Technology', 156531195904],
     'TSLA': ['Consumer Durables', 762865975296],
     'UNH': ['Healthcare', 475756396544],
     'WMT': ['Retail Trade', 356388110336]} 

data_loader = Vanilla_dataloader()

sectors = [i[0] for i in sector_market_share.values() ]
stock_list = list(sector_market_share.keys())
dlist,tilist = data_loader.load_data(stock_list = stock_list)
stock_df = data_loader.percent_change_df(data_list=dlist, sector_market_share=sector_market_share)
    

def test_create_banner():
    a = Banner()
    p = a.create_banner()
    assert isinstance(p, ipywidgets.widgets.widget_string.HTML)

def test_get_sector_cube():
    a = Sector()
    p = a.get_sector(stock_df)
    assert isinstance(p, dict)
    assert all(isinstance(i,str) for i in p.keys())
    assert all(isinstance(i,float) for i in p.values())

def test_cube_factory():
    a = Cube()
    b = Sector()
    x = b.get_sector(stock_df)
    p = a.cube_factory(x)
    assert isinstance(p, ipywidgets.widgets.widget_string.HTML)

#def test_heatmap():

