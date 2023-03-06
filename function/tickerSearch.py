import os.path
import FinanceDataReader as fdr
import pandas as pd
from yahooquery import Ticker

startdate='2022-01-01'
enddate='2023-03-06'

class indexSearch:
    def __init__(self):
        if os.path.isfile('nyse_tickers') and os.path.isfile('nasdaq_tickers'):
            self.nyse=pd.read_csv('nyse_tickers')
            self.ndq=pd.read_csv('nasdaq_tickers')
        else:
            self.nyse=fdr.StockListing('NYSE')
            self.ndq=fdr.StockListing('NASDAQ')
            self.nyse.to_csv('nyse_tickers')
            self.ndq.to_csv('nasdaq_tickers')

    def returns(self):
        nyse,ndq=self.nyse,self.ndq
        return nyse,ndq
    
    def sectorList(self):
        sectors=list(set(self.nyse['Industry'].values))
        sectors=pd.Series(sectors).sort_values().values
        return sectors

class tickerSearch():
    def __init__(self,index,sector):
        nyse,ndq=indexSearch().returns()
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
        func=lambda x:(x.values[-1]/x.values[0]-1) #Calculate profit of stocks
        data=list(map(func,values))
        result=pd.Series(data=data,index=keys).sort_values(ascending=False).dropna()
        return result[:filterN]