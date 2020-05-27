import typing

class Appearance:
    def __init__(self, docId: int, frequency: int):
        self.docId: int = docId
        self.frequency: int = frequency

    def __repr__(self) -> str:
        return str(self.__dict__)