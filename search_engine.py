import numpy as np
from typing import List
from data_processor import DataProcessor

class SearchEngine:
    def __init__(self, paths:List[str]) -> None:
        self.dp = DataProcessor()
        for path in paths:
            self.dp.add_file(path)
    def calculate_tf(self):
        all_words = self.dp.docs_words_count_list()
        for word in self.dp.occur_dict:
            tf = self.dp.docs_occurances_list(word)/all_words
            idf = self.dp.doc_size/(len(self.dp.occur_dict[word])+1)
            print(word, tf*idf)
