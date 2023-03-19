from yahooquery import Ticker
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

class dataDownload():
    def __init__(self,ticker,period:str):
        data=Ticker(ticker).history(period=period)
        data=data.loc[:,'adjclose'].xs(ticker).to_numpy()
        self.data=data

    def returns(self):
        plt.plot(self.data)
        plt.show()
        return self.data
    
class dataProcess():
    def __init__(self,data):
        self.data=data.reshape(-1,1)
    
    def transform(self):
        return scaler.fit_transform(self.data)

    def inverse_transform(self):
        return scaler.inverse_transform(self.data)[:,0]
    
class resultPlot():
    def __init__(self,data,pred,window_size,forecast_size):
        self.data=data
        self.len=data.shape[0]
        self.window_size=window_size
        self.forecast_size=forecast_size
        self.pred=pred

    def plot(self):
        len=self.len
        window_size=self.window_size
        forecast_size=self.forecast_size
        plt.figure(figsize=(20,5))
        plt.plot(range(len-window_size,len),self.data[len-window_size:], label="Real")
        plt.plot(range(len-forecast_size,len), self.pred, label="LSTM-linear")
        plt.legend()
        plt.show()
