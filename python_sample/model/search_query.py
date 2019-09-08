class SearchQuery:

    def __init__(self, **kwargs):
        self.id_testdata = kwargs.get('id_testdata')
        self.brand = kwargs.get('brand')
        self.min_price = kwargs.get('min_price')
        self.max_price = kwargs.get('max_price')

    def __repr__(self):
        return self.id_testdata
