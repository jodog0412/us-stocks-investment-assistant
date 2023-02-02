import os.path
import numpy as np
import pandas as pd
import yfinance as yf
import FinanceDataReader as fdr

class indexSearch:
    def __init__(self):
        if os.path.isfile('nyse_tickers') and os.path.isfile('nasdaq_tickers'):
            self.nyse=pd.read_csv('nyse_tickers')
            self.ndq=pd.read_csv('nasdaq_tickers')
        else:
            self.nyse=fdr.StockListing('NYSE')
            self.ndq=fdr.StockListing('NASDAQ')

    def sectorList(self):
        sectors=list(set(self.nyse['Industry'].values))
        sectors=pd.Series(sectors).sort_values().values
        return sectors