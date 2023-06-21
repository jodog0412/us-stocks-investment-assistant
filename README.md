# USIA(US STOCK INVESTMENT ASSISTANT)
## Description
Python package for investment assistance.  

## Reference
* __`yahooquery`__ API for yahoo finance  https://yahooquery.dpguthrie.com/
* __`financewebreader`__ https://github.com/financedata-org/FinanceDataReader

## Architecture
* main.py
* usia
    * portfolio.py
    * ticker_serach.py
    * financial_statement.py
* data
    * nyse_tickers: tickers in NYSE index
    * nasdaq_tickers: tickers in NASDAQ index
    * sector_name.txt: name of sectors include stocks
## Functions
### 1. Analyze portfolio   
__Visualize__ your portfolio.  
And __calculate average yield__ of your portfolio's stocks.
* Code
    ```python
    import usia
    start='2023-01-01'
    end='2023-06-20'
      
    """1. Create portfolio from csv"""
    path="data\public.csv"
    portfoilo=usia.portfolio(path,start,end)
    portfoilo.implement()
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/219939860-be0563d7-7ba3-4ec7-b6c8-f3c0191ef036.png" width="60%" height="45%" title="portfolio visualization"></img>  
    <img src="https://user-images.githubusercontent.com/83653380/219939955-9aa6e67f-f515-454c-ae9f-05f77f5039e1.png" width="40%" height="30%" title="portfolio yield"></img>


### 2. Search tickers    
__Search tickers__ in NYSE, NASDAQ index.   
And __calculate yield__ of searched stocks.
* Code    
    ```python
    searched=usia.tickerSearch('NASDAQ','헬스케어 장비 및 용품').download(start,end,filter_percent=0.5)
    print(searched)
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/226162455-b1c6377a-2636-4d91-8099-07d7bc7f9d95.png" width="20%" height="10%" title="tickerSearch"></img>

### 3. Compare financials  
Compare Key financials.  
I selected `PER`, `Forward PER`, `PBR`, `marketcap`, `freecashflow`, `PEGR`, `ROE`, `currentRatio` as default financial indicators.
* Code
    ```python
    tickerDict={
    'SEARCH':searched.index,
    'SAMPLE':['AAPL','F','DIS','AMZN','KO','GOOG','XOM']
    }
    function.financialCompare(tickerDict,'SAMPLE').implement()
    ```
* Result  
    <img src="https://user-images.githubusercontent.com/83653380/226162696-81c0ffde-179c-42a4-9928-42cd1080d7b3.png" width="60%" height="45%" title="keyFinancial"></img>    
    <img src="https://user-images.githubusercontent.com/83653380/216546823-697aa88c-0cbf-4471-9f88-763d7d313612.png" width="60%" height="45%" title="revenueGrowth" alt="RubberDuck"></img>     
    <img src="https://user-images.githubusercontent.com/83653380/216546281-81f723c3-1606-48da-9a23-e05548eca4ce.png" width="60%" height="45%" title="cashflow" alt="RubberDuck"></img>     


