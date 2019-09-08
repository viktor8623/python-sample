from python_sample.pages.search_form import SearchForm


class SearchActions:

    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.search_form = SearchForm(driver=self.driver)

    def select_query(self, query):
        if query.min_price is not None:
            self.search_form.select_min_price(query.min_price)
        if query.max_price is not None:
            self.search_form.select_max_price(query.max_price)
        if query.brand is not None:
            self.search_form.select_brand(query.brand)

    def click_show(self):
        self.search_form.click_show_results()
