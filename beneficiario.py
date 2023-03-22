from enum import Enum

from contato import Contato
from endereco import Endereco
from pessoa import Pessoa


class TipoBeneficiario(Enum):
    PARENTE = 'PARENTE'
    AMIGO = 'AMIGO'
    OUTROS = 'OUTROS'


class Beneficiario:
    def __init__(self, pessoa: Pessoa, tipo: str, endereco: Endereco, contato: Contato):
        self._pessoa = pessoa
        self._tipo = TipoBeneficiario(tipo)
        self._endereco = endereco
        self._contato = contato
