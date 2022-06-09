import pandas as pd

class Sector:
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
