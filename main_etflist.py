import pandas as pd
import time as time

import etf_list as etfList

# Get ETF List from ETF_US.csv
df = etfList.gatheringETFList_US()

print(df.head())

etfList.saveCSVFile(df, './data/ETF_US.csv')
