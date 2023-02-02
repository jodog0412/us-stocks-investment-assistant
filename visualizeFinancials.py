import yfinance as yf
import numpy as np
import pandas as pd
from tqdm import tqdm
def revenueGrowthTable(tickers):
    revDict={}
    for ticker in tqdm(tickers):
        data=yf.Ticker(ticker).earnings
        revGrowth=[(data.iloc[i+1,0]-data.iloc[i,0])/data.iloc[i,0]*100 for i in range(3)]
        revDict[ticker]=revGrowth
    result=pd.DataFrame(data=revDict)
    return result

def cashflowTable(tickers):
    flowDict={}
    for ticker in tqdm(tickers):
        balance=yf.Ticker(ticker).cashflow.loc[['Operating Cash Flow','Financing Cash Flow','Investing Cash Flow']]
        balance.index=['Operating','Financing','Investing']
        balance=balance.transpose().sort_index()
        flowDict[ticker]=balance
    return flowDict