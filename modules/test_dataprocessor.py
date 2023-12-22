import unittest
from dataprocessor import DataProcessorDocs
from cluster import ClusterKmeans

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.dp = DataProcessorDocs()
        DOC_SIZE = 4
        self.dp.set_paths([f"tests/doc{i}" for i in range(DOC_SIZE)])
        self.dp.generate_tfidf()
        
        self.clusters = ClusterKmeans(self.dp.calculate_similarities(), 3).clusters
        
tp = TestDataProcessor()
tp.setUp()
print(tp.clusters)
