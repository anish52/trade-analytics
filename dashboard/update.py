import json, pickle
from utils.vanilla_dataloader import Vanilla_dataloader
from utils.heatmap import Heatmap
from prediction import Prediction

class Update(object):
	"""
	This module is used to update the cache. This cache is eventually
	used to render the dashboard. We can set the time interval for this
	cache refresh based on our requirements. This can be done using a
	cron job which runs this function at every 't' time interval.

	Currently, this can be set to 5 mins as it the minimum time interval
	for which we monitor any price change for a given stock.
	"""
	def __init__(self, arg=None):
		super(Update, self).__init__()
		self.data_loader = Vanilla_dataloader()
		self.pred = Prediction()
		self.arg = arg
		
	def save_as_pickle(self, parent_path='./output/'):
		sector_market_share = {
			'AAPL': ['Electronics Technology', 2455053795328],
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
			'WMT': ['Retail Trade', 356388110336]
		} 

		stock_list = list(sector_market_share.keys())
		time_intervals = ['1d', '30m', '5m']

		cur_stock = stock_list[0]
		cur_interval = time_intervals[0]

		data_list, ti_list = self.data_loader.load_data(stock_list)
		df = self.data_loader.percent_change_df(data_list, sector_market_share)

		pred_df = self.pred.get_prediction()

		w = {
			'data_list': data_list,
			'ti_list': ti_list,
			'df': df,
			'pred_df': pred_df
		}

		import os
		print(os.getcwd())
		with open (parent_path+'cache.pkl','wb') as f:
			pickle.dump(w, f)

		hmp = Heatmap()
		img_src = hmp.get_heatmap(df, parent_path+'overview.png')
		return

