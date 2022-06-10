from banner import *
from index_performance import * 
from vanilla_dataloader import *
from heatmap import *
import pandas as pd
import pytest


data_loader = Vanilla_dataloader()

sector_market_share = {'AAPL': ['Electronics Technology', 2455053795328],
'AMZN': ['Retail Trade', 1167926362112],
'AZN': ['Healthcare', 208860000000],
'CVS': ['Healthcare', 129431887872],
'EA': ['Consumer Durables', 39177392128],
'META': ['Technology Servies', 542804836352],
'GOOGL': ['Technology Servies', 1482231906304 ],
'INTC': ['Electronics Technology', 181184856064],
'MSFT': ['Technology Servies', 2051480354816],
'NVDA': ['Electronics Technology', 468770127872],
'QCOM': ['Electronics Technology', 156531195904],
'TSLA': ['Consumer Durables', 762865975296],
'UNH': ['Healthcare', 475756396544],
'WMT': ['Retail Trade', 356388110336]} 

#def test_stock_metrics():
    #dframe, stockList = stock_metrics()
    #assert list(dframe.columns) == ['sector', 'regularMarketOpen', 'regularMarketPrice', 'prev_close', 'curr_close', 'market_cap', 'percentage_change']
    #assert isinstance(stockList, list)
    #assert dframe.index.name == 'stock'
    #assert dframe['prev_close'].dtype == 'float64'
    #assert dframe['curr_close'].dtype == 'float64'
    #assert dframe['market_cap'].dtype == 'int64'
    #assert dframe['percentage_change'].dtype == 'float64'
    #assert dframe['regularMarketOpen'].dtype == 'float64'
    #assert dframe['regularMarketPrice'].dtype == 'float64'
def test_load_data():
    stock_list = list(sector_market_share.keys())
    dlist, tilist = data_loader.load_data(stock_list = stock_list)
    assert isinstance(dlist, list)
    assert isinstance(tilist, list)
    assert isinstance(dlist[0], pd.core.frame.DataFrame)
    assert isinstance(tilist[0], pd.core.frame.DataFrame)

def test_percent_change_df():
    sectors = [i[0] for i in sector_market_share.values() ]
    stock_list = list(sector_market_share.keys())
    dlist,tilist = data_loader.load_data(stock_list = stock_list)
    dframe = data_loader.percent_change_df(data_list=dlist, sector_market_share=sector_market_share)
    assert isinstance(dframe, pd.core.frame.DataFrame)
    assert dframe['percent_change'].dtype == 'float64' 
    assert dframe['market_share'].dtype == 'int64'
    assert set(dframe['sector'].unique()) == set(sectors)

def test_get_index_performance():
    a = Index_performance()
    symbol = 'AAPL'
    p = a.get_index_performance(symbol)
    assert isinstance(p, tuple)
    assert isinstance(p[0], float)
    assert isinstance(p[1], float)
    assert p[2] == symbol

def test_get_performance():
    a = Banner()
    p = a.get_performance()
    assert isinstance(p, dict)
    assert all(isinstance(i,str) for i in p.keys())
    assert all(isinstance(i,str) for i in p.values())
    assert all(i[-3].isdigit() for i in p.values())





