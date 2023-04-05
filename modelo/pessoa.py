from datetime import date
from typing import Optional

from construtores import separa_nome_sobrenome
from modelo.componente_seguro import ComponenteSeguro
from modelo.contato import Contato
from modelo.endereco import Endereco
from validadores import valida_arg_nao_nulo
from validadores import valida_cpf
from validadores import valida_nome


class Pessoa(ComponenteSeguro):
    def __init__(
        self,
        primeiro_nome: str,
        sobrenome: str,
        data_nascimento: date,
        cpf: str,
        rg: str,
        endereco: Optional[Endereco],
        contato: Optional[Contato]
    ):
        self._primeiro_nome = primeiro_nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._rg = rg
        self._endereco = endereco
        self._contato = contato
        self._valida()

    def _pega_erros(self):
        erros = []
        erros += valida_nome(self._primeiro_nome, "primeiro_nome")
        erros += valida_nome(self._sobrenome, "sobrenome")
        erros += valida_cpf(self._cpf)
        erros += valida_arg_nao_nulo(self._rg, "rg")
        return erros

    def __str__(self):
        return (
            f"nome_completo: {self.nome_completo()}, data_nascimento:"
            f" {self._data_nascimento.strftime('%d/%m/%Y')}, classe: {self.__class__.__name__}"
        )

    def nome_completo(self):
        return f"{self._primeiro_nome} {self._sobrenome}"

    @classmethod
    def from_dict(cls, data: dict):
        primeiro_nome, sobrenome = separa_nome_sobrenome(data.get("nome"))
        endereco = Endereco.from_dict(data["endereco"])
        contato = Contato.from_dict(data["contato"])
        return cls(
            primeiro_nome,
            sobrenome,
            date.fromisoformat(data.get("data_nascimento")),
            data.get("cpf"),
            data.get("rg"),
            endereco,
            contato,
        )
