from collections import defaultdict
import os,math
import numpy as np
from typing import Dict, List

from psutil import Error


def sentencize(string) -> List[str]:
    return string.split('. ')

def tokenize(string) -> List[str]:
    return string.lower().replace('. ', ' ').split()


class DataProcessor:
    paths: List[str]
    # occur_dict: Dict[str,List[List[int]]]
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
            # self.occur_dict[token] += [0 for _ in range(1+self.doc_size-len(self.occur_dict[token]))]
            # self.occur_dict[token] += [[] for _ in range(1+self.doc_size-len(self.occur_dict[token]))]
            # sentence count
            self.occur_dict[token].append((self.doc_size,np.zeros(len(sentences),np.uint8)))

        for i, sentence in enumerate(sentences):
            sentence_tokens = tokenize(sentence)
            for token in set(sentence_tokens):

                self.occur_dict[token][-1][1][i] = sentence_tokens.count(token)

        self.doc_size+=1

    def word_search_index(self, word:str, index:int):
        self.check_word(word)
        high = len(self.occur_dict[word])
        low = 0
        while low <= high:
            mid = low+(high-low)//2

            if index == self.occur_dict[word][mid][0]:
                return self.occur_dict[word][mid][1]

            if index > self.occur_dict[word][mid][0]:
                low = mid+1
            else:
                high = mid-1
        return 0
            
    # development helpers
    def check_word(self, word:str):
        if word not in self.occur_dict:
            raise RuntimeError(f"Error: word \"{word}\" not found in this instance of DataProcessor.")

    def occurences(self, word:str) -> int:
        self.check_word(word)
        return np.sum(np.concatenate([item for index,item in self.occur_dict[word]]))


    def document_occurences(self, word:str, index:int) -> int:
        if index >= self.doc_size or index < 0:
            raise RuntimeError(f"Error: index is not valid. valid indexes for this instance are between 0 and {self.doc_size-1}.")
        self.check_word(word)
        try:
            return np.sum(self.word_search_index(word, index))
        except(IndexError):
            return 0

    def __str__(self)->str:
        output = ""
        for key, value in self.occur_dict.items():
            output+=f"'{key}': {value}\n"
        return output

