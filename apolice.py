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
        valor_premio,
        segurado,
        corretor,
        data_inicio_vigencia,
        data_fim_vigencia,
        status: StatusApolice,
    ):
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._segurado = segurado
        self._corretor = corretor
        self._data_inicio_vigencia = data_inicio_vigencia
        self._data_fim_vigencia = data_fim_vigencia
        self._status = status

    @property
    def valor_premio(self):
        return self._valor_premio

    def comissao(self):
        return 0.1 * self._valor_premio

apolice1 = Apolice(123, "Vida", 1000, "Diego", "Paloma", "01/01/2023", "31/12/2023", "VIDA")
apolice2 = Apolice(456, "Vida", 5000, "Diego", "Paloma", "01/01/2023", "31/12/2023", "VIDA")
apolice1._status
apolice2._status

# from segurado import Segurado
# segurado1 = Segurado("Diego", "abc", "123", "xyz", [apolice1, apolice2])
# segurado1.premio_total()