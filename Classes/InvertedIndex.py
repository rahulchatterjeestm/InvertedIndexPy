from typing import Dict
from Classes.Appearance import Appearance
from Classes.Database import Database
import re
class InvertedIndex:
    def __init__(self, db: Database):
        self.index = dict()
        self.db = db

    def __repr__(self):
        return str(self.index)

    def IndexDocument(self, document):
        cleanText = re.sub(r'[^\w\s]','', document['text'])
        terms= cleanText.split(' ')
        appearances: Dict[str, Appearance]= dict()
        for term in terms:
            freq = 0
            if term in appearances:
                freq = appearances[term].frequency
            appearances[term] = Appearance(document['id'], freq + 1)
        updateDict = {key: [appearance] if key not in self.index else self.index[key] + [appearance] for (key,appearance) in appearances.items()}
        self.index.update(updateDict)
        self.db.Add(document)
        return document

    def LookUp(self, query):
        return { term: self.index[term] for term in query.split(' ') if term in self.index }