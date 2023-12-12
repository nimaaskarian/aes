from typing import Dict, List
import os
class DataProcessor:
    tokens: List[str]
    word_count_dict: Dict[str,int]
    def __init__(self, path=None) -> None:
        self.tokens = []
        if path is not None:
            self.add_file(path)

    def add_dir(self, dir) -> None:
        for file in os.listdir(dir):
            self.add_file(os.path.join(dir,file))

    def add_file(self, path) -> None:
        self.tokens += self.tokenize(open(path).read())

    def tokenize(self, string) -> List[str]:
        return string.lower().split()

    def count_word(self, word) -> int:
        return self.tokens.count(word)

    def create_word_count(self):
        self.word_count_dict = dict()

        for token in self.tokens:
            try:
                self.word_count_dict[token]
            except(KeyError):
                self.word_count_dict[token] = self.count_word(token)
        return self.word_count_dict

    def unique_words(self):
        return [word for word in self.word_count_dict.keys() if self.word_count_dict[word] == 1]

dp = DataProcessor()
for i in range(20):
    dp.add_file(f"/home/nima/Downloads/Telegram Desktop/data/document_{i}.txt")
# dp.add_file("/home/nima/Downloads/Telegram Desktop/data/document_3.txt")
# dp.add_dir("/home/nima/Downloads/Telegram Desktop/data")
print(dp.create_word_count())
print(dp.unique_words())
