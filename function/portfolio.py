import pandas as pd
import matplotlib.pyplot as plt
from yahooquery import Ticker

class portfolio:
    def __init__(self,command,start,end):
        self.command=command
        if command=='PRIVATE':
            data=pd.read_csv('./data/private.csv')
        elif command=='PUBLIC':
            data=pd.read_csv('./data/public.csv')
        data=data.sort_values(by="TICKER")
        self.portfolio=data
        self.start=start
        self.end=end

    def show(self):
        print(self.portfolio)
        data=self.portfolio.sort_values(by="STOCK_QUANTITY",ascending=False)
        plt.pie(data["STOCK_QUANTITY"],labels=data.loc[:,"TICKER"],autopct='%.1f%%',startangle=90)
        return(plt.show())
    
    def calcProfit(self,start,end):
        portfolio=self.portfolio
        buyPrice=portfolio.loc[:,'AVER_PRICE'].values
        tickers=portfolio.loc[:,"TICKER"].values
        stocknum=portfolio.loc[:,'STOCK_NUM'].values
        stockqnt=portfolio.loc[:,'STOCK_QUANTITY'].values
        def getPresentPrice(tickers):
            tickerQ=Ticker(tickers,asynchronous=True)
            histories=tickerQ.history(start=start,end=end)
            histories=list(histories['adjclose'].groupby('symbol'))
            history = [value for key,value in histories]
            func=lambda x:(x.values[-1]) #Get lastPrice from data
            prices=list(map(func,history))
            return prices
        PresentPrice=getPresentPrice(tickers)
        data=(PresentPrice/buyPrice-1)*100
        result=pd.Series(data=data,index=tickers).sort_values(ascending=False).dropna()
        total=sum(result.values)/len(result.index)
        total=stocknum.T@(PresentPrice-buyPrice)/sum(stockqnt)*100
        print("\n[Stock yield]")
        print(f'Total profit: {total:.2f}%')
        return(result)

    def implement(self):
        data=portfolio(self.command,self.start,self.end)
        data.show()
        print(data.calcProfit(self.start,self.end))