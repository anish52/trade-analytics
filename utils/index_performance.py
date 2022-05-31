import yfinance as yf

def get_index_performance(symbol):
    '''
    Function is used to get the current performance of Nasdaq, Dow Jones, and S&P 500 
    (currentPrice - previousClose)/(previousClose)
    The *quickStats* function utilizes this output.
    ...
    Parameters: symobl of index
    ...
    :return: amount of change, percent change, and stock symbol are returned 
    :rtype: tuple
    '''
    try:
        stock = yf.Ticker(symbol)
        a = stock.info['regularMarketPrice']
        b = stock.info['regularMarketPreviousClose']
        change = (a-b)
        per = round(((change/b)*100),2)
    except Exception:
        pass
    return (change,per,symbol)