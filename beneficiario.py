from datetime import date
from enum import Enum

from construtores import separa_nome_sobre
from contato import Contato
from endereco import Endereco
from pessoa import Pessoa


class TipoBeneficiario(Enum):
    PARENTE = 1
    AMIGO = 2
    OUTROS = 3


class Beneficiario(Pessoa):
    def __init__(
        self,
        primeiro_nome: str,
        sobrenome: str,
        data_nascimento: date,
        cpf: str,
        rg: str,
        endereco: Endereco,
        contato: Contato,
        tipo: TipoBeneficiario,
    ) -> None:
        super().__init__(
            primeiro_nome, sobrenome, data_nascimento, cpf, rg, endereco, contato
        )
        self._tipo = tipo

    @classmethod
    def from_dict(cls, data: dict):
        primeiro_nome, sobrenome = separa_nome_sobre(data.get("nome"))
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
            TipoBeneficiario(data.get("tipo")),
        )

    def __str__(self):
        return super().__str__() + f", tipo: {self._tipo}"

    @property
    def tipo(self):
        return self._tipo
