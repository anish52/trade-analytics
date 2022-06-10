from datetime import datetime
from typing import Dict, List
import json
import numpy as np
from utils.vanilla_dataloader import Vanilla_dataloader
from utils.heatmap import Heatmap
from utils.banner import Banner
from utils.index_performance import Index_performance
from utils.sector import Sector
from utils.cube import Cube
import concurrent.futures

import ipyvuetify as v
import ipywidgets as ipw
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from PIL import Image
import panel as pn
from ipywidgets import Layout


v.theme.dark = True
plt.style.use('dark_background')

class Widgets(object):
    """docstring for widgets"""
    def __init__(self, arg=None):
        super(Widgets, self).__init__()
        self.banner = Banner()
        self.sector = Sector()
        self.cube = Cube()
        self.index_performance = Index_performance()
        self.arg = arg
        

    def get_banner_widget(self):
        banner = self.banner.create_banner()
        return banner


    def stock_price_plot_factory(self, stock_list, data_daily):
        '''
        data_daily: DataFrame on different stocks on daily-interval
        '''
        fig = go.Figure()
        for stock in stock_list:
            fig.add_trace(
                go.Scatter(
                    x=data_daily.index,
                    y=data_daily[stock]['Close'],
                    mode='lines',
                    fill='tozeroy',
                    hovertemplate = 'Stock: {}'.format(stock) + '<br>Date: %{x} </br>Price: %{y:$.2f}<extra></extra>',
                )
            )

        fig.update_xaxes(
            title_text = 'Date',
            color='white',
            showgrid=False,
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
                    dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
                    dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
                    dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
                    dict(step = 'all')])),
            rangeselector_activecolor='green',
            rangeselector_bgcolor='rgb(179,226,205)')

        fig.update_yaxes(title_text = 'Share Price', tickprefix = '$', color='white', showgrid=False)

        buttons_list = []
        buttons_list.append(
                    dict(label="All",
                         method="update",
                         args=[{"visible": [True] * len(stock_list)},
                               {"title": "Daily Share Price"}])
            )

        for ind, stock in enumerate(stock_list):
            visible_list = [False] * len(stock_list)
            visible_list[ind] = True
            buttons_list.append(
                        dict(label=stock,
                             method="update",
                             args=[{"visible": visible_list},
                                   {"title": '{} Daily Share Price'.format(stock)}])
            )

        fig.update_layout(
            showlegend = False,
            updatemenus=[
                dict(
                    active=0,
                    buttons=buttons_list,
                    bgcolor='rgb(179,226,205)',
                    x=-.15
                ),
            ],
            paper_bgcolor='rgba(0,0,0,0.16)',#'rgba(37,37,37,1)',
            plot_bgcolor='rgba(0,0,0,0.16)',#'rgba(37,37,37,1)',
            font_color='gray',
            title_font_color='white',
            title_font_size=22,
            title_font_family='Droid Serif',
            title = {'text':'DAILY SHARE PRICE',
                     'y':0.95,
                     'x':0.025,
                     'xanchor': 'left',
                     'yanchor': 'top'
                    },
            hovermode='x unified'
        )
        layout = go.Layout(height=700, width=1000)
        return go.FigureWidget(fig, layout)


    def ti_plot_factory(self, data_list, ti_list, time_intervals=['1d', '30m', '5m'],\
        stock_list=['AAPL', 'NVDA', 'INTC', 'QCOM', 'MSFT', 'GOOGL', 'META', 'AMZN', 'WMT', 'TSLA', 'EA', 'UNH', 'AZN', 'CVS'],\
        curr_interval='1d', cur_stock='AAPL'):
        '''
        data_list: list of DataFrame on different intervals
        ti_list: list of DataFrame on techinical indicator objects on different intervals
        '''
        
        fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.01, row_heights=[0.5,0.1,0.2,0.2])

        for time_idx, interval in enumerate(time_intervals):
            data = data_list[time_idx]
            ti   = ti_list[time_idx]
            for ind, stock in enumerate(stock_list):
                visible_default = True if ind==0 and time_idx == 0 else False  # when plot first starts, only show first stock

                # Candlestick
                candle = go.Candlestick(x=data.index,
                                  open=data[stock]['Open'],
                                  high=data[stock]['High'],
                                  low=data[stock]['Low'],
                                  close=data[stock]['Close'],
                                  showlegend=False,
                                  visible=visible_default, name="candle_"+interval+"_"+stock)
                fig.add_trace(candle, row=1, col=1)

                # MA 5
                ma5 = go.Scatter(x=data.index, 
                               y=data[stock]['MA5'], 
                               opacity=0.7, 
                               line=dict(color='blue', width=2), 
                               name='MA 5'+interval+"_"+stock,
                               visible=visible_default)
                fig.add_trace(ma5, row=1, col=1)
                
                # MA 20
                ma20 = go.Scatter(x=data.index, 
                               y=data[stock]['MA20'], 
                               opacity=0.7, 
                               line=dict(color='orange', width=2), 
                               name='MA 20'+interval+"_"+stock,
                               visible=visible_default)
                fig.add_trace(ma20, row=1, col=1)


                # Volume
                colors = ['green' if row[stock]['Open'] - row[stock]['Close'] >= 0 
                          else 'red' for index, row in data.iterrows()]
                volume = go.Bar(x=data.index, 
                               y=data[stock]['Volume'],
                               marker_color=colors,
                               visible=visible_default, name=interval+"_"+stock)
                fig.add_trace(volume, row=2, col=1)

                # MACD 
                colors = ['green' if val >= 0 
                          else 'red' for val in ti.loc['MACD', stock].macd_diff()]
                macd_diff = go.Bar(x=data.index, 
                           y=ti.loc['MACD', stock].macd_diff(),
                           marker_color=colors,
                           visible=visible_default, name=interval+"_"+stock)
                fig.add_trace(macd_diff, row=3, col=1)

                macd = go.Scatter(x=data.index, 
                                   y=ti.loc['MACD', stock].macd(),
                                   line=dict(color='darkgoldenrod', width=2),
                                   visible=visible_default, name=interval+"_"+stock)
                fig.add_trace(macd, row=3, col=1)

                macd_sig = go.Scatter(x=data.index, 
                                   y=ti.loc['MACD', stock].macd_signal(),
                                   line=dict(color='blue', width=1),
                                   visible=visible_default, name=interval+"_"+stock)
                fig.add_trace(macd_sig, row=3, col=1)

                # STOCH
                stoch = go.Scatter(x=data.index, 
                                   y=ti.loc['STOCH', stock].stoch(),
                                   line=dict(color='darkgoldenrod', width=2),
                                   visible=visible_default, name=interval+"_"+stock)
                fig.add_trace(stoch, row=4, col=1)

                stoch_sig = go.Scatter(x=data.index, 
                                   y=ti.loc['STOCH', stock].stoch_signal(),
                                   line=dict(color='blue', width=1),
                                   visible=visible_default, name=interval+"_"+stock)
                fig.add_trace(stoch_sig, row=4, col=1)

        # colors and labels
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0.16)',#'rgba(37,37,37,1)',
            plot_bgcolor='rgba(0,0,0,0.16)',#'rgba(37,37,37,1)',
            font_color='white',
            title = {'text':'Technical Indicators',
                     'y':0.9,
                     'x':0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'})

        # plot size, hide legends & rangeslider
        fig.update_layout(height=680, width=1000, 
                          showlegend=False, 
                          xaxis_rangeslider_visible=False)

        # update axes labels
        fig.update_xaxes(title_text="Date", showgrid=False, row=4, col=1)
        fig.update_xaxes(showgrid=False, row=1, col=1)
        fig.update_yaxes(title_text="Price", showgrid=False, row=1, col=1)
        fig.update_yaxes(title_text="Volume", showgrid=False, row=2, col=1)
        fig.update_yaxes(title_text="MACD", showgrid=False, row=3, col=1)
        fig.update_yaxes(title_text="Stoch", showgrid=False, row=4, col=1)
        
        fig = go.FigureWidget(fig)
        
        interval = ipw.Dropdown(
                        options=time_intervals,
                        description='time_intervals')
        stock = ipw.Dropdown(
                options=stock_list,
                description='stock')
        
        def change_visible(new_interval, new_stock):
            def change_trace(trace):
                if new_interval in trace.name and new_stock in trace.name:
                    trace.update(visible=True)
                else:
                    trace.update(visible=False)

            fig.for_each_trace(change_trace)
            print(type(fig))
            fig.for_each_trace(lambda trace: print(trace.name + " " + str(trace.visible)))
        
        def update_visible_time(change):
            nonlocal curr_interval, cur_stock
            curr_interval = change.new
            print(curr_interval, cur_stock)
            change_visible(curr_interval, cur_stock)
                
        def update_visible_stock(change):
            nonlocal curr_interval, cur_stock
            cur_stock = change.new
            print(curr_interval, cur_stock)
            change_visible(curr_interval, cur_stock)
                
        interval.observe(update_visible_time, 'value')
        stock.observe(update_visible_stock, 'value')
        controls = ipw.VBox([interval, stock])
        layout = ipw.HBox([controls, fig])
        
        return layout


    def get_heatmap_widget(self, parent_path='./output/'):
        img_src = parent_path+'overview.png'
        img = Image.open(img_src)

        # Create figure
        fig = go.Figure()


        # Constants 
        img_width = 1400
        img_height = 400
        scale_factor = 1

        # Add invisible scatter trace.
        # This trace is added to help the autoresize logic work.
        fig.add_trace(
            go.Scatter(
                x=[0, img_width * scale_factor],
                y=[0, img_height * scale_factor],
                mode="markers",
                marker_opacity=0
            )
        )

        # Configure axes
        fig.update_xaxes(
            visible=False,
            range=[0, img_width * scale_factor]
        )

        fig.update_yaxes(
            visible=False,
            range=[0, img_height * scale_factor],
            # the scaleanchor attribute ensures that the aspect ratio stays constant
            scaleanchor="x"
        )

        # Add image
        fig.add_layout_image(
            dict(
                x=0,
                sizex=img_width * scale_factor,
                y=img_height * scale_factor,
                sizey=img_height * scale_factor,
                xref="x",
                yref="y",
                opacity=1.0,
                layer="below",
                sizing="stretch",
                source=img)
        )

        # Configure other layout
        fig.update_layout(
            width=img_width * scale_factor,
            height=img_height * scale_factor,
            margin={"l": 0, "r": 0, "t": 0, "b": 0},
        )

        widget = go.FigureWidget(fig, layout=ipw.Layout(width='100%'))
        # Disable the autosize on double click because it adds unwanted margins around the image
        # More detail: https://plotly.com/python/configuration-options/
        #fig.show(config={'doubleClick': 'reset'})
        return widget


    def get_index_stats_widget(self, sector_market_share, percent_change_df, data = ["^DJI","^IXIC", "^GSPC", "QQQ"]):
        '''
        Add documentation 
        '''
        mapp = {"^DJI": "DOW JONES","^IXIC":"NASDAQ", "^GSPC":"S&P 500", "QQQ": "QQQ Index"}
        vals = []
        cols = []
        stock_list = list(sector_market_share.keys())
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.index_performance.get_index_performance, sym): sym for sym in data}
            for future in concurrent.futures.as_completed(futures):
                change,per,symbol = future.result()
                if change:
                    vals.append((change,per,symbol))
                    
        for i in vals:
            if i[1] < 0:
                state = 'Bearish'
                fc = '<FONT COLOR = "RED">'
                arr = "&#8595"
                plus = ""
            else:
                state = 'Bullish'
                fc = '<FONT COLOR = "GREEN">'
                arr = "&#8593"
                plus = '+'
            col = ipw.HTML('<div style="width:200px;height:150px;border:6px; background:#2f2f30; margin:0 auto;">' + "<FONT COLOR = '#c1c1c7'>&nbsp" + mapp[i[2]] + "<br><FONT COLOR = 'WHITE'><b> &nbsp" + state + "<br>" + fc + "&nbsp" + plus + str(round(i[0],2)) + " (" + str(i[1]) + "%)" + arr + "</div></div>")
            cols.append(col)
        
        sector = self.sector.get_sector(percent_change_df)
        val = round(max(sector.values()),2)
        key = max(sector, key=sector.get)
        if val >= 0:
            fc = '<FONT COLOR = "GREEN">'
            arr = "&#8593"
        else:
            fc = '<FONT COLOR = "RED">'
            arr = "&#8595"
            
        sector_col = ipw.HTML('<div style="width:200px;height:150px;border:6px; background:#2f2f30; margin:0 auto;"><FONT COLOR = "#c1c1c7">&nbspHOTTEST SECTOR <br><FONT COLOR = "WHITE"><b> &nbsp'+ key + '<br>' + fc+ '&nbsp' + str(val) + '%' + arr)
        box_layout = Layout(width='1300px',
                        align_items='center',
                        display='flex',
                       justify_content='space-between',
                           )
        ret = ipw.HBox(children=cols+[sector_col], layout = box_layout)
        return ret


    def get_sector_wise_widget(self, percent_change_df):
        '''
        Add documentation
        '''
        def delete_multiple_element(list_object, indices):
            indices = sorted(indices, reverse=True)
            for idx in indices:
                if idx < len(list_object):
                    list_object.pop(idx)
        
        data = dict(sorted(self.sector.get_sector(percent_change_df).items(), key=lambda item: item[1]))

        names = list(data.keys())
        values = list(data.values())


        names_neg = []
        values_neg = []
        for i in range(len(names)):
            if values[i]<0:
                names_neg.append(names[i])
                values_neg.append(values[i])
            
        #get positive sectors
        neg_index = []
        for i in values:
            if i<0:
                neg_index.append(values.index(i))
                
        delete_multiple_element(values,neg_index)
        delete_multiple_element(names,neg_index)


        fig = go.Figure(layout=go.Layout(
        title=go.layout.Title(text="Sector Performance")))

        fig.add_trace(go.Bar(
            y=names_neg,
            x=values_neg,
            name='- sector',
            orientation='h',
            marker=dict(
                color='rgba(230, 40, 145, 0.8)',
                line=dict(color='rgba(200, 44, 13, 0.8)', width=3)
            )
        ))

        fig.add_trace(go.Bar(
                    x=values,
                    y=names,
                    name = '+ sector',
                    orientation='h',
                    marker=dict(
                        color='rgba(46, 202, 13, 0.8)',
                        line=dict(color='rgba(55, 139, 101, 0.8)', width=3)
            )
        ),)


        fig.update_layout(paper_bgcolor='rgba(0,0,0,0.16)',plot_bgcolor='rgba(0,0,0,0.16)')
        fig.update_layout(
            font_family="Courier New",
            font_color="white")

        widget = go.FigureWidget(fig, layout=ipw.Layout(width='100%'))
        
        return widget


    def get_cube_widget(self, percent_change_df):
        sector = self.sector.get_sector(percent_change_df)
        a = self.cube.cube_factory(sector)
        return a
