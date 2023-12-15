import json
from typing import List

class Documents:
    query:str
    candidates: List[int]
    selected: int
    def __init__(self, query, candidates, selected) -> None:
        self.query = query
        self.candidates = candidates
        self.selected = selected

def json_return_docs(path)->List:
    with open(path) as file:
        data = json.load(file)

    return [Documents(document["query"], document["candidate_documents_id"], document["is_selected"].index(1)) 
              for document in data]
