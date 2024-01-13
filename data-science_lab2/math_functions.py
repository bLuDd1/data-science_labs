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
    print('Регресійна модель:')
    print(f'y(t) =  {C[0,0]}  + {C[1,0]}  * t  +  {C[2,0]}  * t^2')
    return y_output


def MNK_Extrapol (S0, koef):
    iter = len(S0)
    Yout_Extrapol = np.zeros((iter+koef, 1))
    Yin = np.zeros((iter, 1))
    F = np.ones((iter, 3))
    for i in range(iter):
        Yin[i, 0] = float(S0[i])
        F[i, 1] = float(i)
        F[i, 2] = float(i * i)
    FT=F.T
    FFT = FT.dot(F)
    FFTI=np.linalg.inv(FFT)
    FFTIFT=FFTI.dot(FT)
    C=FFTIFT.dot(Yin)
    print('Регресійна модель:')
    print(f'y(t) =  {C[0,0]}  + {C[1,0]}  * t  +  {C[2,0]}  * t^2')
    for i in range(iter+koef):
        Yout_Extrapol[i, 0] = C[0, 0]+C[1, 0]*i+(C[2, 0]*i*i)
    return Yout_Extrapol


def print_MNK_characteristics(data, title):
    num_iterations = len(data)
    y_output = MNK(data)
    result_data = np.zeros((num_iterations))
    for i in range(num_iterations):
        result_data[i] = data[i] - y_output[i, 0]

    median = np.median(result_data)
    var = np.var(result_data)
    meanSquare = mt.sqrt(var)

    print(f'------------ {title} -------------')
    print(f'Мат. очікування = {median}')
    print(f'Дисперсія = {var}')
    print(f'Середньоквадратичне відхилення = {meanSquare}')

    return y_output


def print_predict_MNK_characteristics(koef, data, title):
    num_iterations = len(data)
    y_output = MNK(data)
    result_data = np.zeros((num_iterations))
    for i in range(num_iterations):
        result_data[i] = data[i] - y_output[i, 0]

    median = np.median(result_data)
    var = np.var(result_data)
    meanSquare = mt.sqrt(var)

    scvS_extrapol = meanSquare * koef
    print(f'------------ {title} -------------')
    print(f'Кількість елементів вибірки ={len(data)}')
    print(f'Мат. очікування = {median}')
    print(f'Дисперсія ={var}')
    print(f'Середньоквадратичне відхилення = {meanSquare}')
    print(f'Довірчий інтервал прогнозованих значень ={scvS_extrapol}')


def r2_score(SL, Yout, Text):
    iter = len(Yout)
    numerator = 0
    denominator_1 = 0
    for i in range(iter):
        numerator = numerator + (SL[i] - Yout[i, 0]) ** 2
        denominator_1 = denominator_1 + SL[i]
    denominator_2 = 0
    for i in range(iter):
        denominator_2 = denominator_2 + (SL[i] - (denominator_1 / iter)) ** 2
    R2_score_our = 1 - (numerator / denominator_2)
    print('------------', Text, '-------------')
    print('кількість елементів вибірки=', iter)
    print('Коефіцієнт детермінації (ймовірність апроксимації)=', R2_score_our)

    return R2_score_our