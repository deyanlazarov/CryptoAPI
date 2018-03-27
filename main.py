from pprint import pprint
from cryptoAPI import HistoryApi, ApiCallResult

api = HistoryApi()

#pprint(api.get_daily("BTC", "EUR", 10, 1))
#pprint(api.get_hourly("ETH", "USD", 10, 5))
#pprint(api.get_minutely("XMR", "GBP", 10, 3))

result = ApiCallResult(api.get_minutely("ETH", "USD", 1440, 0))

df = result.to_pandas()