
from dataProcess import *
from dataset import windowDataset
from torch.utils.data import DataLoader
from trainer import *
forecast_size=30
window_size=forecast_size*3

data=dataDownload('tsla','2y').returns()
data=dataProcess(data).transform()
train=data[:-window_size,0]
train_dataset=windowDataset(train,window_size,forecast_size)
train_loader=DataLoader(train_dataset,batch_size=4)
pred=trainer(train,train_loader=train_loader,window_size=window_size,forecast_size=forecast_size).implement()
data =dataProcess(data).inverse_transform()
resultPlot(data=data,pred=pred,window_size=window_size,forecast_size=forecast_size).plot()