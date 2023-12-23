from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

class _Cluster:
    clusters:dict
    def __init__(self, clusterer) -> None:
        if clusterer is None:
            return
        self.labels = clusterer.labels_
        self.clusters = {}
        for i, cluster_index in enumerate(clusterer.labels_):
            if cluster_index not in self.clusters:
                self.clusters[cluster_index] = []
            self.clusters[cluster_index].append(i)

    def find_contains(self, search):
        for values in self.clusters.values():
            if search in values:
                return values


class ClusterKmeans(_Cluster):
    def __init__(self,data, k:int) -> None:
        # random state is our random seed
        clusterer = KMeans(n_clusters=k, random_state=42, n_init="auto")
        clusterer.fit(data)
        super().__init__(clusterer)

class ClusterDBSCAN(_Cluster):
    def __init__(self,data) -> None:
        clusterer = DBSCAN()
        clusterer.fit(data)
        super().__init__(clusterer)
