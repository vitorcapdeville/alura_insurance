from typing import List

from apolice import Apolice
from calculadora_comissao import calcula_comissao
from contato import Contato
from pessoa import Pessoa
from datetime import date


class Corretor(Pessoa):
    def __init__(
        self,
        primeiro_nome: str,
        sobrenome: str,
        data_nascimento: date,
        cpf: str,
        rg: str,
        contato: Contato,
        numero_susep,
        apolices: List[Apolice],
    ):
        super().__init__(
            primeiro_nome, sobrenome, data_nascimento, cpf, rg, None, contato
        )
        self._numero_susep = numero_susep
        self._apolices = apolices

    def __str__(self):
        return super().__str__() + f", comissao_total: {self.comissao_total():,.2f}"

    def comissao_total(self):
        return calcula_comissao(self._apolices)
