from _query import QueryMixin
        
class BaseMinerApi(QueryMixin):
    def __init__(self, base_url = "https://min-api.cryptocompare.com/data/"):
        self.baseUrl = base_url

    def query(self, path, params, error_check = True):
        # TODO: make a function for more reliable concatenation of the url parts
        return super(BaseMinerApi, self).query(self.baseUrl + path, params, error_check)

