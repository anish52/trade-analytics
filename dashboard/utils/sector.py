import pandas as pd

class Sector:
    '''
    This class returns the sector wise performance based on the 
    weighted sum of the major stocks in each sector. The weights 
    are based on the market cap of each comapny.
    --------------------------------------------------------------
    Methods:
        - get_sector(): returns the sector-wise percentage change
    '''
    def __init__(self):
        pass

    def get_sector(self, df):
        dic = {}
        y = df.groupby(['sector'])
        for name, group in y:
            dic[name] = group.market_share.sum()

        df['sector_market_cap'] = df['sector'].map(dic)
        df['weight'] = (df.market_share/df.sector_market_cap) * df.percent_change
        for name, group in y:
            dic[name] = group.weight.sum()
        return dic
