import abc

from ASCI import ASCI
from encoder_abstract import Encoder

class VernamEncoder(Encoder):
    def __init__(self, key: int):
        if (key == ""):
            raise Exception("Empty string")
        self.key = int(key) % ASCI.size()
        pass
    def encode_char(self, char:str, pos: int) -> str:
        if (ASCI.contains(char)):
            return ASCI.getchar((ASCI.order(char) ^ self.key) % ASCI.size())
        else:
            return char


class VernamDecoder(Encoder):

    def __init__(self, key: str):
        if key == "":
            raise Exception("Empty string")
        self.key = int(key) % ASCI.size()
        pass

    def encode_char(self, char: str, pos: int) -> str:
        if ASCI.contains(char):
            return ASCI.getchar((ASCI.order(char) ^ self.key) % ASCI.size())
        else:
            return char
        pass