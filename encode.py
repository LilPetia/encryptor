from caesar import CaesarEncoder, CaesarDecoder
from vigenere import VigenereEncoder, VigenereDecoder
from vernam import VernamDecoder, VernamEncoder
from hacker import CaesarHacker
from train import FrequencyTrainer

def encode(cipher: str, key, text: str) -> str:
    
    if cipher == 'vigenere':
        encoder = VigenereEncoder(key)
    elif cipher == 'caesar':
        encoder = CaesarEncoder(key)
    elif cipher == 'vernam':
        encoder = VernamEncoder(key)
    return encoder.encode(text)
    


def decode(cipher: str, key, text: str) -> str:
    if cipher == 'vigenere':
        decoder = VigenereDecoder(key)
    elif cipher == 'caesar':
        decoder = CaesarDecoder(key)
    elif cipher == 'vernam':
        decoder = VernamDecoder(key)
    return decoder.encode(text)


def train(text: str) -> str:
    trainer = FrequencyTrainer()
    trainer.train(text)
    return trainer.get_json_model()
    pass


def hack(model: dict, text: str) -> str:
    hacker = CaesarHacker(model)
    hacker_decoder = CaesarDecoder(hacker.hack_key(text))
    return hacker_decoder.encode(text)
    pass