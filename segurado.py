from typing import List

from apolice import Apolice
from beneficiario import Beneficiario
from contato import Contato
from endereco import Endereco
from pessoa import Pessoa


class Segurado:
    def __init__(
        self,
        pessoa: Pessoa,
        endereco: Endereco,
        contato: Contato,
        beneficiarios: List[Beneficiario],
        apolices: List[Apolice],
    ):
        self._pessoa = pessoa
        self._endereco = endereco
        self._contato = contato
        self._beneficiarios = beneficiarios
        self._apolices = apolices

    def nome_segurado(self):
        return self._pessoa.nome_completo()

    def premio_total(self):
        return sum([apolice.valor_premio for apolice in self._apolices])
