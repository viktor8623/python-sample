import logging

from python_sample.pages.list_results import ListResults

LOGGER = logging.getLogger(__name__)


class ResultsActions:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.list_results = ListResults(driver=self.driver)

    def check_first_page(self, query):
        for title in self.list_results.get_titles_list():
            assert query.brand in title
        LOGGER.info("Titles on the page has been verified")
        for min_price in self.list_results.get_min_prices_list():
            assert min_price >= int(query.min_price), "Actual min price is lower than selected"
            assert min_price <= int(query.max_price), "Actual min price is higher than selected max price"
        LOGGER.info("Min price on the page has been verified")
        for max_price in self.list_results.get_max_prices_list():
            assert max_price <= int(query.max_price), "Actual max price is higher then selected"
        LOGGER.info("Max price on the page has been verified")
