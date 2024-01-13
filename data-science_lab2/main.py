import math as mt
from data_parsing import parsing_site, file_parsing
from math_functions import Plot_AV, print_MNK_characteristics, print_predict_MNK_characteristics, MNK_Extrapol, r2_score
from data_manipulating import ABF, Sliding_Window_AV_Detect_sliding_wind


if __name__ == '__main__':
    n = 10000
    n_Wind = 3
    extrapolation_koef = 0.5

    print('Обрано: Парсинг табличних даних https://index.minfin.com.ua/ua/exchange/nbu/bullion/xau/')
    url = "https://index.minfin.com.ua/ua/exchange/nbu/bullion/xau/"
    parsing_site(url)

    data_array = file_parsing(url, 'hrn-to-gold.xlsx', 'Курс (грн.)')
    print_MNK_characteristics(data_array, 'Коливання ціни золота')
    Plot_AV(data_array, data_array, 'Коливання ціни золота')

    smoothed = Sliding_Window_AV_Detect_sliding_wind(data_array, n_Wind)
    Plot_AV(smoothed, smoothed, 'Очищена вибірка')

    info = print_MNK_characteristics(smoothed, 'Очищена вибірка')
    Plot_AV(info, smoothed, 'Модель')
    r2_score(smoothed, info, 'Модель')

    koef = mt.ceil(len(smoothed)*extrapolation_koef)
    predicted = MNK_Extrapol(smoothed, koef)
    Plot_AV(predicted, smoothed, 'Прогнозована')
    print_predict_MNK_characteristics(koef, predicted, 'Прогнозована')

    abf = ABF(smoothed)
    r2_score(smoothed, abf, 'ABF')
    Plot_AV(abf, smoothed, 'ABF')
