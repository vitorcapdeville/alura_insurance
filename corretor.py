from datetime import datetime
from typing import List

from apolice import Apolice
from calculadora_comissao import calcula_comissao
from contato import Contato
from pessoa import Pessoa


class Corretor(Pessoa):
    def __init__(
        self,
        primeiro_nome: str,
        sobrenome: str,
        cpf: str,
        rg: str,
        contato: Contato,
        numero_susep,
        apolices: List[Apolice],
    ):
        super().__init__(
            primeiro_nome,
            sobrenome,
            datetime.fromisoformat("9999-12-01"),
            cpf,
            rg,
            None,
            contato,
        )
        self._numero_susep = numero_susep
        self._apolices = apolices

    def __str__(self):
        return super().__str__() + f", comissao_total: {self.comissao_total():,.2f}"

    def comissao_total(self):
        return calcula_comissao(self._apolices)
