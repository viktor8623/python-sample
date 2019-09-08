import logging

from python_sample.pages.left_navigation_bar import LeftNavigationBar

LOGGER = logging.getLogger(__name__)


class Navigation:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.navigation_bar = LeftNavigationBar(driver=self.driver)

    def navigate_to(self, section, subsection):
        self.navigation_bar.hover_section(section)
        self.navigation_bar.select_subsection(subsection)
        LOGGER.info("Navigate to %s -> %s", section, subsection)
