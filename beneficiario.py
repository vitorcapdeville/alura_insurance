from enum import Enum

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
        primeiro_nome,
        sobrenome,
        data_nascimento,
        cpf,
        rg,
        endereco: Endereco,
        contato: Contato,
        tipo: TipoBeneficiario,
    ):
        super().__init__(
            primeiro_nome, sobrenome, data_nascimento, cpf, rg, endereco, contato
        )
        self._tipo = tipo

    def __str__(self):
        return super().__str__() + f", tipo: {self._tipo}"

    @property
    def tipo(self):
        return self._tipo
