from typing import List

from pydantic import validator

from src.calculadora_comissao import CalculadoraComissao
from src.modelo.apolice import Apolice
from src.modelo.pessoa import Pessoa
from src.validadores import valida_numero_susep


class Corretor(Pessoa):
    numero_susep: str
    apolices: List[Apolice]

    @validator("numero_susep")
    def verifica_numero_susep(cls, numero_susep: str) -> str:
        erros = valida_numero_susep(numero_susep)
        if len(erros) > 0:
            raise ValueError(erros)
        return numero_susep

    def comissao_total(self) -> float:
        return CalculadoraComissao(self.apolices).calcula()
