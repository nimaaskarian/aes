from sklearn.cluster import AgglomerativeClustering, KMeans
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
    clusterer: KMeans
    def __init__(self,data, k:int) -> None:
        # random state is our random seed
        # k = self.find_k(data,max_k//3,max_k) or 0
        clusterer = KMeans(n_clusters=k, random_state=42, n_init="auto")
        clusterer.fit(data)
        super().__init__(clusterer)
    def find_best_k(self,data, min_k, max_k):
        best_score = -1
        best_k = None
        for k in range(min_k, max_k):
            self.clusterer.fit_predict(data)
            labels = self.clusterer.labels_
            score = silhouette_score(data, labels)
            if score > best_score:
                best_score = score
                best_k = k
            print(k, best_score, score)
            # if k > 200:
            #     break
        print("best score:", best_score)
        return best_k

class ClusterAgglomerative(_Cluster):
    clusterer: AgglomerativeClustering
    def __init__(self,data) -> None:
        clusterer = AgglomerativeClustering(n_clusters=None, distance_threshold=0)
        clusterer.fit(data)
        super().__init__(clusterer)


class ClusterDBSCAN(_Cluster):
    clusterer: DBSCAN
    def __init__(self,data,eps) -> None:
        # len(data[0])
        clusterer = DBSCAN(eps=eps, min_samples=1, metric='precomputed')
        clusterer.fit(data)
        super().__init__(clusterer)
