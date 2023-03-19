# -*- coding: utf-8 -*-
"""stock_investment_assistance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYIFPs0UYc8GgcN_SSXOALthaIk_eUEI

# 1. Environment&Import
"""

start='2022-01-01'
end='2023-03-19'

import function

# 1. Create portfolio from csv
function.portfolio('PRIVATE',start,end).implement()

# # 2. Search Tickers
# searched=function.tickerSearch('NASDAQ','전기 유틸리티').download(start,end,filterPercent=0.5)
# print(searched)

# 3. Compare Financials
# tickerDict={
    # 'SEARCH':searched.index,
    # 'WATCH':['CLFD','STEM','GOOG','ONTO','PERI','META','APD','CLH','DE','CWEN','CEG'],
    # 'SAMPLE':['AAPL','F','DIS','AMZN','KO','GOOG','XOM']
# }

# function.financialCompare(tickerDict,'WATCH').implement()

