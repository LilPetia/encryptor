import abc
from alphabet import Alphabet
from encoder_abstract import Encoder


class CaesarEncoder(Encoder):
    
    def __init__(self, key: int):
        self.key = int(key) % Alphabet.size()


    def encode_char(self, char: str, pos: int) -> str:
        if Alphabet.contains(char):
            sum_code = Alphabet.order(char) + self.key
            return Alphabet.getchar(sum_code % Alphabet.size())
        else:
            return char
        

    


class CaesarDecoder(Encoder):
    
    def __init__(self, key: int):
        self.key = int(key) % Alphabet.size()
        

    def encode_char(self, char: str, pos: int) -> str:
        if Alphabet.contains(char):
            sum_code = Alphabet.order(char) - self.key
            return Alphabet.getchar(sum_code % Alphabet.size())
        else:
            return char
        

    
