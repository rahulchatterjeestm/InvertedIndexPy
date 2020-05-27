from typing import Dict

class Database:
    def __init__(self):
        self.db: Dict[int, dict] = dict()

    def __repr__(self) -> str:
        return str(self.__dict__)

    def Get(self, id: int) -> dict:
        return self.db.get(id, None)

    def Add(self, document):
        self.db.update({document['id']: document})

    def Remove(self, document) -> dict:
        return self.db.pop(document['id'], None)