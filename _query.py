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
    
    