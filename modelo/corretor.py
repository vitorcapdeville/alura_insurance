from datetime import datetime
from typing import List

from calculadora_comissao import CalculadoraComissao
from construtores import separa_nome_sobrenome
from modelo.apolice import Apolice
from modelo.contato import Contato
from modelo.pessoa import Pessoa
from validadores import valida_numero_susep


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
        self._numero_susep = numero_susep
        self._apolices = apolices
        super().__init__(
            primeiro_nome,
            sobrenome,
            datetime.fromisoformat("9999-12-01"),
            cpf,
            rg,
            None,
            contato,
        )

    def _pega_erros(self):
        erros = super()._pega_erros()
        erros += valida_numero_susep(self._numero_susep)
        return erros

    @classmethod
    def from_dict(cls, data: dict):
        primeiro_nome, sobrenome = separa_nome_sobrenome(data.get("nome"))
        contato = Contato.from_dict(data["contato"])
        return cls(
            primeiro_nome,
            sobrenome,
            data.get("cpf"),
            data.get("rg"),
            contato,
            data.get("numero_susep"),
            [Apolice.from_dict(apolice) for apolice in data.get("apolices")],
        )

    def __str__(self):
        return super().__str__() + f", comissao_total: {self.comissao_total():,.2f}"

    def comissao_total(self):
        return CalculadoraComissao(self._apolices).calcula()
