import numpy as np
import matplotlib.pyplot as plt
import math as mt


def Plot_AV (S0_L, SV_L, Text):
    plt.plot(SV_L)
    plt.plot(S0_L)
    plt.ylabel(Text)
    plt.show()
    return


def MNK (S0):
    iter = len(S0)
    Yout = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):
        Yout[i, 0] = float(S0[i])
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT = F.T
    FFT = FT.dot(F)
    FFTI = np.linalg.inv(FFT)
    FFTIFT = FFTI.dot(FT)
    C = FFTIFT.dot(Yout)
    y_output = F.dot(C)
    a, b, c = C[2,0], C[1,0], C[0,0]
    print('Регресійна модель:')
    print(f'y(t) =  {C[0,0]}  + {C[1,0]}  * t  +  {C[2,0]}  * t^2')
    return y_output, a, b, c


def print_MNK_characteristics(data, title):
    num_iterations = len(data)
    y_output, a, b, c = MNK(data)
    result_data = np.zeros((num_iterations))
    for i in range(num_iterations):
        result_data[i] = data[i] - y_output[i, 0]

    median = np.median(result_data)
    var = np.var(result_data)
    meanSquare = mt.sqrt(var)

    print(f'------------ {title} -------------')
    print(f'Мат. очікуання = {median}')
    print(f'Дисперсія = {var}')
    print(f'Середньоквадратичне відхилення = {meanSquare}')

    return meanSquare, median, var, a, b, c

def get_normal_model(loc, scale, n):
    return np.random.normal(loc, scale, n)


def get_square_model(n, a, b, c):
    S = np.zeros((n))

    koeffs = [c, b, a]
    for i in range(n):
        for index, koef in enumerate(koeffs):
            S[i] += koef*(i**index)
    return S