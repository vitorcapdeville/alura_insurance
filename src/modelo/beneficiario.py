from datetime import date
from enum import Enum

from src.construtores import separa_nome_sobrenome
from src.modelo.contato import Contato
from src.modelo.endereco import Endereco
from src.modelo.pessoa import Pessoa


class TipoBeneficiario(Enum):
    PARENTE = "PARENTE"
    AMIGO = "AMIGO"
    OUTROS = "OUTROS"


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
            TipoBeneficiario(data.get("tipo")),
        )

    def __str__(self) -> str:
        return super().__str__() + f", tipo: {self._tipo}"

    @property
    def tipo(self) -> TipoBeneficiario:
        return self._tipo
