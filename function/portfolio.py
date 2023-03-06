startdate='2022-01-01'
enddate='2023-03-06'
import pandas as pd
import matplotlib.pyplot as plt
from yahooquery import Ticker

class portfolio:
    def __init__(self,command):
        self.command=command
        if command=='PRIVATE':
            data=pd.read_csv('./data/private.csv')
        elif command=='PUBLIC':
            data=pd.read_csv('./data/public.csv')
        data=data.sort_values(by="TICKER")
        self.pf=data

    def show(self):
        print(self.pf)
        data=self.pf.sort_values(by="STOCK_QUANTITY",ascending=False)
        plt.pie(data["STOCK_QUANTITY"],labels=data.loc[:,"TICKER"],autopct='%.1f%%',startangle=90)
        return(plt.show())
    
    def calcProfit(self,start=startdate,end=enddate):
        portfolio=self.pf
        buyPrice=portfolio.loc[:,'AVER_PRICE'].values
        tickers=portfolio.loc[:,"TICKER"].values
        tickerQ=Ticker(tickers,asynchronous=True)
        history=tickerQ.history(start=startdate,end=enddate)
        history=list(history['adjclose'].groupby('symbol'))
        values = [value for key,value in history]
        func=lambda x:(x.values[-1]) #Get lastPrice from data
        lastPrice=list(map(func,values))
        data=(lastPrice/buyPrice-1)*100
        result=pd.Series(data=data,index=tickers).sort_values(ascending=False).dropna()
        total=sum(result.values)/len(result.index)
        print("\n[Stock yield]")
        print(f'Total profit: {total:.2f}%')
        return(result)

    def implement(self,startdate=startdate,enddate=enddate):
        data=portfolio(self.command)
        data.show()
        print(data.calcProfit(startdate,enddate))