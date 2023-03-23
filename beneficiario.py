from enum import Enum

from contato import Contato
from endereco import Endereco
from pessoa import Pessoa


class TipoBeneficiario(Enum):
    PARENTE = 1
    AMIGO = 2
    OUTROS = 3


class Beneficiario:
    def __init__(
        self,
        pessoa: Pessoa,
        tipo: TipoBeneficiario,
        endereco: Endereco,
        contato: Contato,
    ):
        self._pessoa = pessoa
        self._tipo = tipo
        self._endereco = endereco
        self._contato = contato

    @property
    def tipo(self):
        return self._tipo
