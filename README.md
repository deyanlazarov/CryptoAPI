# CryptoAPI
Wrapper for Cryptocompare -  https://www.cryptocompare.com


```
from pprint import pprint
from cryptoAPI import HistoryApi

api = HistoryApi()

pprint(api.get_daily("BTC", "EUR", 10, 1))

# get results for N days; Max 2000 
N_days = 10
result_day = ApiCallResult(api.get_daily("ETH", "USD", N_days))
# get results for N days; Max 2000 
N_minutes = 1440 # 24 hours
result_min = ApiCallResult(api.get_minutely("ETH", "USD", N_minutes))

df_daily = result_day.to_pandas()
df_min = result_min.to_pandas()

```

HistoryApi methods:
* get_daily           - Get open, high, low, close, volumefrom and volumeto from the daily historical data.
* get_hourly          - Get open, high, low, close, volumefrom and volumeto from the hourly historical data.
* get_minutely        - Get open, high, low, close, volumefrom and volumeto from the minutely historical data.


        :param from_currency: The cryptocurrency symbol of interest [Max character length: 10]
        :param to_currency: The currency symbol to convert into [Max character length: 10]
        :param limit: The number of data points to return
        :param aggregate: Time period to aggregate the data over (for daily it's days, for hourly it's hours and for minute histo it's minutes)
        :return: JSON Response
        

More help to come
