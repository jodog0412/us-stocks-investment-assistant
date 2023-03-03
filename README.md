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
    portfolio('PUBLIC').implement(startdate,enddate)
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/219939860-be0563d7-7ba3-4ec7-b6c8-f3c0191ef036.png" width="60%" height="45%" title="portfolio visualization"></img>  
    <img src="https://user-images.githubusercontent.com/83653380/219939955-9aa6e67f-f515-454c-ae9f-05f77f5039e1.png" width="40%" height="30%" title="portfolio yield"></img>


### 2. Search tickers    
__`Search tickers`__ in NYSE, NASDAQ index. And __`calculate yield`__ of searched stocks.
* Code    
    ```python
    searched=tickerSearch('NASDAQ','제약').download(filterPercent=0.1)
    print(searched)
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/219940122-cb28f1fc-b7a8-4b63-b872-e76b55f9befa.png" width="40%" height="30%" title="tickerSearch"></img>

### 3. Compare financials    
* Code
    ```python
    tickerDict={
    'SEARCH':searched.index,
    'SAMPLE':['AAPL','F','DIS','AMZN','KO','GOOG','XOM']
    }
    financialCompare(tickerDict,'SAMPLE').implement()
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/216545817-d34b8c51-4da2-4277-adf5-d3482781ca05.png" width="60%" height="45%" title="keyFinancial" alt="RubberDuck"></img>    
    <img src="https://user-images.githubusercontent.com/83653380/216546823-697aa88c-0cbf-4471-9f88-763d7d313612.png" width="60%" height="45%" title="revenueGrowth" alt="RubberDuck"></img>     
    <img src="https://user-images.githubusercontent.com/83653380/216546281-81f723c3-1606-48da-9a23-e05548eca4ce.png" width="60%" height="45%" title="cashflow" alt="RubberDuck"></img>     




