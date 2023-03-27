from datetime import date
from enum import Enum


class TipoApolice(Enum):
    VIDA = 1
    CARRO = 2
    CASA = 3
    VIAGEM = 4


class StatusApolice(Enum):
    ATIVA = 1
    LIQUIDADA = 2
    CANCELADA = 3
    EM_SINISTRO = 4


class Apolice:
    def __init__(
        self,
        numero: int,
        tipo: TipoApolice,
        valor_beneficio: float,
        data_inicio_vigencia: date,
        data_fim_vigencia: date,
        status: StatusApolice,
    ):
        self._numero = numero
        self._tipo = tipo
        self._valor_beneficio = valor_beneficio
        self._segurado = None
        self._corretor = None
        self._data_inicio_vigencia = data_inicio_vigencia
        self._data_fim_vigencia = data_fim_vigencia
        self._status = status

    def __str__(self):
        return (
            f"numero: {self._numero}, tipo: {self._tipo}, status: {self._status}, "
            f"inicio: {self._data_inicio_vigencia.strftime('%d/%m/%Y')}, "
            f"fim: {self._data_fim_vigencia.strftime('%d/%m/%Y')}, "
            f"valor_beneficio: {self._valor_beneficio:,.2f}, comissao: {self.comissao():,.2f}"
        )

    @property
    def tipo(self):
        return self._tipo

    @property
    def valor_beneficio(self):
        return self._valor_beneficio
