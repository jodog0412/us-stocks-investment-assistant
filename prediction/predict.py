
from torch.utils.data import DataLoader
from dataProcess import *
from dataset import *
from trainer import *

def implement(ticker:str,period:str,window_size:int,forecast_size:int):
    date, data=dataDownload(ticker,period).returns()
    data=dataProcess(data).transform()
    train=data[:-window_size,0]
    train_dataset=windowDataset(train,window_size,forecast_size)
    train_loader=DataLoader(train_dataset,batch_size=4)
    pred=trainer(train,train_loader,window_size,forecast_size).implement()
    data =dataProcess(data).inverse_transform()
    resultPlot(date,data,pred,window_size,forecast_size).plot()

implement('aapl','2y',90,30)