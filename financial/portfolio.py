import pandas as pd
import matplotlib.pyplot as plt
from yahooquery import Ticker

def get_present_price(tickers,start,end):
            yticker=Ticker(tickers,asynchronous=True)
            histories=list(yticker.history(start=start,end=end)['adjclose'].groupby('symbol'))
            history = [value for key,value in histories]
            func=lambda x:(x.values[-1]) #Get lastPrice from data
            prices=list(map(func,history))
            return prices

class portfolio:
    def __init__(self,command:str,start:str,end:str):
        self.command=command
        self.start=start
        self.end=end
        if command=='PRIVATE':
            data=pd.read_csv('./data/private.csv')
        elif command=='PUBLIC':
            data=pd.read_csv('./data/public.csv')
        else: raise Exception("Wrong command Input. Command must be 'PRIVATE' OR 'PUBLIC'.")
        data=data.sort_values(by="TICKER")
        self.portfolio=data
        self.buyprice=data.loc[:,'AVER_PRICE'].values
        self.tickers=data.loc[:,'TICKER'].values
        self.stocknum=data.loc[:,'STOCK_NUM'].values
        self.stockqnt=data.loc[:,'STOCK_QUANTITY'].values

    def figureplot(self):
        print(self.portfolio)
        data=self.portfolio.sort_values(by="STOCK_QUANTITY",ascending=False)
        plt.pie(data["STOCK_QUANTITY"],labels=data.loc[:,"TICKER"],autopct='%.1f%%',startangle=90)
        return(plt.show())
    
    def profit_calc(self):
        buyPrice=self.buyprice
        tickers=self.tickers
        stocknum=self.stocknum
        stockqnt=self.stockqnt
        PresentPrice=get_present_price(tickers,self.start,self.end)
        profit=(PresentPrice/buyPrice-1)*100
        each=pd.Series(data=profit,index=tickers).sort_values(ascending=False).dropna()
        total=stocknum.T@(PresentPrice-buyPrice)/sum(stockqnt)*100
        return(each, total)
    
    def implement(self):
        data=portfolio(self.command,self.start,self.end)
        data.figureplot()
        each, total=data.profit_calc()
        print(f"\n[Stock yield]\nTotal Profit: {total:.2f}%\n")
        print(each)