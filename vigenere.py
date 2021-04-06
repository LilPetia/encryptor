import abc
from alphabet import Alphabet
from encoder_abstract import Encoder


class VigenereEncoder(Encoder):
    def __init__(self, key: str):
        if key == "":
            raise Exception("Empty string")
        self.key = key
        pass

    def encode_char(self, char: str, pos: int) -> str:
        if Alphabet.contains(char):
            sum_code = Alphabet.order(char) + Alphabet.order(self.key[pos % len(self.key)])
            return Alphabet.getchar(sum_code % Alphabet.size())
        else:
            return char
        pass

    pass


class VigenereDecoder(Encoder):

    def __init__(self, key: str):
        if key == "":
            raise Exception("Empty string")
        self.key = key
        pass

    def encode_char(self, char: str, pos: int) -> str:
        if Alphabet.contains(char):
            sum_code = Alphabet.order(char) - Alphabet.order(self.key[pos % len(self.key)])
            return Alphabet.getchar(sum_code % Alphabet.size())
        else:
            return char
        pass
