from enum import Enum


class TipoApolice(Enum):
    VIDA = 1


class StatusApolice(Enum):
    ATIVA = 1
    LIQUIDADA = 2
    CANCELADA = 3
    EM_SINISTRO = 4


class Apolice:
    def __init__(
        self,
        numero,
        tipo: TipoApolice,
        valor_beneficio,
        segurado,
        corretor,
        data_inicio_vigencia,
        data_fim_vigencia,
        status: StatusApolice,
    ):
        self._numero = numero
        self._tipo = tipo
        self._valor_beneficio = valor_beneficio
        self._segurado = segurado
        self._corretor = corretor
        self._data_inicio_vigencia = data_inicio_vigencia
        self._data_fim_vigencia = data_fim_vigencia
        self._status = status

    @property
    def valor_beneficio(self):
        return self._valor_beneficio

    def comissao(self):
        return 0.1 * self._valor_beneficio
