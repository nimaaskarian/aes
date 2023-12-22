import os, re, string
from typing import List
from dataclasses import dataclass

import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def sentencize(str) -> List[str]:
    return list(filter(None, re.split(r'\.\s+', str)))
    # return str.split('. ')

def tokenize(str) -> List[str]:
    return str.lower().translate(str.maketrans('', '', string.punctuation)).split()
    # return str.lower().replace('. ', ' ').split()

@dataclass
class SentencePosition:
    doc_index: int
    sentence_index: int

class DataProcessor:
    paths: List[str]
    document_tfidfs: list
    tfidf_vectorizer: TfidfVectorizer
    def __init__(self, path=None) -> None:
        self.paths = list()
        if path is not None:
            self.add_file(path)
        self.generated = False

    def set_paths(self, paths:List[str]) -> None:
        self.paths = paths
        self.generated = False

    def add_dir(self, dir) -> None:
        for file in os.listdir(dir):
            self.add_file(os.path.join(dir,file))
        self.generated = False

    def add_file(self, path) -> None:
        self.paths.append(path)
        self.generated = False

    def calculate_similarities(self):
        return cosine_similarity(self.document_tfidfs)

    def calculate_query_similarities(self, query:str):
        query_vector = self.tfidf_vectorizer.transform([query])
        return cosine_similarity(query_vector, self.document_tfidfs)

class DataProcessorDocs(DataProcessor):
    def generate_tfidf(self):
        self.document_tfidfs = list()
        datas = list()
        for path in self.paths:
            with open(path) as file:
                datas.append(file.read())

        self.tfidf_vectorizer = TfidfVectorizer(stop_words="english", use_idf=True)
        self.document_tfidfs = self.tfidf_vectorizer.fit_transform(datas)
        self.generated = True

class DataProcessorSentences(DataProcessor):
    def generate_tfidf(self):
        self.document_tfidfs = list()
        self.documents_sentences_count = list()
        sentences = list()
        for path in self.paths:
            with open(path) as file:
                sentences+=sentencize(file.read())
                self.documents_sentences_count.append(len(sentences[-1]))

        self.tfidf_vectorizer = TfidfVectorizer(stop_words="english", use_idf=True)
        self.document_tfidfs = self.tfidf_vectorizer.fit_transform(sentences)
        self.generated = True
    # most_similar_doc_index = np.argmax(similarities)
    # print(np.argsort(similarities)[::-1])
    # print("Most relevant document:", most_similar_doc_index)
    # similarities
