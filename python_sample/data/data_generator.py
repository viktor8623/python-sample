import pandas as pd

from python_sample.model.search_query import SearchQuery

laptops_tab = pd.read_excel("python_sample/data/search_queries.xlsx", "Laptops", dtype=str, keep_default_na=False)

laptops_dict = laptops_tab.to_dict(orient='records')

laptop_queries = []


def extract_test_data(test_data, excel_dict):
    for item in excel_dict:
        for key in item:
            if item[key] == "":
                item[key] = None
        test_data.append(SearchQuery(**item))


def get_ids(val):
    return repr(val)


extract_test_data(laptop_queries, laptops_dict)
