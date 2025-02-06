from abc import ABC, abstractmethod

class ConvertABC(ABC):
    @abstractmethod
    def convert(self):
        pass