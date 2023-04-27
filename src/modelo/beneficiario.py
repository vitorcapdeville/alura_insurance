from datetime import date
from enum import Enum

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

    def __str__(self) -> str:
        return super().__str__() + f", tipo: {self._tipo}"

    @property
    def tipo(self) -> TipoBeneficiario:
        return self._tipo
