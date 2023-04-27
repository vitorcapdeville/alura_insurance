from enum import Enum

from src.modelo.pessoa import Pessoa


class TipoBeneficiario(Enum):
    PARENTE = "PARENTE"
    AMIGO = "AMIGO"
    OUTROS = "OUTROS"


class Beneficiario(Pessoa):
    tipo: TipoBeneficiario
