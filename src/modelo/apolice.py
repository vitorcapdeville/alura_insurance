from datetime import date
from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from pydantic import root_validator
from pydantic import validator

from src.validadores import valida_positivo
from src.validadores import valida_vigencia


class TipoApolice(Enum):
    VIDA = "VIDA"
    CARRO = "CARRO"
    CASA = "CASA"
    VIAGEM = "VIAGEM"


class StatusApolice(Enum):
    ATIVA = "ATIVA"
    LIQUIDADA = "LIQUIDADA"
    CANCELADA = "CANCELADA"
    EM_SINISTRO = "EM_SINISTRO"


class Apolice(BaseModel):
    numero: UUID
    tipo: TipoApolice
    valor_beneficio: float
    valor_premio: float
    data_inicio_vigencia: date
    data_fim_vigencia: date
    status: StatusApolice

    @validator("valor_beneficio", "valor_premio")
    def verifica_valor(cls, valor):
        erros = valida_positivo(valor, "valor")
        if len(erros) > 0:
            raise ValueError(erros)
        return valor

    @root_validator
    def verifica_vigencia(cls, values):
        data_inicio, data_fim = values["data_inicio_vigencia"], values["data_fim_vigencia"]
        erros = valida_vigencia(data_inicio, data_fim)
        if len(erros) > 0:
            raise ValueError(erros)
        return values
