import pandas as pd
import time as time

import etf_list as etfList
import etf_historic as etfHistoric

# Get ETF List from ETF_US.csv
df = etfList.gatheringETFList_US()

# print(df.head())

print('Gathering ETF Historic prices')

for index, row in df.iterrows():
    symbol = row.iloc[0]

    # ERROR
    #if (index < 2883):
    #    continue

    print(str(index) +':'+ symbol)

    # get Historic Data from Yahoo Finance
    data = etfHistoric.gatheringHistoricDataFromYahoo(symbol, '1990-01-01', '2022-03-25')
    etfList.saveCSVFile(data, './data_etf_us/'+ symbol +'.csv')

    # wait 1 second
    #time.sleep(1)

    # Debug
    #if (index == 2):
    #    break
