import pandas as pd
import os.path
import FinanceDataReader as fdr
from yahooquery import Ticker

class indexSearch:
    def __init__(self):
        if os.path.isfile('./data/nyse_tickers') and os.path.isfile('./data/nasdaq_tickers'):
            self.nyse=pd.read_csv('./data/nyse_tickers')
            self.ndq=pd.read_csv('./data/nasdaq_tickers')
        else:
            self.nyse=fdr.StockListing('NYSE')
            self.ndq=fdr.StockListing('NASDAQ')
            self.nyse.to_csv('./data/nyse_tickers')
            self.ndq.to_csv('./data/nasdaq_tickers')

    def returns(self):
        return self.nyse,self.ndq
    
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
        else: raise Exception("Input is not matching for index.")
        self.tickers=list(data[sector]['Symbol'].values)

    def download(self,start,end,filterPercent=0.5):
        filterN=int(len(self.tickers)*filterPercent)
        ticker=Ticker(self.tickers,asynchronous=True)
        df=list(ticker.history(start=start,end=end)['adjclose'].groupby('symbol'))
        keys, values = [key for key,value in df], [value for key,value in df]
        func=lambda x:(x.values[-1]/x.values[0]-1) #Calculate profit of stocks
        data=list(map(func,values))
        result=pd.Series(data=data,index=keys).sort_values(ascending=False).dropna()
        return result[:filterN]
    