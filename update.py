import json, pickle
from utils.vanilla_dataloader import load_data, percent_change_df
from utils.heatmap import get_heatmap
from prediction import get_prediction


def save_as_pickle():
	sector_market_share = {
		'AAPL': ['Electronics Technology', 2455053795328],
		'AMZN': ['Retail Trade', 1167926362112],
		'AZN': ['Healthcare', 208860000000],
		'CVS': ['Healthcare', 129431887872],
		'EA': ['Consumer Durables', 39177392128],
		'FB': ['Technology Servies', 542804836352],
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

	data_list, ti_list = load_data(stock_list)
	df = percent_change_df(data_list, sector_market_share)
	pred_df = get_prediction()

	w = {
		'data_list': data_list,
		'ti_list': ti_list,
		'df': df,
		'pred_df': pred_df
	}

	with open ('./output/cache.pkl','wb') as f:
		pickle.dump(w, f)

	img_src = get_heatmap(df)
	return

if __name__ == '__main__':
	from widgets import get_banner_widget, get_index_stats_widget, get_heatmap_widget,\
					get_sector_wise_widget, get_cube_widget, stock_price_plot_factory,\
					ti_plot_factory
	from prediction import get_prediction, plot_pred

	save_as_pickle()

	sector_market_share = {
		'AAPL': ['Electronics Technology', 2455053795328],
		'AMZN': ['Retail Trade', 1167926362112],
		'AZN': ['Healthcare', 208860000000],
		'CVS': ['Healthcare', 129431887872],
		'EA': ['Consumer Durables', 39177392128],
		'FB': ['Technology Servies', 542804836352],
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

	with open ('./output/cache.pkl','rb') as f:
		d = pickle.load(f)

	data_list, ti_list = d['data_list'], d['ti_list']
	df = d['df']
	pred_df = d['pred_df']

	stock_price_widget = stock_price_plot_factory(stock_list, data_list[0])
	print('Done: stock_price_widget!')

	ti_widget = ti_plot_factory(data_list, ti_list, time_intervals, stock_list, cur_stock, cur_interval)
	print('Done: ti_widget!')

	heatmap_widget = get_heatmap_widget(df)    
	print('Done: heatmap_widget!')

	index_stats_widget = get_index_stats_widget(sector_market_share, df)
	print('Done: index_stats_widget!')

	sector_wise_widget = get_sector_wise_widget(df)
	print('Done: sector_wise_widget!')

	cube_widget = get_cube_widget(df)
	print('Done: cube_widget!')

	prediction_widget = plot_pred(pred_df)
	print('Done: prediction_widget!')

