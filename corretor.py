from typing import List

from apolice import Apolice
from contato import Contato
from pessoa import Pessoa


class Corretor(Pessoa):
    def __init__(
        self,
        primeiro_nome,
        sobrenome,
        data_nascimento,
        cpf,
        rg,
        contato: Contato,
        numero_susep,
        apolices: List[Apolice],
    ):
        super().__init__(
            primeiro_nome, sobrenome, data_nascimento, cpf, rg, None, contato
        )
        self._numero_susep = numero_susep
        self._apolices = apolices

    def comissao_total(self):
        return sum([apolice.comissao() for apolice in self._apolices])
