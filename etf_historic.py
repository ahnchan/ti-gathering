import requests
import pandas as pd
import json as json
import datetime as datetime
import time as time
import io as io

def convertTimestamp(date):
    '''
    date format is 'YYYY-MM-DD'
    '''
    element = datetime.datetime.strptime(date,"%Y-%m-%d")

    tuple = element.timetuple()
    timestamp = int(time.mktime(tuple))

    return timestamp

def gatheringHistoricDataFromYahoo(symbol, start, end):
    """
    Gathering Historic Datas from Yahoo Fainance

    :param symbol: TICKER
    :param start: start date (format: yyyy-mm-dd)
    :param end: end date (format: yyyy-mm-dd)
    :return: dataframe
    """

    period1 = convertTimestamp(start)
    period2 = convertTimestamp(end)

    #print (period1)
    #print (type(period1))
    #print (period2)

    params = {
        'period1': str(period1),
        'period2': str(period2),
        'interval': '1d',
        'events': 'history',
        'includeAdjustedClose': 'true',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }

    # Get Historic price data
    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + symbol
    response = requests.get(url, params=params, headers=headers)
    #print(response.url)

    csv_data = response.text
    # print(csv_data)

    df = pd.read_csv(io.StringIO(csv_data))

    #df.head()

    return df



