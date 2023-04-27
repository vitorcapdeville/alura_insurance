from enum import Enum
from typing import Optional

from pydantic import BaseModel
from pydantic import validator

from src.validadores import valida_arg_nao_nulo


class Estado(Enum):
    AC = "AC"
    AL = "AL"
    AP = "AP"
    AM = "AM"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MT = "MT"
    MS = "MS"
    MG = "MG"
    PA = "PA"
    PB = "PB"
    PR = "PR"
    PE = "PE"
    PI = "PI"
    RJ = "RJ"
    RN = "RN"
    RS = "RS"
    RO = "RO"
    RR = "RR"
    SC = "SC"
    SP = "SP"
    SE = "SE"
    TO = "TO"


class Endereco(BaseModel):
    rua: str
    numero: str
    complemento: Optional[str]
    cep: str
    estado: Estado
    cidade: str

    @validator("rua", "numero", "cep", "cidade")
    def verifica_rua(cls, arg: str) -> str:
        erros = valida_arg_nao_nulo(arg, "arg")
        if len(erros) > 0:
            raise ValueError(erros)
        return arg
