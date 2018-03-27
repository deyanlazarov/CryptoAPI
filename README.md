# CryptoAPI
Wrapper for Cryptocompare -  https://www.cryptocompare.com


```
from pprint import pprint
from cryptoAPI import HistoryApi

api = HistoryApi()

pprint(api.get_daily("BTC", "EUR", 10, 1))
```

More help to come
