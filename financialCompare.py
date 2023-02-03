import yfinance as yf
import numpy as np
import pandas as pd
from tqdm import tqdm

def keyFinancialTable(tickerDict, command):
    if command=='SEARCH':
        tickers=tickerDict['SEARCH']
    else:
        tickers=tickerDict['WATCH']

    def getFinancial(ticker):
        def return_(info, key):
            try: return info[key]
            except KeyError: return "NaN"
        info=yf.Ticker(ticker).info
        infoCustom=[return_(info,"trailingPE"), return_(info,"forwardPE"), return_(info,"priceToBook"),
                    return_(info,"pegRatio"), return_(info,"returnOnEquity"),return_(info,"shortPercentOfFloat"),
                    return_(info,"quickRatio")]
        return infoCustom

    financial=[getFinancial(ticker) for ticker in tqdm(tickers)]
    df=pd.DataFrame(data=financial,
                    index=tickers,
                    columns=['PER', 'FPER', 'PBR',
                             'PEGR', 'ROE', 'short%', 'qRatio'])
    df=df.sort_values('FPER',ascending=False)
    return df

def revenueGrowthTable(tickers):
    revDict={}
    for ticker in tqdm(tickers):
        data=yf.Ticker(ticker).earnings
        revGrowth=[(data.iloc[i+1,0]-data.iloc[i,0])/data.iloc[i,0]*100 for i in range(3)]
        revDict[ticker]=revGrowth
    result=pd.DataFrame(data=revDict)
    return result

def cashflowTable(tickers):
    flowDict={}
    for ticker in tqdm(tickers):
        balance=yf.Ticker(ticker).cashflow.loc[['Operating Cash Flow','Financing Cash Flow','Investing Cash Flow']]
        balance.index=['Operating','Financing','Investing']
        balance=balance.transpose().sort_index()
        flowDict[ticker]=balance
    return flowDict