from abc import ABC
from abc import abstractmethod


class ComponenteSeguro(ABC):
    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        raise NotImplementedError

    @abstractmethod
    def _pega_erros(self):
        raise NotImplementedError

    def _valida(self):
        erros = self._pega_erros()
        if len(erros) > 0:
            raise Exception(erros)
