from datetime import date
from typing import List

from src.modelo.apolice import Apolice
from src.modelo.beneficiario import Beneficiario
from src.modelo.contato import Contato
from src.modelo.endereco import Endereco
from src.modelo.pessoa import Pessoa
from src.validadores import valida_arg_nao_nulo
from src.validadores import valida_beneficiarios
from src.validadores import valida_maioridade


class Segurado(Pessoa):
    def __init__(
        self,
        primeiro_nome: str,
        sobrenome: str,
        data_nascimento: date,
        cpf: str,
        rg: str,
        endereco: Endereco,
        contato: Contato,
        beneficiarios: List[Beneficiario],
        apolices: List[Apolice],
    ) -> None:
        self._beneficiarios = beneficiarios
        self._apolices = apolices
        self._data_ingresso = min([apolice.data_inicio_vigencia for apolice in apolices] or [date.today()])
        super().__init__(
            primeiro_nome, sobrenome, data_nascimento, cpf, rg, endereco, contato
        )

    def _pega_erros(self) -> list:
        erros = super()._pega_erros()
        erros += valida_beneficiarios(self._beneficiarios)
        erros += valida_arg_nao_nulo(self._apolices, "apolices")
        erros += valida_maioridade(self._data_nascimento, self._data_ingresso)
        return erros

    def __str__(self) -> str:
        return super().__str__() + f", beneficio_total: {self.beneficio_total():,.2f}"

    def beneficio_total(self) -> float:
        return sum([apolice.valor_beneficio for apolice in self._apolices])
