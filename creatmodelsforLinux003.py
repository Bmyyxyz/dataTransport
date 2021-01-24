# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:10:54 2021

@author: 15212
"""

import torch
import torch.nn as nn
import numpy as np
# import sys

# src = int(sys.argv[1])
# dst = int(sys.argv[2])

for i in range(2,5,2):
    for j in range(18,29,2):
        src = i
        dst = j
        # 构建输入集

        #x=np.loadtxt('/home/stack/code/pythontest/data.txt')
        x=np.loadtxt("/home/stack/code/pythontest/datafortrain/datafortrain("+str(src)+"-"+str(dst)+").txt")
        layer1 = len(x[0])
        x = torch.tensor(x).float()

        #y=np.loadtxt('/home/stack/code/pythontest/databinarypath001.txt')
        y=np.loadtxt("/home/stack/code/pythontest/answer("+str(src)+"-"+str(dst)+").txt")
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
        optimzer = torch.optim.SGD(myNet.parameters(), lr=0.0025)
        loss_func = nn.MSELoss()

        iterations = 300000
        for epoch in range(iterations):
            out = myNet(x)
            loss = loss_func(out, y)  # 计算误差
            if (epoch%10000==0):
                print(str(epoch)+"/"+str(iterations),"  loss: ",loss)
                #print("loss: ",loss)
            optimzer.zero_grad()  # 清除梯度
            loss.backward()
            optimzer.step()

        #torch.save(myNet,"/home/stack/code/pythontest/model(1-100).pth")
        torch.save(myNet,"/home/stack/code/testmodel/model("+str(src)+"-"+str(dst)+").pth")

        print("the model "+str(i)+"-"+str(j)+" have done!!!")

print("------------0,2,4 -->18-28 models have done!!!------------")

for i in range(0,5,2):
    for j in range(40,51,2):
        src = i
        dst = j
        # 构建输入集

        #x=np.loadtxt('/home/stack/code/pythontest/data.txt')
        x=np.loadtxt("/home/stack/code/pythontest/datafortrain/datafortrain("+str(src)+"-"+str(dst)+").txt")
        layer1 = len(x[0])
        x = torch.tensor(x).float()

        #y=np.loadtxt('/home/stack/code/pythontest/databinarypath001.txt')
        y=np.loadtxt("/home/stack/code/pythontest/answer("+str(src)+"-"+str(dst)+").txt")
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
        optimzer = torch.optim.SGD(myNet.parameters(), lr=0.0025)
        loss_func = nn.MSELoss()

        iterations = 300000
        for epoch in range(iterations):
            out = myNet(x)
            loss = loss_func(out, y)  # 计算误差
            if (epoch%10000==0):
                print(str(epoch)+"/"+str(iterations),"  loss: ",loss)
                #print("loss: ",loss)
            optimzer.zero_grad()  # 清除梯度
            loss.backward()
            optimzer.step()

        #torch.save(myNet,"/home/stack/code/pythontest/model(1-100).pth")
        torch.save(myNet,"/home/stack/code/testmodel/model("+str(src)+"-"+str(dst)+").pth")

        print("the model "+str(i)+"-"+str(j)+" have done!!!")

print("------------0,2,4 -->40-51 models have done!!!------------")

for i in range(6,11,2):
    for j in range(62,73,2):
        src = i
        dst = j
        # 构建输入集

        #x=np.loadtxt('/home/stack/code/pythontest/data.txt')
        x=np.loadtxt("/home/stack/code/pythontest/datafortrain/datafortrain("+str(src)+"-"+str(dst)+").txt")
        layer1 = len(x[0])
        x = torch.tensor(x).float()

        #y=np.loadtxt('/home/stack/code/pythontest/databinarypath001.txt')
        y=np.loadtxt("/home/stack/code/pythontest/answer("+str(src)+"-"+str(dst)+").txt")
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
        optimzer = torch.optim.SGD(myNet.parameters(), lr=0.0025)
        loss_func = nn.MSELoss()

        iterations = 300000
        for epoch in range(iterations):
            out = myNet(x)
            loss = loss_func(out, y)  # 计算误差
            if (epoch%10000==0):
                print(str(epoch)+"/"+str(iterations),"  loss: ",loss)
                #print("loss: ",loss)
            optimzer.zero_grad()  # 清除梯度
            loss.backward()
            optimzer.step()

        #torch.save(myNet,"/home/stack/code/pythontest/model(1-100).pth")
        torch.save(myNet,"/home/stack/code/testmodel/model("+str(src)+"-"+str(dst)+").pth")

        print("the model "+str(i)+"-"+str(j)+" have done!!!")

print("------------6,8,10 -->62-72 models have done!!!------------")
print("=====all done!!!=====all done!!!=====all done!!!=====all done!!!=====")