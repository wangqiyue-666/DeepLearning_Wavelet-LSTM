# encoding: utf-8 
import pywt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy import signal


#--读取数据--
def ReadFile(filename):
    #filename = 'data.txt' 
    data = []
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline() # 整行读取数据
            if not lines:
                break
                pass
            # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            p_tmp = lines.split() 
            data.append(p_tmp[0])  # 添加新读取的数据
            pass
    #print(data)
    return data

#--连续小波变换 cwt --
def MyCWT(data):    
    #--原始数据初始化--
    # x = np.arange(len(data))
    # y = data

    # Fs = 500000 #采样频率：500 000 Hz 
    #             #采样周期：2 us
    # #--尺度计算--
    # wavename = 'gaus1'
    # totalscal = 64;    #尺度序列的长度
    
    # #Fc = 2000;          #小波中心频率(Hz)（“主波峰之间的差值”=2000Hz）
    #                     #Fc = pywt.central_frequency(wavename, precision=8) 
    # Fc = pywt.central_frequency(wavename)               
                   
    # C = 2*Fc*totalscal; # C 为常数，C = 2*Fc/totalscal
    # scal= C/np.arange(1,totalscal+1);   #尺度序列,范围（2*Fc,inf）

    # #--连续小波变换--
    # # coef,freqs = pywt.cwt(y,scal,wavename)
    
    # # return coef ,freqs
    # data = map(float,data)
    # data1  = map(lambda x: float(x),data)
    data1 = np.ones(len(data),np.float)  
    for i in range(0,len(data)): data1[i] = float(data[i])

    widths = np.arange(1, 31)
    
    cwtmatr =  signal.cwt(data1, signal.ricker, widths)
    return cwtmatr

    
def ShowCoef(coef):

    #from mpl_toolkits.mplot3d import Axes3D
    #ax = Axes3D(fig)
        
    # fig = plt.figure()

    #--时频(尺度)度--
    # plt.matshow( coef )
    #f = pywt.scale2frequency(wavename,scal,precision=8); #将尺度转换为频率
    #print(f);
    
    #三维图
    # x = []
    # y = []
    # z = []
    
    # for i in range(0,len(coef)):
    #     for j in range(0,len(coef[i])):
    #         x.append(i)
    #         y.append(j)
    #         z.append(coef[i][j])
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_trisurf(x, y, z)
    
    # plt.show()

    fig = plt.figure()
    ax = Axes3D(fig)
    
    data = coef

    stepX = 1  # 采样步长 X
    stepY = 10 # 采样步长 Y
    
    X = range(0, len(data), stepX)
    Y = range(0, len(data[0]), stepY)
    ZZ = np.zeros([len(X), len(Y)])

    YY, XX = np.meshgrid(Y, X)
    # print(XX)
    # print(YY)
    # print(ZZ)
    
    # print(printData)
    for i in range(0, len(X)):
        for j in range(0, len(Y)):
            ZZ[i][j] = data[ X[i] ][ Y[j] ]
    # R = np.sqrt(X**2 + Y**2)
    # Z = np.sin(R)
    # print(ZZ)


    # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    ax.plot_surface(XX, YY, ZZ, rstride=1, cstride=1, cmap='rainbow')

    plt.show()


if __name__=="__main__":
    data = ReadFile('data.txt')
    coef = MyCWT(data)
    ShowCoef(coef)
    
    
    
    
    
    