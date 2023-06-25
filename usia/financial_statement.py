from yahooquery import Ticker
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class financialCompare:
    def __init__(self,tickers:list):
        self.tickers=tickers
        self.ytickers=Ticker(self.tickers, asynchronous=True)

    def keyFinancialTable(self):
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
        
        '''Return stock tickers if TPER>FPER'''
        return round(datafrm.loc[(datafrm['PER']>datafrm['FPER'])],2)
    
    def revenueTable(self):
        data=self.ytickers.earnings
        earnings=[pd.DataFrame(data=data[i]['financialsChart']['quarterly']).drop('date',axis=1).T 
                for i in self.tickers]
        result=pd.concat(earnings,keys=self.tickers,names=["ticker","indicator"])
        return result
    
    def plot(self,start,end):
        length=len(self.tickers)
        histories=list(self.ytickers.history(start=start,end=end)['adjclose'].groupby('symbol'))
        fig,axs=plt.subplots(length//2+length%2,2)
        fig.tight_layout()
        for index in range(len(self.tickers)):
            ticker=histories[index][1].index[0][0]
            cur_axis=axs[index//2,index%2]
            cur_axis.plot(histories[index][1][ticker])
            cur_axis.set_title(ticker)
        return plt.show()
    
    # def cashflowTable(self):
    #     def getCashflow(ticker):
    #         tickerflow=ticker.cashflow.loc[['Operating Cash Flow','Financing Cash Flow','Investing Cash Flow']]
    #         tickerflow.index=['Operating','Financing','Investing']
    #         tickerflow=tickerflow.transpose().sort_index()
    #         return tickerflow
    #     tickersflow=[getCashflow(ticker) for ticker in tqdm(self.yfTickers)]
    #     return dict(zip(self.tickers,tickersflow))

    def implement(self):
        data=financialCompare(self.tickers)
        print(data.keyFinancialTable())
        print(data.revenueTable())
        # print(data.cashflowTable())
