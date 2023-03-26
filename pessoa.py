from contato import Contato
from endereco import Endereco


class Pessoa:
    def __init__(
        self,
        primeiro_nome,
        sobrenome,
        data_nascimento,
        cpf,
        rg,
        endereco: Endereco,
        contato: Contato,
    ):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._contato = contato

    def nome_completo(self):
        return f"{self._primeiro_nome} {self._sobrenome}"
