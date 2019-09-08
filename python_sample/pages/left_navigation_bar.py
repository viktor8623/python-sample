from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find
from webium.wait import wait


class LeftNavigationBar(BasePage):
    sections = Finds(by=By.XPATH, value="//span[contains(@class, 'Catalog__SectionLevel1')]")
    subsections = Finds(by=By.XPATH, value="//span[contains(@class, 'Catalog__SectionLevel3')]/a")

    def get_link_by_text(self, text):
        return Find(by=By.LINK_TEXT, value="{}".format(text), context=self)

    def hover_section(self, section_name):
        for section in self.sections:
            if section.text == section_name:
                ActionChains(self._driver).move_to_element(section).perform()
                wait(lambda: len(self.subsections) > 0)
                break

    def select_subsection(self, subsection_name):
        self.get_link_by_text(subsection_name).click()
