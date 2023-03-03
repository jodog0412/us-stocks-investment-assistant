import pandas as pd
from indexSearch import indexSearch
from yahooquery import Ticker

startdate='2022-01-01'
enddate='2023-03-03'

index=indexSearch()
nyse, ndq = index.nyse, index.ndq

class tickerSearch:
    def __init__(self,index,sector):
        if index=='NYSE':
            data = dict(list(nyse.groupby('Industry')))
        elif index=='NASDAQ':
            data = dict(list(ndq.groupby('Industry')))
        self.tickers=list(data[sector]['Symbol'].values)

    def download(self,filterPercent=0.5):
        filterN=int(len(self.tickers)*filterPercent)
        ticker=Ticker(self.tickers,asynchronous=True)
        df=ticker.history(start=startdate,end=enddate)
        df=list(df['adjclose'].groupby('symbol'))
        keys, values = [key for key,value in df], [value for key,value in df]
        func=lambda x:(x.values[-1]/x.values[0]-1)
        data=list(map(func,values))
        result=pd.Series(data=data,index=keys).sort_values(ascending=False).dropna()
        return result[:filterN]