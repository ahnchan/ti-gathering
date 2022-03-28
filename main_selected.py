import pandas as pd
import time as time

import etf_list as etfList
import etf_historic as etfHistoric

# Get ETF List from ETF_US.csv
#df = etfList.gatheringETFList_US()

#print(df.head())

print('Gathering ETF Historic prices')

symbol = 'PRN'

data = etfHistoric.gatheringHistoricDataFromYahoo(symbol, '1990-01-01', '2022-03-25')

print(data.head())
print(data.size)

etfList.saveCSVFile(data, './data_etf_us/'+ symbol +'.csv')

