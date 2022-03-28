

import requests
import pandas as pd
import json as json
import datetime as datetime

def gatheringETFList_US():
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qSTBOa1pDTTBaR1JUTTROemRFUkRVM1JrRXdOelUxTkRoRVFrUTRNakpEUlRsQk9FWXdSUSJ9.eyJpc3MiOiJodHRwczovL2V0ZmRvdGNvbS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4NjE2ZTY2OWVmNTgwMDY4NjU5MWM2IiwiYXVkIjoiWjk1aUpHYWprOUhoMGtUUG9OWEF6UUU2OGRad0xGS3UiLCJleHAiOjE2NDc3NzQ3MTAsImlhdCI6MTY0NzczODcxMCwiYXpwIjoiWjk1aUpHYWprOUhoMGtUUG9OWEF6UUU2OGRad0xGS3UifQ.mYClUR8zh3mQDdweKhdmDf7jm0Cp2xAtNisgli6HfBl5IiGqHWX70q7JkjQja8_S_9CISFt0rnzDSsD2i3vu5Q1ft5rvk54lf8u7-j0p00AmrqKcuHIBNl6NHaAcdmrif-Gcgh2cj_f4iq8D-61SF0x5kCTRKJUbHWjPpIxA-l38cQ8IGtPAq0vvGgVT9d2hq1czhjnDsEplqaZ3G6zSXumX1VklahWrd_sW91snFSKACjodJV-7dqIxbb2VDoOwA3z139mnslelZ59U4boky7zx_UXzkDQo4NovuJcfuUUGWXQDisZIUy41ucI7nl8csTByQ1MQ2H9tvlWOnkGSoQ',
        'Content-Type': 'application/json',
        'Host': 'api.etf.com',
        'Origin': 'https://www.etf.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '80',
        'sec-ch-ua-platform': 'macOS',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'x-limit': '3000'
    }

    url = 'https://api.etf.com/private/finder/funddata'
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    df = pd.json_normalize(json_data)

    return df

def saveCSVFile(df, file_name):
    df.to_csv(file_name, index=False)

    return

def getCurrentDateYMD():
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    return date


def getETFList_US():

    # Read ETF list from CSV File.
    # File: ETF_US_LIST
    df = pd.read_csv('./data/ETF_US.csv')

    column_map = {
        'ticker': 'symbol', #idx 0, 단축코드
        'fund':'name',  #idx 1 종목명
        #'e82ff34dd7c8': "issuer", #idx 4 Issuer
        #'ee4e7b0130a8':"datetime_started", #idx 2 시작일
    }

    df1 = df.rename(columns=column_map)
    df1_columns = df1.columns[[0,1, 4, 2]].tolist()

    df2 = df1.loc[:, df1_columns].copy()

    return df2

'''
df = gatheringETFList_US()
print(df.head())
saveCSVFile(df, './data/ETF_US.csv')


df2 = getETFList_US()
print(df2.head())
'''

