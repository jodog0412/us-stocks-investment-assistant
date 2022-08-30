# USIA(US STOCK INVESTMENT ASSISTANCE PROGRAM)
## DESCRIPTION
It is my personal investment assistance program for US stocks.

## FUNCTIONS
* **PORTFOLIO VISUALIZATION**
  * Visualize stock portfolio status
  * EXAMPLE : `portfolio_plt(pf)`
  \
  ![portfoilo1](https://user-images.githubusercontent.com/83653380/186848008-12e78dff-3d52-4d26-837f-b981860ef601.png)\
  ![portfolio2](https://user-images.githubusercontent.com/83653380/186848103-3bf93e9b-192a-4c64-92c3-29f8b90acc4c.png)

* **TICKER SEARCH**
  * Search tickers for specific sectors.
  \
  Tickers are sorted by rate of return, so you can find valuable stock easily.
  * EXAMPLE :`ticker_search('NASDAQ','재생에너지')`
  \
  ![ticker_search1](https://user-images.githubusercontent.com/83653380/186849115-9693fe96-b00b-4e14-ad2a-27aa4c9d30eb.png)


* **FINANCIALS COMPARISON**
  * Compare financials for multiple companies.
  * EXAMPLE : `financial_comparison(['AMZN','AAPL','KO','MSFT','GOOG','TSLA])`
  \
  ![financial_comparison](https://user-images.githubusercontent.com/83653380/186851180-f6fff4bb-7e8e-4307-9835-618f75ee24dd.png)

* **FINANCIALS VISUALIZATION**
  * Visualize earnings, balance and cashflow for multiple companies.
  * EXAMPLE : `plt_earning(['AAPL','MSFT'])`,`plt_balance(['AAPL','MSFT'])`,`plt_cashflow(['AAPL','MSFT'])`
  \
  ![financial_visualization1](https://user-images.githubusercontent.com/83653380/186852614-e304722e-a7cd-4b2b-8594-bb8508cae2cf.png)
  ![financial_visualization2](https://user-images.githubusercontent.com/83653380/186852900-ed944904-c0c0-4001-922b-7ecfac7fe241.png)
  ![financial_visualization3](https://user-images.githubusercontent.com/83653380/186853019-4435b669-23d4-4ebd-8cb2-1a863c01307f.png)

## IDEA
* **Advanced visualization for financials**
  * plotting pie graph for balance
* **Stock price prediction**
  * deep learning


