from caesar import CaesarEncoder, CaesarDecoder
from vigenere import VigenereEncoder, VigenereDecoder


def encode(cipher: str, key, text: str) -> str:
   
    if cipher == 'vigenere':
        encoder = VigenereEncoder(key)
    elif cipher == 'caesar':
        encoder = CaesarEncoder(key)
    return encoder.encode(text)
    pass


def decode(cipher: str, key, text: str) -> str:
    if cipher == 'vigenere':
        decoder = VigenereDecoder(key)
    elif cipher == 'caesar':
        decoder = CaesarDecoder(key)

    return decoder.encode(text)
    pass
