import torch
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm
import matplotlib.pyplot as plt

from model import Dlinear,Nlinear
from dataProcess import dataProcess
class trainer():
    def __init__(self, train, train_loader, window_size, forecast_size, command="D", feature_size=4, lr=1e-4):
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.criterion=nn.MSELoss()
        self.trainRaw=train
        self.train_loader=train_loader
        if command=="D":
            self.model=Dlinear(window_size,forecast_size).to(self.device)
        else:
            self.model=Nlinear(window_size,forecast_size).to(self.device)
        self.window_size=window_size
        self.forecast_size=forecast_size
        self.feature_size=feature_size
        self.command=command
        self.optimizer=torch.optim.Adam(self.model.parameters(),lr=lr)

    def train(self, epoch=50):
        self.model.train()
        progress=tqdm(range(epoch))
        losses=[]
        for i in progress:
            batchloss = 0.0
            for (inputs, outputs) in self.train_loader:
                self.optimizer.zero_grad()
                result = self.model(inputs.float().to(self.device))
                loss = self.criterion(result, outputs.float().to(self.device))
                loss.backward()
                self.optimizer.step()
                batchloss += loss
            losses.append(batchloss.cpu().item())
            progress.set_description("loss: {:0.6f}".format(batchloss.cpu().item() / len(self.train_loader)))
        plt.plot(losses)

    def evaluate(self):
        window_size=self.window_size
        input = torch.tensor(self.trainRaw[-window_size:]).reshape(1,-1,1).float().to(self.device)
        self.model.eval()
        predictions = self.model(input)
        return predictions.detach().cpu().numpy()
    
    def implement(self):
        process=trainer(self.trainRaw,self.train_loader,self.window_size,
                        self.forecast_size,self.feature_size,self.command)
        process.train()
        evaluate=process.evaluate()
        result=dataProcess(evaluate).inverse_transform()
        return result
