from datetime import date
from enum import Enum
from uuid import UUID

from modelo.componente_seguro import ComponenteSeguro
from validadores import valida_positivo
from validadores import valida_vigencia


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


class Apolice(ComponenteSeguro):
    def __init__(
        self,
        numero: UUID,
        tipo: TipoApolice,
        valor_beneficio: float,
        valor_premio: float,
        data_inicio_vigencia: date,
        data_fim_vigencia: date,
        status: StatusApolice,
    ):
        self._numero = numero
        self._tipo = tipo
        self._valor_beneficio = valor_beneficio
        self._valor_premio = valor_premio
        self._segurado = None
        self._corretor = None
        self._data_inicio_vigencia = data_inicio_vigencia
        self._data_fim_vigencia = data_fim_vigencia
        self._status = status
        self._valida()

    @classmethod
    def from_dict(cls, data):
        return cls(
            UUID(data.get("numero")),
            TipoApolice(data.get("tipo")),
            data.get("valor_beneficio"),
            data.get("valor_premio"),
            date.fromisoformat(data.get("data_inicio_vigencia")),
            date.fromisoformat(data.get("data_fim_vigencia")),
            StatusApolice(data.get("status")),
        )

    def __str__(self):
        return (
            f"numero: {self._numero}, tipo: {self._tipo}, status: {self._status}, "
            f"inicio: {self._data_inicio_vigencia.strftime('%d/%m/%Y')}, "
            f"fim: {self._data_fim_vigencia.strftime('%d/%m/%Y')}, "
            f"valor_beneficio: {self._valor_premio:,.2f}"
        )

    @property
    def data_inicio_vigencia(self):
        return self._data_inicio_vigencia

    @property
    def tipo(self):
        return self._tipo

    @property
    def valor_premio(self):
        return self._valor_premio

    @property
    def valor_beneficio(self):
        return self._valor_beneficio

    def _pega_erros(self):
        erros = []
        erros += valida_positivo(self._valor_beneficio, "valor_beneficio")
        erros += valida_positivo(self._valor_premio, "valor_premio")
        erros += valida_vigencia(self._data_inicio_vigencia, self._data_fim_vigencia)
        return erros
