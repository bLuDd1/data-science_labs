import geopandas as gpd
import matplotlib.pyplot as plt


def map_plot(filname):
    df = gpd.read_file(filname)
    print('df.head():', df.head())

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    df.plot(ax=ax)
    plt.show()

    return


def map_filtr_plot_all(filname):
    df = gpd.read_file(filname)

    def myfilter(x):
        return x in tc

    len(df['fclass'].value_counts())
    print(len(df['fclass'].value_counts()))
    target_types = df['fclass'].value_counts() > 1
    tc = target_types[target_types == True].index
    df['delete'] = df['fclass'].apply(lambda x: myfilter(x))
    df = df[df['delete']]

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    df.plot(ax=ax, column='fclass', legend=True, cmap='viridis')
    plt.show()

    return


def map_filtr_plot_1(filname):
    df = gpd.read_file(filname)

    def myfilter(x):
        return x in tc

    tc = ['recreation_ground', 'park']
    df['delete'] = df['fclass'].apply(lambda x: myfilter(x))
    df = df[df['delete']]
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    gpd.read_file(filname).plot(ax=ax, color='grey', alpha=0.5)
    df.plot(ax=ax, column='fclass', legend=True, cmap='viridis')
    plt.show()
    return



def map_filtr_plot_2(filname):
    df = gpd.read_file(filname)

    def myfilter(x):
        return x in tc

    tc = ['forest']
    df['delete'] = df['fclass'].apply(lambda x: myfilter(x))
    df = df[df['delete']]
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    gpd.read_file(filname).plot(ax=ax, color='grey', alpha=0.5)
    df.plot(ax=ax, column='fclass', legend=True, cmap='viridis')
    plt.show()
    return
    

if __name__ == '__main__':
    map_plot('Estonia/gis_osm_landuse_a_free_1.shp')
    map_filtr_plot_all('Estonia/gis_osm_landuse_a_free_1.shp')
    map_filtr_plot_1('Estonia/gis_osm_landuse_a_free_1.shp')
    map_filtr_plot_2('Estonia/gis_osm_landuse_a_free_1.shp')
