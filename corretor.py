from typing import List

from apolice import Apolice
from contato import Contato
from pessoa import Pessoa


class Corretor:
    def __init__(
        self, pessoa: Pessoa, numero_susep, apolices: List[Apolice], contato: Contato
    ):
        self._pessoa = pessoa
        self._numero_susep = numero_susep
        self._apolices = apolices
        self._contato = contato

    def comissao_total(self):
        return sum([apolice.comissao() for apolice in self._apolices])
