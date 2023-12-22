from sklearn.cluster import KMeans

class _Cluster:
    clusters:dict
    def __init__(self, cluster_data) -> None:
        if cluster_data.labels_ is None:
            return
        self.clusters = {}
        for i, cluster_index in enumerate(cluster_data.labels_):
            if cluster_index not in self.clusters:
                self.clusters[cluster_index] = []
            self.clusters[cluster_index].append(i)



class ClusterKmeans(_Cluster):
    def __init__(self,data, k:int) -> None:
        # random state is our random seed
        cluster_data = KMeans(n_clusters=k, random_state=42, n_init="auto")
        cluster_data.fit(data)
        super().__init__(cluster_data)
