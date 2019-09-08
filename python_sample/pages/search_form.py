import logging

from selenium.webdriver.common.by import By
from webium import BasePage, Find

LOGGER = logging.getLogger(__name__)


class SearchForm(BasePage):
    min_price_input = Find(by=By.XPATH, value="//input[@name='price_before']")
    max_price_input = Find(by=By.XPATH, value="//input[@name='price_after']")
    show_results = Find(by=By.XPATH, value="//div[contains(@class, 'ModelFilter__ParamListBtnSel')]//span")

    def select_brand(self, brand):
        Find(by=By.XPATH, value="//div[@id='Attr_prof_1000']//label[text()='{}']"
             .format(brand), context=self).click()
        LOGGER.info("Brand has been set to '%s'", brand)

    def select_min_price(self, min_price):
        self.min_price_input.send_keys(min_price)
        LOGGER.info("Min price has been set to '%s'", min_price)

    def select_max_price(self, max_price):
        self.max_price_input.send_keys(max_price)
        LOGGER.info("Max price has been set to '%s'", max_price)

    def click_show_results(self):
        self.show_results.click()
        LOGGER.info("Click show results button")
