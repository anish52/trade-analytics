import sys, os, pickle
sys.path.insert(0,os.getcwd()+'/../dashboard')
sys.path.insert(0,os.getcwd()+'/../dashboard/utils')
import pytest
from dashboard import widgets
from dashboard.utils import vanilla_dataloader
import ipywidgets as ipw

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

stock_list = list(sector_market_share.keys())
time_intervals = ['1d', '30m', '5m']

cur_stock = stock_list[0]
cur_interval = time_intervals[0]

data_loader = vanilla_dataloader.Vanilla_dataloader()

data_list, ti_list = data_loader.load_data(stock_list)
df = data_loader.percent_change_df(data_list, sector_market_share)


with open (os.getcwd()+'/../dashboard/output/cache.pkl','rb') as f:
    d = pickle.load(f)

data_list, ti_list = d['data_list'], d['ti_list']
df = d['df']
pred_df = d['pred_df']

a = widgets.Widgets()

def test_stock_price_widget():
    stock_price_widget = a.stock_price_plot_factory(stock_list, data_list[0])
    assert isinstance(stock_price_widget, ipw.Widget), "stock_price widget has an issue!"

def test_ti_widget():
    ti_widget = a.ti_plot_factory(data_list, ti_list, time_intervals, stock_list, cur_stock, cur_interval)
    assert isinstance(ti_widget, ipw.Widget), "tech_indicator has an issue!"

def test_heatmap_widget():
    heatmap_widget = a.get_heatmap_widget(parent_path=os.getcwd()+'/../dashboard/output/')
    assert isinstance(heatmap_widget, ipw.Widget), "heatmap"

def test_banner_widget():
    banner_widget = a.get_banner_widget()
    assert isinstance(banner_widget, ipw.Widget), "banner"

def test_index_stats_widget():
    index_stats_widget = a.get_index_stats_widget(sector_market_share, df)
    assert isinstance(index_stats_widget, ipw.Widget), "index_stats"

def test_sector_wise_widget():
    sector_wise_widget = a.get_sector_wise_widget(df)
    assert isinstance(sector_wise_widget, ipw.Widget), "sectors"

def test_cube_widget():
    cube_widget = a.get_cube_widget(df)
    assert isinstance(cube_widget, ipw.Widget), "cube"
