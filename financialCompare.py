import yfinance as yf
import pandas as pd
from tqdm import tqdm

def financialCompare(tickerDict, command):
    if command=='SEARCH':
        tickers=tickerDict['SEARCH']
    else:
        tickers=tickerDict['WATCH']

    def getFinancial(ticker):
        def return_(info, key):
            try: return info[key]
            except KeyError: return "NaN"
        info=yf.Ticker(ticker).info
        infoCustom=[return_(info,"trailingPE"), return_(info,"forwardPE"), return_(info,"priceToBook"),
                    return_(info,"pegRatio"), return_(info,"returnOnEquity"),return_(info,"shortPercentOfFloat"),
                    return_(info,"quickRatio")]
        return infoCustom

    financial=[getFinancial(ticker) for ticker in tqdm(tickers)]
    df=pd.DataFrame(data=financial,
                    index=tickers,
                    columns=['PER', 'FPER', 'PBR',
                             'PEGR', 'ROE', 'short%', 'qRatio'])
    df=df.sort_values('FPER',ascending=False)
    return df