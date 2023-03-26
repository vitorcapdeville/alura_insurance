from typing import List

from apolice import Apolice
from beneficiario import Beneficiario
from contato import Contato
from endereco import Endereco
from pessoa import Pessoa


class Segurado(Pessoa):
    def __init__(
        self,
        primeiro_nome,
        sobrenome,
        data_nascimento,
        cpf,
        rg,
        endereco: Endereco,
        contato: Contato,
        beneficiarios: List[Beneficiario],
        apolices: List[Apolice],
    ):
        super().__init__(
            primeiro_nome, sobrenome, data_nascimento, cpf, rg, endereco, contato
        )
        self._beneficiarios = beneficiarios
        self._apolices = apolices

    def __str__(self):
        return super().__str__() + f", beneficio_total: {self.beneficio_total():,.2f}"

    def beneficio_total(self):
        return sum([apolice.valor_beneficio for apolice in self._apolices])
