# USIA(US STOCK INVESTMENT ASSISTANCE PROGRAM)
## DESCRIPTION
It is my personal investment assistance program for US stocks.

## LIBRARY
* yfinance 0.1.74 https://github.com/ranaroussi/yfinance
* financewebreader https://github.com/financedata-org/FinanceDataReader

## FUNCTIONS
* **Create portfolio**  
    
  **`portfolio(sheet)`**         
  ![portfoilo1](https://user-images.githubusercontent.com/83653380/186848008-12e78dff-3d52-4d26-837f-b981860ef601.png)    
  **`portfolio(sheet).plot()`**        
  ![portfolio2](https://user-images.githubusercontent.com/83653380/186848103-3bf93e9b-192a-4c64-92c3-29f8b90acc4c.png)

* **Search tickers**    
  **`tickerSearch('NASDAQ','소프트웨어 및 IT서비스').download()`**        
      
  ![ticker_search](https://user-images.githubusercontent.com/83653380/200852813-6c5e2024-7d1b-4d31-bcee-3be5e5a18c68.png)    
* **Compare financials**    
  **`financial_comparison(['AMZN','AAPL','KO','MSFT','GOOG','TSLA])`**        
  ![FINANCIALS COMPARISON](https://user-images.githubusercontent.com/83653380/200853675-58b95519-4fab-454e-8cff-471d10db3bdf.png)

  

* **FINANCIALS VISUALIZATION**
  * Visualize earnings, balance and cashflow for multiple companies.
  * EXAMPLE : `plt_earning(['AAPL','MSFT'])`,`plt_balance(['AAPL','MSFT'])`,`plt_cashflow(['AAPL','MSFT'])`    
  ![financial_visualization1](https://user-images.githubusercontent.com/83653380/186852614-e304722e-a7cd-4b2b-8594-bb8508cae2cf.png)
  ![financial_visualization2](https://user-images.githubusercontent.com/83653380/186852900-ed944904-c0c0-4001-922b-7ecfac7fe241.png)
  ![financial_visualization3](https://user-images.githubusercontent.com/83653380/186853019-4435b669-23d4-4ebd-8cb2-1a863c01307f.png)

## IDEA
* **Advanced visualization for financials**
  * plotting pie graph for balance
* **Stock price prediction**
  * deep learning


