import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

startdate='2022-01-01'
enddate='2023-01-01'

class portfolio:
    def __init__(self):
        data=pd.read_csv('sheet1.csv')
        data=data.sort_values(by="TICKER")
        self.pf=data

    def plot(self):
        data=self.pf.sort_values(by="STOCK_QUANTITY",ascending=False)
        pf_plt=plt.pie(data["STOCK_QUANTITY"],labels=data.loc[:,"TICKER"],
                       autopct='%.1f%%',startangle=90)
        return(plt.show())
    
    def calcProfit(self,start=startdate,end=enddate):
        ticker=self.pf.loc[:,"TICKER"].values
        data=yf.download(list(ticker),start=start,end=end,progress=False)
        lastPrice=data['Adj Close'].iloc[-1]
        averPrice=(self.pf)['AVER_PRICE'].values.astype(float)
        profit=(lastPrice/averPrice-1)*100
        profit=profit.sort_values(ascending=False)
        totalProfit=sum(profit.values)/len(profit.index)
        print("\n[Stock yield]")
        print(f'Total profit: {totalProfit:.2f}%')
        return(profit)

    def implement(self,startdate=startdate,enddate=enddate):
        result=portfolio()
        print(result.pf)
        result.plot()
        print(result.calcProfit(startdate,enddate))