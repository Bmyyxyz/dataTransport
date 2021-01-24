# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:10:54 2021

@author: 15212
"""

import torch
import torch.nn as nn
import numpy as np


# 构建输入集

#x=np.loadtxt('/home/stack/code/pythontest/data.txt')
x=np.loadtxt("/home/stack/code/pythontest/datafortrain/datafortrain(0-18)test.txt")
layer1 = len(x[0])
x = torch.tensor(x).float()

#y=np.loadtxt('/home/stack/code/pythontest/databinarypath001.txt')
y=np.loadtxt("/home/stack/code/pythontest/answer(0-18).txt")
#layer4 = len(y[0])
y = torch.tensor(y).float()


# 搭建网络
myNet = nn.Sequential(
    nn.Linear(layer1, 10),
    nn.ReLU(),
    nn.Linear(10, 8),
    nn.ReLU(),
    nn.Linear(8, 5),
    nn.ReLU(),
    nn.Linear(5,3),
    nn.Sigmoid()
)
print(myNet)

# 设置优化器
optimzer = torch.optim.SGD(myNet.parameters(), lr=0.003)
loss_func = nn.MSELoss()

iterations = 500000
for epoch in range(iterations):
    out = myNet(x)
    loss = loss_func(out, y)  # 计算误差
    if (epoch%1000==0):
        print(str(epoch)+"/"+str(iterations),"loss: ",loss)
        #print("loss: ",loss)
    optimzer.zero_grad()  # 清除梯度
    loss.backward()
    optimzer.step()
    
#torch.save(myNet,"/home/stack/code/pythontest/model(1-100).pth")
torch.save(myNet,"/home/stack/code/testmodel/test0001(0-18)-"+str(layer1)+"in"+str(3)+"out"+".pth")

print("done!!!")
