from typing import Optional

from pydantic import BaseModel
from pydantic import validator

from src.validadores import valida_arg_nao_nulo
from src.validadores import valida_email


class Contato(BaseModel):
    celular: str
    telefone_residencial: Optional[str]
    telefone_comercial: Optional[str]
    email: str

    @validator("celular")
    def verifica_celular(cls, celular: str) -> str:
        erros = valida_arg_nao_nulo(celular, "celular")
        if len(erros) > 0:
            raise ValueError(erros)
        return celular

    @validator("email")
    def verifica_email(cls, email: str) -> str:
        erros = valida_email(email)
        if len(erros) > 0:
            raise ValueError(erros)
        return email
