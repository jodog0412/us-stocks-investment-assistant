from yahooquery import Ticker
import numpy as np
import pandas as pd
from tqdm import tqdm

class financialCompare:
    def __init__(self,tickerDict:dict,command:str):
        self.tickerDict=tickerDict
        self.command=command
        self.tickers=tickerDict[command]
        self.ytickers=Ticker(self.tickers, asynchronous=True)

    def keyFinancialTable(self,filter=True):
        keyList=['PER','FPER','PBR','marketcap','freecashflow','PEGR','ROE','cRatio']
        valuation_key=('PeRatio','ForwardPeRatio','pbRatio','MarketCap','PegRatio')
        financial_key=('freeCashflow','returnOnEquity','currentRatio')
        financials=self.ytickers.financial_data
        valuations=self.ytickers.valuation_measures

        def financial(ticker,key):
            try: return financials[ticker][key]
            except (TypeError,KeyError): return np.nan

        def valuation(ticker,key):
            try: data=valuations.loc[ticker,key]
            except (AttributeError,KeyError): return np.nan #valuation doesn't return
            else: 
                try: return data.dropna().values[-1]
                except IndexError: return np.nan # valuation returns nan.
        
        def financial_search(targets,tickers):
            return [[financial(i,target) for i in tickers] for target in targets]
        
        def valuation_search(targets,tickers):
            return [[valuation(i,target) for i in tickers] for target in targets]
        
        per,fper,pbr,marketcap,pegr=valuation_search(valuation_key,tickers=self.tickers)
        freecashflow,roe,currentR=financial_search(financial_key,tickers=self.tickers)

        data=np.array([per,fper,pbr,marketcap,freecashflow,pegr,roe,currentR]).T
        datafrm=pd.DataFrame(data=data,index=self.tickers,columns=keyList).sort_values(by='FPER',ascending=False)
        
        if filter==False:
            return datafrm
        else: 
            return datafrm.loc[(datafrm['PER']>datafrm['FPER'])]
    
    def revenueTable(self):
        data=self.ytickers.earnings
        earnings=[pd.DataFrame(data=data[i]['financialsChart']['quarterly']).drop('date',axis=1).T 
                for i in self.tickers]
        result=pd.concat(earnings,keys=self.tickers,names=["ticker","indicator"])
        return result

    # def cashflowTable(self):
    #     def getCashflow(ticker):
    #         tickerflow=ticker.cashflow.loc[['Operating Cash Flow','Financing Cash Flow','Investing Cash Flow']]
    #         tickerflow.index=['Operating','Financing','Investing']
    #         tickerflow=tickerflow.transpose().sort_index()
    #         return tickerflow
    #     tickersflow=[getCashflow(ticker) for ticker in tqdm(self.yfTickers)]
    #     return dict(zip(self.tickers,tickersflow))

    def implement(self):
        data=financialCompare(self.tickerDict,self.command)
        if self.command=='WATCH':
            print(data.keyFinancialTable(filter=False))
        else:
            print(data.keyFinancialTable())
        print(data.revenueTable())
        # print(data.cashflowTable())
