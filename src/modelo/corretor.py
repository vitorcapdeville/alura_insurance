from datetime import datetime
from typing import List

from src.calculadora_comissao import CalculadoraComissao
from src.modelo.apolice import Apolice
from src.modelo.contato import Contato
from src.modelo.pessoa import Pessoa
from src.validadores import valida_numero_susep


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

    def _pega_erros(self) -> list:
        erros = super()._pega_erros()
        erros += valida_numero_susep(self._numero_susep)
        return erros

    def __str__(self) -> str:
        return super().__str__() + f", comissao_total: {self.comissao_total():,.2f}"

    def comissao_total(self) -> float:
        return CalculadoraComissao(self._apolices).calcula()
