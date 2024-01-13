import numpy as np


def add_datasets(data_one, data_two):
    if len(data_one) != len(data_two):
        raise ValueError('Datasets must have the same length')

    return np.array(data_one) + np.array(data_two)


def add_anomalies(data, loc, scale, percentage, q):
    result = np.copy(data)
    n = len(data)
    num_anomalies = int(n * (percentage / 100))

    indexes = np.random.choice(np.arange(n), size=num_anomalies, replace=False)
    anomalies = np.random.normal(loc, q * scale, num_anomalies)

    result[indexes] += anomalies

    return result