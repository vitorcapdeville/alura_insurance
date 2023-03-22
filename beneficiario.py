from contato import Contato
from endereco import Endereco
from pessoa import Pessoa


class Beneficiario:
    def __init__(self, pessoa: Pessoa, tipo, endereco: Endereco, contato: Contato):
        self._pessoa = pessoa
        self._tipo = tipo
        self._endereco = endereco
        self._contato = contato
