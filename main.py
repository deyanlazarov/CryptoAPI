from pprint import pprint
from cryptoAPI import HistoryApi, ApiCallResult
import time

api = HistoryApi()

#pprint(api.get_daily("BTC", "EUR", 10, 1))
#pprint(api.get_hourly("ETH", "USD", 10, 5))
#pprint(api.get_minutely("XMR", "GBP", 10, 3))

# get results for N days; Max 2000 
N_days = 10
result_day = ApiCallResult(api.get_daily("ETH", "USD", N_days))
# get results for N days; Max 2000 
N_minutes = 1440 # 24 hours
result_min = ApiCallResult(api.get_minutely("ETH", "USD", N_minutes))

df_daily = result_day.to_pandas()
df_min = result_min.to_pandas()


