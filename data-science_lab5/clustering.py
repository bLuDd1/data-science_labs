import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


def k_means(dataset):
    plt.scatter(dataset[:, 0], dataset[:, 1], s=50)
    plt.show()

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(dataset)
    y_kmeans = kmeans.predict(dataset)

    plt.scatter(dataset[:, 0], dataset[:, 1], c=y_kmeans, s=50, cmap='viridis')

    centers = kmeans.cluster_centers_1
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()

    return centers


def main_cluster():
    dataset, _ = make_blobs(n_samples=600, cluster_std=1.8, random_state=0)
    k_means(dataset)

    expected_centers = [[-5, 0], [1, 3], [4, 4]]
    dataset, _ = make_blobs(n_samples=800, centers=expected_centers, cluster_std=0.7)
    actual_centers = k_means(dataset)

    print(f'Expected centers: {expected_centers}')
    print(f'Actual centers: {actual_centers}')
    return
