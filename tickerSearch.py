import numpy as np
import pandas as pd
import yfinance as yf
import FinanceDataReader as fdr
from tqdm import tqdm
from indexSearch import indexSearch
startdate='2022-01-01'
enddate='2023-02-02'

index=indexSearch()
nyse, ndq = index.nyse, index.ndq

class tickerSearch:
    def __init__(self,index,sector):
        if index=='NYSE':
            data = dict(list(nyse.groupby('Industry')))
        if index=='NASDAQ':
            data = dict(list(ndq.groupby('Industry')))
        tickers=list(data[sector]['Symbol'].values)
        self.tickerFilt=[ticker for ticker in tqdm(tickers) if yf.download(ticker,progress=False).empty!=True]

    def download(self,filterPercent=0.5):
        tickers=self.tickerFilt
        filterN=int(len(tickers)*filterPercent)
        data=yf.download(tickers,start=startdate,end=enddate)
        result=(data['Adj Close'].iloc[-1]/data['Adj Close'].iloc[0]-1).sort_values(ascending=False).dropna()
        return result[:filterN]