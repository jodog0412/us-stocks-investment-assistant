# USIA(US STOCK INVESTMENT ASSISTANT)
## Description
Python package for investment assistance.

## Reference
* __`yahooquery`__ https://yahooquery.dpguthrie.com/
* __`financewebreader`__ https://github.com/financedata-org/FinanceDataReader
* __`LTSF-Linear`__ https://github.com/cure-lab/LTSF-Linear   
(It is the model from the paper ["Are Transformers Effective for Time Series Forecasting?"](https://arxiv.org/abs/2205.13504, "arxiv"))

## Architecture
* main.py
* default
    * portfolio.py
    * tickerSearch.py
    * financialCompare.py
* predict  
    * dataProcess.py
    * dataset.py
    * model.py
    * train.py
    * main.py
* data
    * public.csv
    * nyse_tickers: tickers in NYSE index
    * nasdaq_tickers: tickers in NASDAQ index
    * sector_name.txt: name of sectors include stocks
## Functions
### 1. Analyze portfolio   
__Visualize__ your portfolio.  
And __calculate average yield__ of your portfolio's stocks.
* Code
    ```python
    import function
    start='2022-01-01'
    end='2023-03-19'
    function.portfolio('PRIVATE',start,end).implement()
    ```
* Result    
    <img src="https://user-images.githubusercontent.com/83653380/219939860-be0563d7-7ba3-4ec7-b6c8-f3c0191ef036.png" width="60%" height="45%" title="portfolio visualization"></img>  
    <img src="https://user-images.githubusercontent.com/83653380/219939955-9aa6e67f-f515-454c-ae9f-05f77f5039e1.png" width="40%" height="30%" title="portfolio yield"></img>


### 2. Search tickers    
__Search tickers__ in NYSE, NASDAQ index.   
And __calculate yield__ of searched stocks.
* Code    
    ```python
    searched=function.tickerSearch('NYSE','전기 유틸리티').download(start,end,filterPercent=0.2)
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

### 4. Predict prices(Alpha version)
>__This is alpha version, and the performance is unreliable.  
So, I recommend don't use this for practical investment.__  
  
Predict prices of your stock.    
I use `LTSF-Linear`, long time series prediction deep-learning model, for stock price prediction.    
`LTSF-Linear` is SOTA for long-time series forecast.
* Code
   ``` python    
   forecast_size=30
   window_size=forecast_size*2

   data=dataDownload('aapl','2y').returns()
   data=dataProcess(data).transform()
   train=data[:-window_size,0]
   train_dataset=windowDataset(train,window_size,forecast_size)
   train_loader=DataLoader(train_dataset,batch_size=4)
   pred=trainer(train,train_loader=train_loader,window_size=window_size,forecast_size=forecast_size).implement()
   data =dataProcess(data).inverse_transform()
   resultPlot(data=data,pred=pred,window_size=window_size,forecast_size=forecast_size).plot()
   ```  
* Result  
   * `dataDownload('AAPL','2y')`  
  <img src="https://user-images.githubusercontent.com/83653380/226164168-b196bff1-cc7f-4d21-8539-78c8d432bd28.png" width="80%" height="60%" title="Good sample"></img>     
   * `dataDownload('TSLA,'2y')`  
  <img src="https://user-images.githubusercontent.com/83653380/226164571-1f43b651-dd44-4bce-a7dc-373b9db68a6c.png" width="80%" height="60%" title="Bad sample"></img> 

