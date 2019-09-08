import logging

import webium.settings
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from python_sample.actions.navigation import Navigation
from python_sample.actions.results import ResultsActions
from python_sample.actions.search import SearchActions

LOGGER = logging.getLogger(__name__)


class Application:

    def __init__(self, browser, url):
        self.url = url
        if browser == "chrome":
            options = Options()
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(options=options)
        elif browser == "edge":
            self.driver = webdriver.Edge()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))
        self.driver.implicitly_wait(30)
        webium.settings.wait_timeout = 15
        LOGGER.info("Started browser %s", browser)
        self.navigation = Navigation(self)
        self.search = SearchActions(self)
        self.results = ResultsActions(self)
        self.url = url

    def open_home_page(self):
        self.driver.get(self.url)
        LOGGER.info("Open url '%s'", self.url)

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.current_url()
            LOGGER.info("Browser is valid")
            return True
        except WebDriverException:
            return False

    def current_url(self):
        return self.driver.current_url
