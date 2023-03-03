from yahooquery import Ticker
import numpy as np
import pandas as pd
from tqdm import tqdm

class financialCompare:
    def __init__(self,tickerDict,command):
        self.tickerDict=tickerDict
        self.command=command
        self.tickers=tickerDict[command]
        self.qrTickers=Ticker(self.tickers, asynchronous=True)

    def keyFinancialTable(self):
        keyList=['PER','FPER','PBR','marketcap','freecashflow','PEGR','ROE','cRatio']
        financials=self.qrTickers.financial_data
        valuations=self.qrTickers.valuation_measures

        def financial(ticker,key):
            try: return financials[ticker][key]
            except (TypeError,KeyError): return np.nan

        def valuation(ticker,key):
            try: data=valuations.loc[ticker,key]
            except (AttributeError,KeyError): return np.nan
            else: 
                try: return data.dropna().values[-1]
                except IndexError: return np.nan
        #key로 valuation이 호출이 안될 때, valuation이 호출은 되나 nan일 때

        per=[valuation(i,'PeRatio') for i in self.tickers]
        fper=[valuation(i,'ForwardPeRatio') for i in self.tickers]
        pbr=[valuation(i,'PbRatio') for i in self.tickers]
        marketcap=[valuation(i,'MarketCap') for i in self.tickers]
        freecashflow=[financial(i,'freeCashflow') for i in self.tickers]
        # pcr=np.array(marketcap)/np.array(freecashflow)
        pegr=[valuation(i,'PegRatio') for i in self.tickers]
        roe=[financial(i,'returnOnEquity') for i in self.tickers]
        currentR=[financial(i,'currentRatio') for i in self.tickers]

        data=np.array([per,fper,pbr,marketcap,freecashflow,pegr,roe,currentR]).T
        result=pd.DataFrame(data=data,index=self.tickers,columns=keyList).sort_values(by='FPER',ascending=False)
        return result

    # def revenueGrowthTable(self):
    #     def getGrowth(ticker):
    #         data=ticker.earnings
    #         tickerGrowth=[(data.iloc[i+1,0]-data.iloc[i,0])/data.iloc[i,0]*100 for i in range(3)]
    #         return tickerGrowth
    #     tickersGrowth=[getGrowth(ticker) for ticker in tqdm(self.yfTickers)]
    #     result=pd.DataFrame(data=tickersGrowth,columns=self.tickers)
    #     return result

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
        print(data.keyFinancialTable())
        # print(data.revenueGrowthTable())
        # print(data.cashflowTable())
