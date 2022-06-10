'''
Unittests for the prediction module in the dashboard
'''
import pytest
import sys, os
sys.path.insert(0,os.getcwd()+'/../dashboard')
import pandas as pd
import plotly
from dashboard  import prediction

a = prediction.Prediction()

def test_get_prediction():
    p = a.get_prediction()
    assert isinstance(p, pd.DataFrame)

def test_fill_col():
    label1 = 0
    label2 = 5
    assert a.fillcol(label1) == 'rgba(0,250,0,0.4)'
    assert a.fillcol(label2) == 'rgba(0,250,250,0.4)'

def test_plot_pred():
    x = a.get_prediction()
    p = a.plot_pred(x)
    assert isinstance(p, plotly.graph_objs._figurewidget.FigureWidget)
