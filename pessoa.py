class Pessoa:
    def __init__(
        self, primeiro_nome, sobrenome, data_nascimento=None, cpf=None, rg=None
    ):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._rg = rg

    def nome_completo(self):
        return f"{self._primeiro_nome} {self._sobrenome}"
