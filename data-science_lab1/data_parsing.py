import numpy as np
import pandas as pd
import re
import requests


def parsing_site(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
    html_source = requests.get(url, headers=headers).text
    html_source = re.sub(r'<.*?>', lambda g: g.group(0).upper(), html_source)
    dataframe = pd.read_html(html_source)[0]

    dataframe.to_excel("hrn-to-gold.xlsx")
    return dataframe


def file_parsing(url, file_name, data_name):
    dataframe = pd.read_excel(file_name)
    dataframe = dataframe.iloc[:-1]
    values = dataframe[data_name].values / 10000
    S_real = np.zeros(len(values))

    for i, value in enumerate(values):
        S_real[i] = value

    print(f'Джерело даних: {url}')
    return S_real
