from data_processing import parse, visualize, data_sum_sales, data_sum_profit, region_clustering
from modeling import MNK, Stat_characteristics

if __name__ == '__main__':
    file_path = 'Pr_1.xls'
    data, magaz_dict = parse(file_path)

    sales = data_sum_sales(data)
    profit = data_sum_profit(data)

    visualize(profit.values(), sales.values(), text="Прибуток і продажі по днях")

    cluster = region_clustering(data, magaz_dict)

    for region in cluster:
        sales_data = cluster[region]['sales']
        dates = sales_data.keys()
        MNK_sales = MNK(list(sales_data.values()))
        visualize(sales_data.values(), MNK_sales, text=f'Продажі по днях регіону: {region}', keys=dates)

        profit_data = cluster[region]['profit']
        dates = profit_data.keys()
        MNK_profit = MNK(list(profit_data.values()), True)
        visualize(profit_data.values(), MNK_profit, text=f'Прибуток по днях регіону: {region}', keys=dates)
        Stat_characteristics(list(profit_data.values()), f'Характеристика розподілу прибутку регіону: {region}')
