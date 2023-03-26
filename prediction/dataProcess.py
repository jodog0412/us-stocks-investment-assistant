from yahooquery import Ticker
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

class dataDownload():
    def __init__(self,ticker,period:str):
        data=Ticker(ticker).history(period=period)
        data=data.loc[:,'adjclose'].xs(ticker)
        self.date=list(data.index)
        self.data=data.to_numpy()

    def returns(self):
        plt.plot(self.data)
        plt.show()
        return self.date, self.data
    
class dataProcess():
    def __init__(self,data):
        self.data=data.reshape(-1,1)
    
    def transform(self):
        return scaler.fit_transform(self.data)

    def inverse_transform(self):
        return scaler.inverse_transform(self.data)[:,0]
    
class resultPlot():
    def __init__(self,date,data,pred,window_size,forecast_size):
        self.date=mdates.date2num(date)
        self.data=data
        self.len=data.shape[0]
        self.window_size=window_size
        self.forecast_size=forecast_size
        self.pred=pred

    def plot(self):
        len=self.len
        window_size=self.window_size
        forecast_size=self.forecast_size
        fig, ax = plt.subplots(figsize=(20,5))
        ax.plot(self.date[len-window_size:len],self.data[len-window_size:], label="Real")
        ax.plot(self.date[len-forecast_size:len], self.pred, label="LSTM-linear")
        locator = mdates.AutoDateLocator()
        formatter = mdates.AutoDateFormatter(locator)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        plt.legend()
        plt.show()
