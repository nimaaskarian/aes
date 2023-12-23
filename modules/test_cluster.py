import unittest
from dataprocessor import DataProcessorDocs
from cluster import ClusterKmeans

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.dp = DataProcessorDocs()
        DOC_SIZE = 4
        self.dp.set_paths([f"tests/doc{i}" for i in range(DOC_SIZE)])
        self.dp.generate_tfidf()
        
    def test_clusters(self):
        cluster = ClusterKmeans(self.dp.calculate_similarities(), 3)
        self.assertEqual(cluster.find_contains(1), [1,3])
        
if __name__ == '__main__':
    unittest.main() 
