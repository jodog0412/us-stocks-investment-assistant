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
        def dataframe_view(dataframe):
            '''1. seperate key and price'''
            keys, values = [key for key,value in dataframe], [value for key,value in dataframe]
            '''2. calculate profit percentage for stock'''
            func=lambda x:(x.values[-1]/x.values[0]-1) 
            data=list(map(func,values))
            '''3. Sort tickers by profit'''
            result=pd.Series(data=data,index=keys).sort_values(ascending=False).dropna()
            return result
        boundary=int(len(self.tickers)*filter_percent)
        
        tickers=Ticker(self.tickers,asynchronous=True)
        datafrm=list(tickers.history(start=start,end=end)['adjclose'].groupby('symbol'))
        result=dataframe_view(datafrm)
        
        if filter_reverse==False:
            return result[:boundary]
        else:
            return result[boundary:]