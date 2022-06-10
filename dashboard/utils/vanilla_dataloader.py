import yfinance as yf
import pandas as pd
import ta
from ta.trend import MACD
from ta.momentum import StochasticOscillator


class Vanilla_dataloader:
    '''
    This class queries the yfinance API and generates the data for
    the list of stocks passed as parameters. 
    ---------------------------------------------------------------------------
    Methods:
        - load_data(): returns the data for the list of stocks passed as params
        - percent_change_df(): returns the percentage change based on the prev. closing price
    '''
    def __init__(self):
        pass


    def load_data(self, stock_list):
        # load data
        period = '2y'; interval = '1d'
        data_daily = yf.download(
                        # tickers list or string as well
                        tickers = stock_list,

                        # use "period" instead of start/end
                        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                        # (optional, default is '1mo')
                        period = period,

                        # fetch data by interval (including intraday if period < 60 days)
                        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                        # (optional, default is '1d')
                        interval = interval,

                        # group by ticker (to access via data['SPY'])
                        # (optional, default is 'column')
                        group_by = 'ticker',

                        # adjust all OHLC automatically
                        # (optional, default is False)
                        auto_adjust = True,

                        # download pre/post regular market hours data
                        # (optional, default is False)
                        prepost = False,

                        # use threads for mass downloading? (True/False/Integer)
                        # (optional, default is True)
                        threads = True,

                        # proxy URL scheme use use when downloading?
                        # (optional, default is None)
                        proxy = None,

                        progress=False
            )

        period = '1wk'; interval = '30m'
        data_30m = yf.download(
                        tickers = stock_list,
                        period = period,
                        interval = interval,
                        group_by = 'ticker',
                        auto_adjust = True,
                        prepost = False,
                        threads = True,
                        proxy = None,
                        progress=False
            )

        period = '1d'; interval = '5m'
        data_5m = yf.download(
                        tickers = stock_list,
                        period = period,
                        interval = interval,
                        group_by = 'ticker',
                        auto_adjust = True,
                        prepost = False,
                        threads = True,
                        proxy = None,
                        progress=False
            )

        data_list = [data_daily, data_30m, data_5m]

        # add moving averages
        for data in data_list:
            for stock in stock_list:
                data[stock, 'MA20'] = data[stock, 'Close'].rolling(window=20).mean()
                data[stock, 'MA5'] = data[stock, 'Close'].rolling(window=5).mean()
            data.sort_index(axis=1, inplace=True)

        # data for technical indicators
        ti_daily = pd.DataFrame(index=['MACD', 'STOCH'], columns=stock_list)
        ti_30m = pd.DataFrame(index=['MACD', 'STOCH'], columns=stock_list)
        ti_5m = pd.DataFrame(index=['MACD', 'STOCH'], columns=stock_list)
        ti_list = [ti_daily, ti_30m, ti_5m]

        for ti, data in zip(ti_list, data_list):
            for stock in stock_list:
                #ti.loc['MACD', stock] = 2
                ti.loc['MACD', stock] = MACD(close=data[stock]['Close'],
                                               window_slow=26,
                                               window_fast=12,
                                               window_sign=9)  # MACD
                ti.loc['STOCH', stock] = StochasticOscillator(high=data[stock]['High'],
                                                 close=data[stock]['Close'],
                                                 low=data[stock]['Low'],
                                                 window=14,
                                                 smooth_window=3)  # stochastic

        return data_list, ti_list

    def percent_change_df(self, data_list, sector_market_share):
        cols = list(map(lambda x: (x, 'Close'), list(sector_market_share.keys())))
        prev_date = data_list[2].dropna(subset=cols).iloc[-1,:].name


        x = data_list[0].loc[:prev_date.date() + pd.DateOffset(1),:].iloc[-2,:]
        y = data_list[2].dropna(subset=cols).iloc[-1,:]
        dic = {}
        for i in list(sector_market_share.keys()):
            close = x[i].Close
            curr = y[i].Close
            dic[i] = [round(((curr-close)/(close)) * 100,2)]
            dic[i].append(sector_market_share[i][0])
            dic[i].append(sector_market_share[i][1])
        df = pd.DataFrame.from_dict(dic, orient ='index')
        df = df.rename(columns={0: "percent_change", 1: "sector", 2: "market_share"})
        df.index.name = 'stock'
        return df
