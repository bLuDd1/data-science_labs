import numpy as np
import math as mt


def ABF (S0):
    iter = len(S0)
    Yin = np.zeros((iter, 1))
    YoutAB = np.zeros((iter, 1))
    T0=1
    for i in range(iter):
        Yin[i, 0] = float(S0[i])

    Yspeed_retro=(Yin[1, 0]-Yin[0, 0])/T0
    Yextra=Yin[0, 0]+Yspeed_retro
    alfa=2*(2*1-1)/(1*(1+1))
    beta=(6/1)*(1+1)
    YoutAB[0, 0]=Yin[0, 0]+alfa*(Yin[0, 0])

    for i in range(1, iter):
        YoutAB[i,0]=Yextra+alfa*(Yin[i, 0]- Yextra)
        Yspeed=Yspeed_retro+(beta/T0)*(Yin[i, 0]- Yextra)
        Yspeed_retro = Yspeed
        Yextra = YoutAB[i,0] + Yspeed_retro
        alfa = (2 * (2 * i - 1)) / (i * (i + 1))
        beta = 6 /(i* (i + 1))
    YoutAB[0] = S0[0]
    return YoutAB

def Sliding_Window_AV_Detect_sliding_wind (S0, n_Wind):
    iter = len(S0)
    j_Wind=mt.ceil(iter-n_Wind)+1
    S0_Wind=np.zeros((n_Wind))
    Midi = np.zeros(( iter))
    for j in range(j_Wind):
        for i in range(n_Wind):
            l=(j+i)
            S0_Wind[i] = S0[l]
        Midi[l] = np.median(S0_Wind)
    S0_Midi = np.zeros((iter))
    for j in range(iter):
        S0_Midi[j] = Midi[j]
    for j in range(n_Wind):
        S0_Midi[j] = S0[j]
    return S0_Midi