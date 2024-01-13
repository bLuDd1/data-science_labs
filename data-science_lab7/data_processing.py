import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def parse(file):
    df = pd.read_excel(file)

    data = np.transpose(df.iloc[:, 0:6].values)
    district_dict = dict(zip(df.iloc[:, 9].dropna().values, df['Регіон'].dropna().values))

    return data, district_dict


def visualize(*args, text, keys=0):
    plt.clf()
    for arg in args:
        plt.plot(keys, arg) if keys else plt.plot(arg)
    plt.title(text)
    plt.show()


def data_sum_sales(data):
    result = {}
    for i in range(len(data[3])):
        current_key = data[1][i]
        sales = data[3][i] * data[5][i]

        if current_key in result:
            result[current_key] += sales
        else:
            result[current_key] = sales
    return result


def data_sum_profit(data):
    result = {}
    for i in range(len(data[3])):
        current_key = data[1][i]
        profit = (data[5][i] - data[4][i]) * data[3][i]
        if current_key in result:
            result[current_key] += profit
        else:
            result[current_key] = profit
    return result


def calculate_sales_profit(row):
    date = row[1]
    sales = [date, row[3] * row[5]]
    profit = [date, (row[5] - row[4]) * row[3]]
    return sales, profit


def region_clustering(data, region_dict):
    result = {}

    for i in range(len(data[3])):
        magaz_code = data[0][i]
        region = region_dict.get(magaz_code, "")

        sales, profit = calculate_sales_profit(data[:, i])

        if region not in result:
            result[region] = {'sales': [], 'profit': []}

        result[region]['sales'].append(sales)
        result[region]['profit'].append(profit)

    for region in result:
        region_date_clustering(result[region])

    return result


def cluster_dates(data, key):
    clustered_dates = {}
    for entry in data[key]:
        if entry[0] not in clustered_dates:
            clustered_dates[entry[0]] = entry[1]
        else:
            clustered_dates[entry[0]] += entry[1]
    sorted_dates = dict(sorted(clustered_dates.items(), key=lambda x: pd.to_datetime(x[0])))
    data[key] = sorted_dates


def region_date_clustering(region):
    cluster_dates(region, 'sales')
    cluster_dates(region, 'profit')

