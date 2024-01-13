from data_parsing import parsing_site, file_parsing
from math_functions import Plot_AV, print_MNK_characteristics, get_normal_model, get_square_model
from data_manipulating import add_datasets, add_anomalies
import matplotlib.pyplot as plt


if __name__ == '__main__':
    n = 10000

    print('Обрано: Парсинг табличних даних https://index.minfin.com.ua/ua/exchange/nbu/bullion/xau/')
    url = "https://index.minfin.com.ua/ua/exchange/nbu/bullion/xau/"
    parsing_site(url)

    data_array = file_parsing(url, 'hrn-to-gold.xlsx', 'Курс (грн.)')
    meanSquare, median, var, a, b, c = print_MNK_characteristics(data_array, 'Коливання ціни золота')
    Plot_AV(data_array, data_array, 'Коливання ціни золота')

    normal_noise = get_normal_model(0, meanSquare, n)
    print_MNK_characteristics(normal_noise, 'Нормальний шум')
    plt.hist(normal_noise, bins=20)
    plt.ylabel('Нормальний шум')
    plt.show()

    a = a/((n/len(data_array))**2)
    b = b/(n/len(data_array))
    square_model = get_square_model(n, a, b, c)
    Plot_AV(square_model, square_model, 'Квадратична модель')

    data_with_noise = add_datasets(square_model, normal_noise)
    print_MNK_characteristics(data_with_noise, 'Модель із нормальним шумом')
    Plot_AV(square_model, data_with_noise, 'Модель із нормальним шумом')

    data_with_noise_and_anomalies = add_anomalies(data_with_noise, 0, 1.7, 5, 3)
    print_MNK_characteristics(data_with_noise_and_anomalies, 'Модель із нормальним шумом та аномальними вимірами')
    Plot_AV(square_model, data_with_noise_and_anomalies, 'Модель із нормальним шумом та аномальними вимірами')
