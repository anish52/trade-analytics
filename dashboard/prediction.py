import yfinance as yf
import TAcharts
from pandas.tseries.offsets import DateOffset

import numpy as np
import plotly.graph_objs as go

class Prediction:
    def __init__(self):
        self.stock_list = ['AZN','AAPL','NVDA','INTC','QCOM','MSFT','GOOGL','META','AMZN','WMT','TSLA','EA','UNH','CVS']
        self.window = 26
        self.start_date = "2021-06-01"
        self.end_date = "2022-05-30"
        self.interval='1d'
        self.percent = 2
        self.data = yf.download(
            self.stock_list,
            start=self.start_date,
            end=self.end_date,
            group_by='ticker',
            interval=self.interval,
            progress=False)


    def get_prediction(self):
        """
        Get prediction range of future stock predictions for the listed stocks
        Output:
            df1 : pd.dataframe
        """
        df1 = yf.download("AAPL",
                          start=self.start_date,
                          end=self.end_date,
                          group_by='ticker',
                          interval=self.interval,
                          progress=False)

        df1 = df1.drop(columns=['Close',"High","Low","Open","Adj Close","Volume"])
        # area plots of share price per stock
        for stk in self.stock_list:
            df1[stk] = self.data[stk]["Adj Close"]
            df1[stk+"A"] = float('NaN')
            df1[stk+"B"] = float('NaN')
        tmp = {}
        # area plots of share price per stock
        fig = go.Figure()
        off_date = df1.index[-1]
        for stk in self.stock_list:
            df = self.data[stk]
            df = df.drop(columns=['Close'])
            df.index.names = ['date']
            df.reset_index(inplace=True)
            df=df.rename(columns={'Open': 'open', 'High': 'high'})
            df=df.rename(columns={'Low': 'low', 'Adj Close': 'close'})
            df=df.rename(columns={'Volume': 'volume'})
            i = TAcharts.indicators.Ichimoku(df)

            i.build(9,26,52,26);


            l = len(df["close"])
            if i.ichimoku["senkou_a"][l] > i.ichimoku["senkou_b"][l]:
                mid =i.ichimoku["senkou_b"][l] +  (i.ichimoku["senkou_a"][l] - i.ichimoku["senkou_b"][l] ) /2
            else:
                mid =i.ichimoku["senkou_a"][l]  + (i.ichimoku["senkou_b"][l] - i.ichimoku["senkou_a"][l] ) /2

            if mid > df["close"][len(df["close"])-1]:
                deltaa =  mid - df["close"][len(df["close"])-1]
                deltab =  mid - df["close"][len(df["close"])-1]
            else:
                deltaa =  mid - df["close"][len(df["close"])-1]
                deltab =  mid - df["close"][len(df["close"])-1]
            #print(mid,deltaa,deltab)

            for j in range(26):
                i.ichimoku["senkou_a"][l+j] -= deltaa
                i.ichimoku["senkou_b"][l+j] -= deltab

            for j in range(l-79):
                i.ichimoku["senkou_b"][j+79] = float('NaN')
            #print(i.ichimoku)
            df['A'] = 0
            df['B'] = 0

            for j in range(26):
                if off_date+DateOffset(days=j+1) in tmp:
                    tmp[off_date+DateOffset(days=j+1)].append(float('NaN'))
                    tmp[off_date+DateOffset(days=j+1)].append(i.ichimoku["senkou_a"][l+j])
                    tmp[off_date+DateOffset(days=j+1)].append(i.ichimoku["senkou_b"][l+j])
                else:
                    tmp[off_date+DateOffset(days=j+1)] = [float('NaN'), i.ichimoku["senkou_a"][l+j],i.ichimoku["senkou_b"][l+j] ]
        for t in tmp:
            df1.loc[t] = tmp[t]
        return df1

    def fillcol(self, label):
        """
        Fill Color
        """
        if label == 0:
            return 'rgba(0,250,0,0.4)'
        else:
            return 'rgba(0,250,250,0.4)'



    def plot_pred(self, df1):
        """
        Plot of future stock predictions for the listed stocks
        Input:
            df1 : pd.dataframe
        Output:
            fig : FigureWidget
        """
        fig = go.Figure()
        for stock in self.stock_list:
            fig.add_trace(
                go.Scatter(
                    x=df1.index,
                    y=df1[stock],
                    mode='lines',
                    #fill='tozeroy',
                    hovertemplate = 'Stock: {}'.format(stock) + '<br>Date: %{x} </br>Price: %{y:$.2f}<extra></extra>',
                )
            )

            df1[stock +'label'] = np.where(df1[stock+"A"][-1]<df1[stock+"B"][-1], 1, 0)
            #print(stock,df1[stock +'label'].iloc[0])
            fig.add_traces(go.Scatter(x=df1.index, y = df1[stock+"A"],
                                      line = dict(color='rgba(0,0,0,0)'),
                                      hovertemplate = 'Lower limit: {}'.format(stock) + '<br>Date: %{x} </br>Price: %{y:$.2f}<extra></extra>',

                                     ))

            fig.add_traces(go.Scatter(x=df1.index, y = df1[stock+"B"],
                                      line = dict(color='rgba(0,0,0,0)'),
                                      fill='tonexty',
                                      hovertemplate = 'Upper limit: {}'.format(stock) + '<br>Date: %{x} </br>Price: %{y:$.2f}<extra></extra>',

                                      fillcolor = self.fillcol(df1[stock +'label'].iloc[0])))

        # layout for x axis and range slider/selector

        # layout for dropdown menu to select stock
        buttons_list = []
        buttons_list.append(
                    dict(label="All",
                         method="update",
                         args=[{"visible": [True] * len(self.stock_list)},
                               {"title": "PROJECTED DAILY SHARE PRICE"}])
            )
        for ind, stock in enumerate(self.stock_list):
            visible_list = [False] * len(self.stock_list) *3

            visible_list[3 *ind] = True
            visible_list[3 *ind+1] = True
            visible_list[3 *ind+2] = True
            buttons_list.append(
                        dict(label=stock,
                             method="update",
                             args=[{"visible": visible_list},
                                   {"title": '{} : PROJECTED DAILY SHARE PRICE'.format(stock)}])
            )

        # add dropdown menu and update fig layout
        fig.update_layout(
            showlegend = False,
            updatemenus=[
                dict(
                    active=0,
                    buttons=buttons_list,
                    bgcolor='rgb(179,226,205)',
                    x=-.15,
                    y=.9
                ),
            ],
            paper_bgcolor='rgba(37,37,37,1)',
            plot_bgcolor='rgba(37,37,37,1)',
            font_color='gray',
            title_font_color='white',
            title_font_size=22,
            title_font_family='Droid Serif',
            title = {'text':'PROJECTED DAILY SHARE PRICE',
                     'y':0.95,
                     'x':0.025,
                     'xanchor': 'left',
                     'yanchor': 'top'
                    },
            hovermode='x unified'
        )

        fig.update_layout(
            annotations=[
                dict(text="Select Stock:", x=-.26, xref="paper", y=1, yref="paper",
                                     align="left", showarrow=False, font_color='white')
            ])

        return go.FigureWidget(fig)
