import pandas as pd
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor

def stock_metrics():
    stocks = {
        'Electronics Technology': ['AAPL','NVDA','INTC','QCOM'],
        'Technology Servies': ['MSFT','GOOGL','FB'],
        'Retail Trade': ['AMZN','WMT'],
        'Consumer Durables': ['TSLA','EA'],
        'Health': ['UNH','AZN','CVS']
    }
    stock_list = []
    for el in stocks.values():
        stock_list.extend(el)


    data = {'stock':[], 'sector':[], 'regularMarketOpen':[], 'regularMarketPrice':[],\
            'prev_close':[], 'curr_close':[], 'market_cap':[]}

    def get_stats(ticker):
        info = yf.Tickers(ticker).tickers[ticker].info
        prev, curr = yf.Tickers(ticker).tickers[ticker].history('2d')['Close']
        data['stock'].append(ticker)
        data['regularMarketOpen'].append(info['regularMarketOpen'])
        data['regularMarketPrice'].append(info['regularMarketPrice'])
        data['prev_close'].append(prev)
        data['curr_close'].append(curr)
        data['market_cap'].append(info['marketCap'])
        data['sector'].append(info['sector'])

    ticker_list = stock_list.copy()

    with ThreadPoolExecutor() as executor:
        executor.map(get_stats, ticker_list)


    df = pd.DataFrame.from_dict(data)
    df['percentage_change'] = (df['curr_close'] - df['prev_close']) * 100 / df['prev_close']
    df = df.round(2)
    df = df.set_index('stock')
    return df, stock_list
    
if __name__=="__main__":
    df, stock_list = stock_metrics()
    print(df)
    print(stock_list)