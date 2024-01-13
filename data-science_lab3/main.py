import pandas as pd
import numpy as np


def file_parsing(data_name, sample_data):
    values = sample_data[data_name].astype(str).str.replace(',', '.').astype(float)
    return values.to_numpy()


def matrix_generation(file_name):
    sample_data = pd.read_excel(file_name)
    print(sample_data)
    line_sample_data, column_sample_data = sample_data.shape
    line_column_matrix = np.zeros((line_sample_data, column_sample_data - 2))

    for i in range(1, column_sample_data - 1):
        column_matrix = file_parsing(sample_data.columns[i], sample_data)
        line_column_matrix[:, i - 1] = column_matrix

    return line_column_matrix


def matrix_adapter(line_column_matrix, line):
    return line_column_matrix[line, :]


def calc_optimal(file, weight_1, weight_2, weight_3, weight_4, weight_5, weight_6, weight_7, weight_8, weight_9, weight_10):
    line_column_matrix = matrix_generation(file)
    column_matrix = np.shape(line_column_matrix)
    Integro = np.zeros((column_matrix[1]))

    price = matrix_adapter(line_column_matrix, 0)
    fuel_consumption = matrix_adapter(line_column_matrix, 1)
    max_speed = matrix_adapter(line_column_matrix, 2)
    racing = matrix_adapter(line_column_matrix, 3)
    engine_capacity = matrix_adapter(line_column_matrix, 4)
    power = matrix_adapter(line_column_matrix, 5)
    trunk = matrix_adapter(line_column_matrix, 6)
    mass = matrix_adapter(line_column_matrix, 7)
    fuel_tank = matrix_adapter(line_column_matrix, 8)
    clearance = matrix_adapter(line_column_matrix, 9)

    price_normalized = np.zeros((column_matrix[1]))
    fuel_consumption_normalized = np.zeros((column_matrix[1]))
    max_speed_normalized = np.zeros((column_matrix[1]))
    racing_normalized = np.zeros((column_matrix[1]))
    engine_capacity_normalized = np.zeros((column_matrix[1]))
    power_normalized = np.zeros((column_matrix[1]))
    trunk_normalized = np.zeros((column_matrix[1]))
    mass_normalized = np.zeros((column_matrix[1]))
    fuel_tank_normalized = np.zeros((column_matrix[1]))
    clearance_normalized = np.zeros((column_matrix[1]))

    weights_normalization_sum = weight_1 + weight_2 + weight_3 + weight_4 + weight_5 + weight_6 + weight_7 + weight_8 + weight_9 + weight_10

    weight_1_normalized = weight_1 / weights_normalization_sum
    weight_2_normalized = weight_2 / weights_normalization_sum
    weight_3_normalized = weight_3 / weights_normalization_sum
    weight_4_normalized = weight_4 / weights_normalization_sum
    weight_5_normalized = weight_5 / weights_normalization_sum
    weight_6_normalized = weight_6 / weights_normalization_sum
    weight_7_normalized = weight_7 / weights_normalization_sum
    weight_8_normalized = weight_8 / weights_normalization_sum
    weight_9_normalized = weight_9 / weights_normalization_sum
    weight_10_normalized = weight_10 / weights_normalization_sum

    sum_price = sum_fuel_consumption = sum_max_speed = sum_racing = sum_engine_capacity = sum_power = sum_trunk = sum_mass = sum_fuel_tank = sum_clearance = 0

    for i in range(column_matrix[1]):
        sum_price += price[i]
        sum_fuel_consumption += fuel_consumption[i]
        sum_max_speed += (1 / max_speed[i])
        sum_racing += racing[i]
        sum_engine_capacity += (1 / engine_capacity[i])
        sum_power += (1 / power[i])
        sum_trunk += (1 / trunk[i])
        sum_mass += mass[i]
        sum_fuel_tank += (1 / fuel_tank[i])
        sum_clearance += (1 / clearance[i])

    for i in range(column_matrix[1]):
        price_normalized[i] = price[i] / sum_price
        fuel_consumption_normalized[i] = fuel_consumption[i] / sum_fuel_consumption
        max_speed_normalized[i] = (1 / max_speed[i]) / sum_max_speed
        racing_normalized[i] = racing[i] / sum_racing
        engine_capacity_normalized[i] = (1 / engine_capacity[i]) / sum_engine_capacity
        power_normalized[i] = (1 / power[i]) / sum_power
        trunk_normalized[i] = (1 / trunk[i]) / sum_trunk
        mass_normalized[i] = mass[i] / sum_mass
        fuel_tank_normalized[i] = (1 / fuel_tank[i]) / sum_fuel_tank
        clearance_normalized[i] = (1 / clearance[i]) / sum_clearance

        Integro[i] = ((weight_1_normalized * (1 - price_normalized[i]) ** (-1)) +
                      (weight_2_normalized * (1 - fuel_consumption_normalized[i]) ** (-1)) +
                      (weight_3_normalized * (1 - max_speed_normalized[i]) ** (-1)) +
                      (weight_4_normalized * (1 - racing_normalized[i]) ** (-1)) +
                      (weight_5_normalized * (1 - engine_capacity_normalized[i]) ** (-1)) +
                      (weight_6_normalized * (1 - power_normalized[i]) ** (-1)) +
                      (weight_7_normalized * (1 - trunk_normalized[i]) ** (-1)) +
                      (weight_8_normalized * (1 - mass_normalized[i]) ** (-1)) +
                      (weight_9_normalized * (1 - fuel_tank_normalized[i]) ** (-1)) +
                      (weight_10_normalized * (1 - clearance_normalized[i]) ** (-1)))

    min = 10000

    optimal_index = 0

    for i in range(column_matrix[1]):
        if min > Integro[i]:
            min = Integro[i]
            optimal_index = i
    sample_data = pd.read_excel(file)
    integro_sorted = sorted(Integro)

    print('\nОптимальний позашляховик:', sample_data.columns[optimal_index + 1])
    print('\nРейтинг позашляховиків:')
    for i in range(len(integro_sorted)):
        element_index = list(Integro).index(integro_sorted[i])
        print(f'{i + 1}. {sample_data.columns[element_index + 1]}: {integro_sorted[i]}')

    return


if __name__ == '__main__':
    file = 'lab3.xlsx'

    weight_1 = weight_4 = weight_5 = weight_7 = weight_10 = weight_8 = weight_3 = 1
    weight_2 = weight_6 = weight_9 = 2

    calc_optimal(file, weight_1, weight_2, weight_3, weight_4, weight_5, weight_6, weight_7, weight_8, weight_9, weight_10)
