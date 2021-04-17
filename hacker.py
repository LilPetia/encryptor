from abc import ABCMeta, abstractmethod
from train import FrequencyTrainer
from alphabet import Alphabet


class Hacker:

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, model):
        self.model = dict(model)
        pass

    @abstractmethod
    def hack_text(self, text: str) -> str:
        pass

    pass


class CaesarHacker(Hacker):

    def __init__(self, model):
        super().__init__(model)
        pass

    def find_frequency(self, text: str):

        self.frequency = {}

        for char in text:
            if not Alphabet.contains(char):
                continue
            if char not in self.frequency:
                self.frequency[char] = 0
            self.frequency[char] += 1
        pass

    pass

    def hack_key(self, text: str):

        self.find_frequency(text)

        min_shift = 0
        min_delta = -1

        for shift in range(0, Alphabet.size()):
            delta = 0
            for (char, freq) in self.frequency.items():
                num_new_char = (Alphabet.order(char) + shift) % Alphabet.size()
                new_char = Alphabet.getchar(num_new_char)

                delta += (self.frequency[char] if char in self.frequency else 0) ** 2 - \
                         (self.model[new_char] if new_char in self.model else 0) ** 2

            if min_delta == -1 or delta < min_delta:
                min_delta = delta
                min_shift = shift

        return Alphabet.size() - min_shift
        pass

    pass
