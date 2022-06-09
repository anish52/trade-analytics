import pytest
import ipywidgets as ipw
import pickle

from widgets import Widgets
from utils.vanilla_dataloader import Vanilla_dataloader


class TestWidgets:
    # def init_test(self):
    #     self.test_list = {
    #         "cube": Widgets.get_cube_widget,
    #         "heatmap": Widgets.get_heatmap_widget,
    #         "index_stats": Widgets.get_index_stats_widget,
    #         "banner": Widgets.get_banner_widget,
    #         "sector": Widgets.get_sector_wise_widget,
    #         "tech_indicators": Widgets.ti_plot_factory,
    #         "stock_price": Widgets.stock_price_plot_factory,
    #     }
    #
    #     # Use the run in widgets
    #     self.sector_market_share = {'AAPL': ['Electronics Technology', 2455053795328],
    #                            'AMZN': ['Retail Trade', 1167926362112],
    #                            'AZN': ['Healthcare', 208860000000],
    #                            'CVS': ['Healthcare', 129431887872],
    #                            'EA': ['Consumer Durables', 39177392128],
    #                            'META': ['Technology Servies', 532804836352],
    #                            'GOOGL': ['Technology Servies', 1482231906304],
    #                            'INTC': ['Electronics Technology', 181184856064],
    #                            'MSFT': ['Technology Servies', 2051480354816],
    #                            'NVDA': ['Electronics Technology', 468770127872],
    #                            'QCOM': ['Electronics Technology', 156531195904],
    #                            'TSLA': ['Consumer Durables', 762865975296],
    #                            'UNH': ['Healthcare', 475756396544],
    #                            'WMT': ['Retail Trade', 356388110336]}
    #
    #     self.stock_list = list(self.sector_market_share.keys())
    #     self.time_intervals = ['1d', '30m', '5m']
    #
    #     self.cur_stock = self.stock_list[0]
    #     self.cur_interval = self.time_intervals[0]
    #
    #     self.data_loader = Vanilla_dataloader()
    #
    #     self.data_list, ti_list = self.data_loader.load_data(self.stock_list)
    #     self.data_daily = self.data_list[0]
    #     self.df = self.data_loader.percent_change_df(self.data_list, self.sector_market_share)
    #
    #     with open('./output/cache.pkl', 'rb') as f:
    #         self.d = pickle.load(f)
    #
    #     self.data_list, ti_list = self.d['data_list'], self.d['ti_list']
    #     self.df = self.d['df']
    #     self.pred_df = self.d['pred_df']
    #
    # def test_widgets(self):
    #     self.init_test()
    #     a = Widgets()
    #     for key, func in self.test_list.items():
    #         print(self.__dict__, vars(self))
    #         assert isinstance(getattr(a, func(a, **vars(self))), ipw.Widget), key

    def test_widgets_vanilla(self):
        sector_market_share = {'AAPL': ['Electronics Technology', 2455053795328],
                               'AMZN': ['Retail Trade', 1167926362112],
                               'AZN': ['Healthcare', 208860000000],
                               'CVS': ['Healthcare', 129431887872],
                               'EA': ['Consumer Durables', 39177392128],
                               'META': ['Technology Servies', 532804836352],
                               'GOOGL': ['Technology Servies', 1482231906304],
                               'INTC': ['Electronics Technology', 181184856064],
                               'MSFT': ['Technology Servies', 2051480354816],
                               'NVDA': ['Electronics Technology', 468770127872],
                               'QCOM': ['Electronics Technology', 156531195904],
                               'TSLA': ['Consumer Durables', 762865975296],
                               'UNH': ['Healthcare', 475756396544],
                               'WMT': ['Retail Trade', 356388110336]}

        stock_list = list(sector_market_share.keys())
        time_intervals = ['1d', '30m', '5m']

        cur_stock = stock_list[0]
        cur_interval = time_intervals[0]

        data_loader = Vanilla_dataloader()

        data_list, ti_list = data_loader.load_data(stock_list)
        df = data_loader.percent_change_df(data_list, sector_market_share)

        with open('./output/cache.pkl', 'rb') as f:
            d = pickle.load(f)

        data_list, ti_list = d['data_list'], d['ti_list']
        df = d['df']
        pred_df = d['pred_df']

        a = Widgets()

        stock_price_widget = a.stock_price_plot_factory(stock_list, data_list[0])
        assert isinstance(stock_price_widget, ipw.Widget), "stock_price"

        ti_widget = a.ti_plot_factory(data_list, ti_list, time_intervals, stock_list, cur_stock, cur_interval)
        assert isinstance(ti_widget, ipw.Widget), "tech_indicator"

        heatmap_widget = a.get_heatmap_widget()
        assert isinstance(heatmap_widget, ipw.Widget), "heatmap"

        banner_widget = a.get_banner_widget()
        assert isinstance(banner_widget, ipw.Widget), "banner"

        index_stats_widget = a.get_index_stats_widget(sector_market_share, df)
        assert isinstance(index_stats_widget, ipw.Widget), "index_stats"

        sector_wise_widget = a.get_sector_wise_widget(df)
        assert isinstance(sector_wise_widget, ipw.Widget), "sectors"

        cube_widget = a.get_cube_widget(df)
        assert isinstance(cube_widget, ipw.Widget), "cube"
