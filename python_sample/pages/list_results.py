import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import BasePage, Find, Finds
from webium.wait import wait

LOGGER = logging.getLogger(__name__)
RESULTS_ON_PAGE = 24


class ResultItem(WebElement):
    title = Find(by=By.XPATH, value=".//span[@itemprop='name']")
    min_price = Find(by=By.XPATH, value=".//span[@class='PriceBlock__PriceValue']/span")
    max_price = Find(by=By.XPATH, value=".//span[contains(@class, 'PriceBlock__PriceLastValue')]/span")


class ListResults(BasePage):
    list_results = Finds(ResultItem, by=By.XPATH, value="//div[@class='ModelList__ModelBlockRow']")
    max_prices = Finds(by=By.XPATH, value="//div[@class='ModelList__ModelBlockRow']//span[contains(@class, 'PriceBlock"
                                          "__PriceLastValue')]/span")

    def get_titles_list(self):
        wait(lambda: len(self.list_results) == RESULTS_ON_PAGE)
        titles = [item.title.text for item in self.list_results]
        LOGGER.info("Titles on the page: '%s'", titles)
        return titles

    def get_min_prices_list(self):
        min_prices = [int(item.min_price.text.replace(" ", "").replace(",", "")) / 100 for item in self.list_results]
        LOGGER.info("Min prices on the page: '%s'", min_prices)
        return min_prices

    def get_max_prices_list(self):
        max_prices = [int(max_price.text.replace(" ", "").replace(",", "")) / 100 for max_price in self.max_prices]
        LOGGER.info("Max prices on the page: '%s'", max_prices)
        return max_prices
