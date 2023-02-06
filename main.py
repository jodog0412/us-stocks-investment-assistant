# -*- coding: utf-8 -*-
"""stock_investment_assistance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYIFPs0UYc8GgcN_SSXOALthaIk_eUEI

# 1. Environment&Import
"""
import numpy as np
import pandas as pd
import yfinance as yf
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from tqdm import tqdm

startdate='2022-01-01'
enddate='2023-02-04'

from portfolio import portfolio
from tickerSearch import tickerSearch
from financialCompare import financialCompare

# 1. Create portfolio from csv
# portfolio('PUBLIC').implement(startdate,enddate)

# 2. Search Tickers
searched=tickerSearch('NASDAQ','제약').download(0.1)
print(searched)

# 3. Compare Financials
tickerDict={
    'SEARCH':searched.index,
    'WATCH':['CLFD','STEM','GOOG','EQNR','ON','ONTO','FLEX','PERI','META','IMKTA','CALM','CLH','CRAI','ASRT']
}

financialCompare(tickerDict,'WATCH').implement()
