import pytest

from python_sample.data.data_generator import laptop_queries, get_ids


@pytest.mark.parametrize("laptop_query", laptop_queries, ids=get_ids)
def test_laptops_results(app, laptop_query):
    """Check search results for laptops"""
    app.open_home_page()
    app.navigation.navigate_to("Компьютеры", "Ноутбуки")
    app.search.select_query(laptop_query)
    app.search.click_show()
    app.results.check_first_page(laptop_query)
