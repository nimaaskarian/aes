from collections import defaultdict
import os,math
import numpy as np
from typing import Dict, List


def sentencize(string) -> List[str]:
    return string.split('. ')

def tokenize(string) -> List[str]:
    return string.lower().replace('. ', ' ').split()

def flatten_list(list:List[List]):
    return [item for row in list for item in row]

class DataProcessor:
    paths: List[str]
    occur_dict: Dict[str,List[List[int]]]
    doc_size:int
    def __init__(self, path=None) -> None:
        self.occur_dict = defaultdict(list)
        self.paths = []
        self.doc_size = 0
        if path is not None:
            self.add_file(path)

    def add_dir(self, dir) -> None:
        for file in os.listdir(dir):
            self.add_file(os.path.join(dir,file))

    def add_file(self, path) -> None:
        data = open(path).read()
        sentences = sentencize(data)

        for token in set(tokenize(data)):
            # doc count 
            self.occur_dict[token] += [[] for _ in range(1+self.doc_size-len(self.occur_dict[token]))]
            # sentence count
            self.occur_dict[token][self.doc_size] = np.zeros(len(sentences),int).tolist()

        for i, sentence in enumerate(sentences):
            sentence_tokens = tokenize(sentence)
            for token in set(sentence_tokens):

                self.occur_dict[token][self.doc_size][i] = sentence_tokens.count(token)

        self.doc_size+=1

    def __str__(self)->str:
        output = ""
        for key in self.occur_dict:
            output+=f"{key}: Docs: {len(self.occur_dict[key])}, Sentences: {len([row for row in self.occur_dict[key]])}, Occurances: {np.sum(flatten_list(self.occur_dict[key]))}, {flatten_list([self.occur_dict[key]])}\n"
        return output
