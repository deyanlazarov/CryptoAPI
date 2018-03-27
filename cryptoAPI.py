from _base import BaseMinerApi
from pprint import pprint

PARAM_FROM_CURRENCY = 'fsym'
PARAM_TO_CURRENCY = 'tsym'
PARAM_LIMIT = 'limit'
PARAM_AGGREGATE = 'aggregate'

HISTORY_MINUTE = "histominute"
HISTORY_HOUR = "histohour"
HISTORY_DAY = "histoday"
DEFAULT_LIMIT = 100
DEFAULT_AGGREGATE = 0

class HistoryApi(BaseMinerApi):
    def get_daily(self, from_currency, to_currency, limit = DEFAULT_LIMIT, aggregate = DEFAULT_AGGREGATE):
        """
        Get open, high, low, close, volumefrom and volumeto from the daily historical data.
        :param from_currency: The cryptocurrency symbol of interest [Max character length: 10]
        :param to_currency: The currency symbol to convert into [Max character length: 10]4
        :param limit: The number of data points to return
        :param aggregate: Time period to aggregate the data over (for daily it's days, for hourly it's hours and for minute histo it's minutes)
        :return: JSON Response
        """
        return self.__get(HISTORY_DAY, from_currency, to_currency, limit, aggregate)

    def get_hourly(self, from_currency, to_currency, limit = DEFAULT_LIMIT, aggregate = DEFAULT_AGGREGATE):
        """
        Get open, high, low, close, volumefrom and volumeto from the hourly historical data.
        :param from_currency: The cryptocurrency symbol of interest [Max character length: 10]
        :param to_currency: The currency symbol to convert into [Max character length: 10]
        :param limit: The number of data points to return
        :param aggregate: Time period to aggregate the data over (for daily it's days, for hourly it's hours and for minute histo it's minutes)
        :return: JSON Response
        """
        return self.__get(HISTORY_HOUR, from_currency, to_currency, limit, aggregate)

    def get_minutely(self, from_currency, to_currency, limit = DEFAULT_LIMIT, aggregate = DEFAULT_AGGREGATE):
        """
        Get open, high, low, close, volumefrom and volumeto from the minutely historical data.
        :param from_currency: The cryptocurrency symbol of interest [Max character length: 10]
        :param to_currency: The currency symbol to convert into [Max character length: 10]
        :param limit: The number of data points to return
        :param aggregate: Time period to aggregate the data over (for daily it's days, for hourly it's hours and for minute histo it's minutes)
        :return: JSON Response
        """
        return self.__get(HISTORY_MINUTE, from_currency, to_currency, limit, aggregate)

    def __get(self, path, from_currency, to_currency, limit = DEFAULT_LIMIT, aggregate = DEFAULT_AGGREGATE):
        params = {
            PARAM_FROM_CURRENCY: from_currency,
            PARAM_TO_CURRENCY: to_currency,
            PARAM_LIMIT: limit,
            PARAM_AGGREGATE: aggregate
        }
        return self.query(path, params)

class ApiCallResult:
    
    def __init__(self,api_call_json):
        self.api_call_json = api_call_json
        
    def to_pandas(self, human_date = True, format = None):
        import pandas as pd
        
        df = pd.DataFrame(self.api_call_json['Data'])
        if human_date:
            df['time'] = pd.to_datetime(df['time'],unit = 's') 
        return df
    
    def save_to_file(self, path, mode = 'a'):
        import json
        with open(path, mode = mode) as f:
            f.write(str(json.dumps(self.api_call_json, indent=1)))
            
        

class RealtimeAPI(BaseMinerApi):
    pass