from datetime import date
from typing import List

from pydantic import root_validator
from pydantic import validator

from src.modelo.apolice import Apolice
from src.modelo.beneficiario import Beneficiario
from src.modelo.pessoa import Pessoa
from src.validadores import valida_arg_nao_nulo
from src.validadores import valida_beneficiarios
from src.validadores import valida_maioridade


class Segurado(Pessoa):
    beneficiarios: List[Beneficiario]
    apolices: List[Apolice]

    @validator("beneficiarios")
    def verifica_beneficiarios(cls, beneficiarios: List[Beneficiario]) -> List[Beneficiario]:
        erros = valida_beneficiarios(beneficiarios)
        if len(erros) > 0:
            raise ValueError(erros)
        return beneficiarios

    @validator("apolices")
    def verifica_apolices(cls, apolices: List[Apolice]) -> List[Apolice]:
        erros = valida_arg_nao_nulo(apolices, "apolices")
        if len(erros) > 0:
            raise ValueError(erros)
        return apolices

    @root_validator
    def verifica_maioridade(cls, values):
        data_ingresso = min([apolice.data_inicio_vigencia for apolice in values.get("apolices")] or [date.today()])
        erros = valida_maioridade(values.get("data_nascimento"), data_ingresso)
        if len(erros) > 0:
            raise ValueError(erros)
        return values

    def beneficio_total(self) -> float:
        return sum([apolice.valor_beneficio for apolice in self.apolices])
