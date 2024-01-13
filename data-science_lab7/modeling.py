import numpy as np
from matplotlib import pyplot as plt
import math as mt


def MNK (Y_coord, show_model = False):
    iter = len(Y_coord)
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 5))

    for i in range(iter):
        Yin[i, 0] = Y_coord[i]
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
        F[i, 3] = float(i * i * i)
        F[i, 4] = float(i * i * i * i)

    FT=F.T
    FFT = FT.dot(F)
    FFTI=np.linalg.inv(FFT)
    FFTIFT=FFTI.dot(FT)
    C=FFTIFT.dot(Yin)
    Yout=F.dot(C)
    if(show_model):
        print('Модель прибутку:')
        print('y(t) = ', C[0, 0], ' + ', C[1, 0], ' * t', ' + ', C[2, 0], ' * t^2', ' + ', C[3, 0], ' * t^3', ' + ', C[4, 0], ' * t^4')
    return Yout


def Stat_characteristics (SL, Text):
    Yout = MNK(SL)
    iter = len(Yout)
    SL0 = np.zeros((iter ))
    for i in range(iter):
        SL0[i] = SL[i] - Yout[i, 0]
    mS = np.median(SL0)
    dS = np.var(SL0)
    scvS = mt.sqrt(dS)
    print(f'------------ {Text} -------------')
    print(f'Мат. очікуання = {mS}')
    print(f'Дисперсія = {dS}')
    print(f'Середньоквадратичне відхилення = {scvS}')
    print('-----------------------------------------------------')
    plt.title(Text)
    plt.hist(SL,  bins=40, facecolor="blue", alpha=0.5)
    plt.show()
    return
