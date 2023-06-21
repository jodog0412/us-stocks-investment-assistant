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
  | Name | Profit Pencentage(%) |
  | ---- | -------------------- |
  | AAPL |    52.88             |
  | F    |    24.96             |
  | XOM  |    16.06             |
  | AMZN |    10.99             |
  | GOOG |    5.80              |
  | KO   |   -1.91              |
  | DIS  |   -10.51             |


### 2. Search tickers    
__Search tickers__ in NYSE, NASDAQ index.   
And __calculate yield__ of searched stocks.
* Code    
    ```python
    searched=usia.tickerSearch('NASDAQ','헬스케어 장비 및 용품').download(start,end,filter_percent=0.1)
    print(searched)
    ```
* Result    
  | Ticker | Profit               |
  | ------ | -------------------- |
  | NPCE   |    2.26              |
  | BSGM   |    2.02              |
  | APYX   |    1.76              |
  | NNOX   |    1.70              |
  | NSPR   |    1.59              |
  ...
### 3. Compare financials  
Compare Key financials.  
I selected `PER`, `Forward PER`, `PBR`, `marketcap`, `freecashflow`, `PEGR`, `ROE`, `currentRatio` as default financial indicators.
* Code
    ```python
    sample=['AAPL','F','DIS','AMZN','KO','GOOG','XOM']
    result=usia.financialCompare(sample).keyFinancialTable()
    print(result)
    ```
* Result
  | Ticker |  PER   |  FPER  | PBR |  marketcap   | freecashflow | PEGR | ROE  | cRatio |
  | ------ | ------ | ------ | --- | ------------ | ------------ | ---- | ---- | ------ |
  | AMZN   | 299.48 |  71.43 | NaN | 1.290547e+12 | 9.030625e+09 | 4.47 | 0.03 |  0.92  |
  | AAPL   | 31.36  |  28.01 | NaN | 2.909967e+12 | 8.379662e+10 | 2.54 | 1.46 |  0.94  |
  | KO     | 26.99  |  23.58 | NaN | 2.649237e+11 | 9.134250e+09 | 3.34 | 0.37 |  1.15  |
  | GOOG   | 27.52  |  23.09 | NaN | 1.567406e+12 | 5.586262e+10 | 1.54 | 0.23 |  2.35  |
  | DIS    | 39.89  |  15.75 | NaN | 1.640006e+11 | 5.236875e+09 | 0.74 | 0.04 |  1.01  |
  | F      | 19.48  |  8.57  | NaN | 5.689095e+10 | 2.655875e+09 | 1.01 | 0.06 |  1.20  |


