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
    def __init__(self,index:str,sector:str):
        nyse,ndq=indexSearch().returns()
        if index=='NYSE':
            data = dict(list(nyse.groupby('Industry')))
        elif index=='NASDAQ':
            data = dict(list(ndq.groupby('Industry')))
        else: raise Exception("Index must be 'NYSE' or 'NASDAQ'")
        self.tickers=list(data[sector]['Symbol'].values)

    def download(self,start:str,end:str,filter_percent=0.5,filter_reverse=False):
        filterN=int(len(self.tickers)*filter_percent)
        tickers=Ticker(self.tickers,asynchronous=True)
        df=list(tickers.history(start=start,end=end)['adjclose'].groupby('symbol'))
        keys, values = [key for key,value in df], [value for key,value in df]
        func=lambda x:(x.values[-1]/x.values[0]-1) #Calculate profit of stocks
        data=list(map(func,values))
        result=pd.Series(data=data,index=keys).sort_values(ascending=False).dropna()
        if filter_reverse==False:
            return result[:filterN]
        else:
            return result[filterN:]
    