from abc import ABC
from abc import abstractmethod


class ComponenteSeguro(ABC):

    @abstractmethod
    def _pega_erros(self) -> list:
        raise NotImplementedError

    def _valida(self) -> None:
        erros = self._pega_erros()
        if len(erros) > 0:
            raise Exception(erros)
