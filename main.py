from flask import Flask, request
from widgets import get_banner_widget, index_stats_widget, get_heatmap_widget,\
					sector_wise_widget, cube_widget, stock_price_plot_factory,\
					ti_plot_factory
from prediction import get_prediction, plot_pred


app = Flask(__name__)

@app.route("/")
def update():

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
	print(df)

	stock_price_widget = stock_price_plot_factory(stock_list, data_list[0])
	print(stock_price_widget)

	ti_widget = ti_plot_factory(data_list, ti_list, time_intervals, stock_list, cur_stock, cur_interval)
	print(ti_widget)

	heatmap_widget = get_heatmap_widget(df)    
	print(heatmap_widget)

	banner_widget = get_banner_widget()
	print(banner_widget)

	index_stats_widget = index_stats_widget(sector_market_share, df)
	print(index_stats_widget)

	sector_wise_widget = sector_wise_widget(df)
	print(sector_wise_widget)

	cube_widget = cube_widget()
	print(cube_widget)

	pred_df = get_prediction()
	prediction_widget = plot_pred(pred_df)
	print(prediction_widget)

	widgets = {
		'Banner': banner_widget,
		'Summary': index_stats_widget, 
		'Heatmap': heatmap_widget,

		'Performance': sector_wise_widget,
		'Cube': cube_widget,

		'Pricechart': stock_price_widget,
		'TIGraph': ti_widget,

		'Bull_Bear': prediction_widget
	}

	with open('./output/cache.json', 'w+') as outfile:
		json.dump(widgets, outfile)
	
	return "<p>Success!</p>"

if __name__=="__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)