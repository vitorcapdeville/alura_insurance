from contato import Contato
from endereco import Endereco
from datetime import date


class Pessoa:
    def __init__(
        self,
        primeiro_nome: str,
        sobrenome: str,
        data_nascimento: date,
        cpf: str,
        rg: str,
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

    def __str__(self):
        return (
            f"nome_completo: {self.nome_completo()}, data_nascimento:"
            f" {self._data_nascimento.strftime('%d/%m/%Y')}, classe: {self.__class__.__name__}"
        )

    def nome_completo(self):
        return f"{self._primeiro_nome} {self._sobrenome}"
