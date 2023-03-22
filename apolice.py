from enum import Enum


class TipoApolice(Enum):
    VIDA = 'VIDA'


class StatusApolice(Enum):
    ATIVA = 'ATIVA'
    LIQUIDADA = 'LIQUIDADA'
    CANCELADA = 'CANCELADA'
    EM_SINISTRO = 'EM_SINISTRO'


class Apolice:
    def __init__(
        self, numero, tipo, valor_beneficio, segurado, corretor, data_inicio_vigencia, data_fim_vigencia, status
    ):
        self._numero = numero
        self._tipo = TipoApolice(tipo)
        self._valor_beneficio = valor_beneficio
        self._segurado = segurado
        self._corretor = corretor
        self._data_inicio_vigencia = data_inicio_vigencia
        self._data_fim_vigencia = data_fim_vigencia
        self._status = StatusApolice(status)

    @property
    def valor_beneficio(self):
        return self._valor_beneficio

    @property
    def comissao(self):
        return 0.1 * self._valor_beneficio
