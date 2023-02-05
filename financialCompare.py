import yfinance as yf
import numpy as np
import pandas as pd
from tqdm import tqdm

class financialCompare:
    def __init__(self,tickerDict,command):
        func=lambda x:yf.Ticker(x)
        self.tickerDict=tickerDict
        self.command=command
        self.tickers=tickerDict[command]
        self.yfTickers=list(map(func,self.tickers))

    def keyFinancialTable(self):
        def getFinancial(ticker):
            def _return(info, key):
                try: return info[key]
                except KeyError: return "NaN"
            def _divide(info,key1,key2):
                a=_return(info,key1)
                b=_return(info,key2)
                try: return a/b
                except TypeError: return "NaN"
            info=ticker.info
            keyInfo=[_return(info,"trailingPE"), _return(info,"forwardPE"), _return(info,"priceToBook"),
            _divide(info,'enterpriseValue','freeCashflow'),
            _return(info,"pegRatio"), _return(info,"returnOnEquity"), _return(info,"quickRatio")]
            return keyInfo
        financial=[getFinancial(ticker) for ticker in tqdm(self.yfTickers)]
        df=pd.DataFrame(data=financial,
                        index=self.tickers,
                        columns=['PER', 'FPER', 'PBR','PCR','PEGR', 'ROE', 'qRatio'])
        df=df.sort_values('FPER',ascending=False)
        return df

    def revenueGrowthTable(self):
        def getGrowth(ticker):
            data=ticker.earnings
            tickerGrowth=[(data.iloc[i+1,0]-data.iloc[i,0])/data.iloc[i,0]*100 for i in range(3)]
            return tickerGrowth
        tickersGrowth=[getGrowth(ticker) for ticker in tqdm(self.yfTickers)]
        result=pd.DataFrame(data=tickersGrowth,columns=self.tickers)
        return result

    def cashflowTable(self):
        def getCashflow(ticker):
            tickerflow=ticker.cashflow.loc[['Operating Cash Flow','Financing Cash Flow','Investing Cash Flow']]
            tickerflow.index=['Operating','Financing','Investing']
            tickerflow=tickerflow.transpose().sort_index()
            return tickerflow
        tickersflow=[getCashflow(ticker) for ticker in tqdm(self.yfTickers)]
        return dict(zip(self.tickers,tickersflow))

    def implement(self):
        data=financialCompare(self.tickerDict,self.command)
        print(data.keyFinancialTable())
        print(data.revenueGrowthTable())
        print(data.cashflowTable())


# def cashflowTable(tickers):
#     flowDict={}
#     for ticker in tqdm(tickers):
#         balance=yf.Ticker(ticker).cashflow.loc[['Operating Cash Flow','Financing Cash Flow','Investing Cash Flow']]
#         balance.index=['Operating','Financing','Investing']
#         balance=balance.transpose().sort_index()
#         flowDict[ticker]=balance
#     return flowDict