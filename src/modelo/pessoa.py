from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import validator

from src.modelo.contato import Contato
from src.modelo.endereco import Endereco
from src.validadores import valida_arg_nao_nulo
from src.validadores import valida_cpf
from src.validadores import valida_nome


# noinspection PyMethodParameters
class Pessoa(BaseModel):
    primeiro_nome: str
    sobrenome: str
    data_nascimento: Optional[date]
    cpf: str
    rg: str
    endereco: Optional[Endereco]
    contato: Optional[Contato]

    class Config:
        arbitrary_types_allowed = True

    @validator("cpf")
    def verifica_cpf(cls, cpf: str) -> str:
        erros = valida_cpf(cpf)
        if len(erros) > 0:
            raise ValueError(erros)
        return cpf

    @validator("primeiro_nome", "sobrenome")
    def verifica_nome(cls, nome: str) -> str:
        erros = valida_nome(nome, "nome")
        if len(erros) > 0:
            raise ValueError(erros)
        return nome

    @validator("rg")
    def verifica_rg(cls, rg: str) -> str:
        erros = valida_arg_nao_nulo(rg, "rg")
        if len(erros) > 0:
            raise ValueError(erros)
        return rg

    def nome_completo(self) -> str:
        return f"{self.primeiro_nome} {self.sobrenome}"
