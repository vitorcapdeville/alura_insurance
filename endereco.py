class Endereco:
    def __init__(self, rua, numero, complemento, cep, estado, cidade):
        self._rua = rua.title()
        self._numero = numero
        self._complemento = complemento
        self._cep = cep
        self._estado = estado.title()
        self._cidade = cidade.title()

    def __str__(self):
        return (
            f"{self._rua}, numero {self._numero}, {self._complemento}, "
            f"{self._cidade}, {self._estado}"
        )

