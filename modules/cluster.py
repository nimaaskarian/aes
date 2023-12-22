from sklearn.cluster import KMeans

class _Cluster:
    clusters:KMeans
    def ordered_clusters(self):
        if self.clusters.labels_ is None:
            return
        ordered = {}
        for i, cluster_index in enumerate(self.clusters.labels_):
            if cluster_index not in ordered:
                ordered[cluster_index] = []
            ordered[cluster_index].append(i)

        return ordered



class ClusterKmeans(_Cluster):
    def __init__(self,data, k:int) -> None:
        # random state is our random seed
        self.clusters = KMeans(n_clusters=k, random_state=42)
        self.clusters.fit(data)
