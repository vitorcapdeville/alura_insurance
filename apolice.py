class Apolice:
    def __init__(self, numero, tipo, valor_beneficio, segurado, corretor, data_inicio_vigencia, data_fim_vigencia,
                 status):
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
