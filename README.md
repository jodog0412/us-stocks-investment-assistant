# USIA(US STOCK INVESTMENT ASSISTANCE PROGRAM)
## Description
It is an investment assistance program for US stocks.

## Reference
* __`yfinance`__ https://github.com/ranaroussi/yfinance
* __`financewebreader`__ https://github.com/financedata-org/FinanceDataReader

## Component
* library
    * portfolio
    * indexSearch
    * tickerSearch
    * financialCompare
* data
    * public.csv
    * nyse_tickers: tickers in NYSE index
    * nasdaq_tickers: tickers in NASDAQ index
    * sector_name.txt: name of sectors include stocks
## Functions
### 1. Analyze portfolio    
__`Analyze and visualize portfolio`__ (your portfoliio data(.csv) should be located in the same folder with __`main.py`.__)     
* Code
    ```python
    portfolio_=portfolio()
    portfolio_.plot()
    portfolio_.calcProfit()
    print(portfolio_.pf)
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/186848103-3bf93e9b-192a-4c64-92c3-29f8b90acc4c.png" width="40%" height="30%" title="portfolio(sheet).plot()" alt="RubberDuck"></img>    
    <img src="https://user-images.githubusercontent.com/83653380/186848008-12e78dff-3d52-4d26-837f-b981860ef601.png" width="40%" height="30%" title="print(portfolio_.pf)" alt="RubberDuck"></img>    

### 2. Search tickers    
__`Search tickers`__ in NYSE, NASDAQ index. And __`calculate yield`__ of searched stocks.
* Code    
    ```python
    tickerInit=tickerSearch('NYSE','커뮤니케이션 및 네트워킹')
    tickerSearched=tickerSearch.download(tickerInit,0.3)
    print(tickerSearched)
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/216543150-71ffa6c7-b52c-49b4-a191-b9b83d5b0c94.png" width="20%" height="15%" title="tickerSearch" alt="RubberDuck"></img> 

### 3. Compare financials    
* Code
    ```python
    print(keyFinancialTable(tickerDict,'SEARCH'))
    print(revenueGrowthTable(tickerDict['SEARCH']))
    print(cashflowTable(tickerDict['SEARCH']))
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/216545817-d34b8c51-4da2-4277-adf5-d3482781ca05.png" width="60%" height="45%" title="keyFinancial" alt="RubberDuck"></img>    
    <img src="https://user-images.githubusercontent.com/83653380/216546823-697aa88c-0cbf-4471-9f88-763d7d313612.png" width="60%" height="45%" title="revenueGrowth" alt="RubberDuck"></img>     
    <img src="https://user-images.githubusercontent.com/83653380/216546281-81f723c3-1606-48da-9a23-e05548eca4ce.png" width="60%" height="45%" title="cashflow" alt="RubberDuck"></img>     




