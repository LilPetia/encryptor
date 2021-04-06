import abc


class Encoder():
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, key):
        pass

    @abc.abstractmethod
    def encode_char(self, char: str, pos: int) -> str:
        pass

    def encode(self, text: str) -> str:
        result = ""
        position = 0
        for char in text:
            result += self.encode_char(char, position)
            position += 1
        return result
        pass

    pass
