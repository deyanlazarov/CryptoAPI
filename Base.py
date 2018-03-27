import requests


class QueryMixin:
    def query(self, url , params, error_check = True):
        try:
            response = requests.get(url, params).json()
        except Exception as e:
            print('Error getting information. {}'.format(str(e)))
            return None
        if error_check and (response.get('Response') == 'Error'):
            print('[ERROR]  {}'.format(response.get('Message')))
        
        return response
    
    

# ******************************************************************************

        
class BaseMinerApi(QueryMixin):
    def __init__(self, base_url = "https://min-api.cryptocompare.com/data/"):
        self.baseUrl = base_url

    def query(self, path, params, error_check = True):
        # TODO: make a function for more reliable concatenation of the url parts
        return super(BaseMinerApi, self).query(self.baseUrl + path, params, error_check)

