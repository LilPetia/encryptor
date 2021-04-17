from abc import ABCMeta, abstractmethod
import json
from alphabet import Alphabet


class Trainer:

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def train(self, text: str):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_dict_model(self) -> dict:
        pass

    @abstractmethod
    def get_json_model(self) -> str:
        pass

    pass


class FrequencyTrainer(Trainer):

    def __init__(self):
        self.model = {}

    def train(self, text: str):
        for char in text:
            if not Alphabet.contains(char):
                continue
            if char not in self.model:
                self.model[char] = 0
            self.model[char] += 1
        pass

    def clear(self):
        self.model = {}
        pass

    def get_dict_model(self) -> dict:
        return self.model
        pass

    def get_json_model(self) -> str:
        return json.dumps(self.model)
        pass

    pass
