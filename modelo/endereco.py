from enum import Enum
from typing import Optional

from modelo.componente_seguro import ComponenteSeguro
from validadores import valida_arg_nao_nulo


class Estado(Enum):
    AC = "AC"
    AL = "AL"
    AP = "AP"
    AM = "AM"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MT = "MT"
    MS = "MS"
    MG = "MG"
    PA = "PA"
    PB = "PB"
    PR = "PR"
    PE = "PE"
    PI = "PI"
    RJ = "RJ"
    RN = "RN"
    RS = "RS"
    RO = "RO"
    RR = "RR"
    SC = "SC"
    SP = "SP"
    SE = "SE"
    TO = "TO"


class Endereco(ComponenteSeguro):
    def __init__(
        self,
        rua: str,
        numero: str,
        complemento: Optional[str],
        cep: str,
        estado: Estado,
        cidade: str
    ) -> None:
        self._rua: str = rua.title()
        self._numero: str = numero
        self._complemento: Optional[str] = complemento
        self._cep: str = cep
        self._estado: Estado = estado
        self._cidade: str = cidade.title()
        self._valida()

    def _pega_erros(self) -> list:
        erros = []
        erros += valida_arg_nao_nulo(self._rua, "rua")
        erros += valida_arg_nao_nulo(self._numero, "numero")
        erros += valida_arg_nao_nulo(self._cep, "cep")
        erros += valida_arg_nao_nulo(self._cidade, "cidade")
        return erros

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data.get("rua"),
            data.get("numero"),
            data.get("complemento"),
            data.get("cep"),
            Estado(data.get("estado")),
            data.get("cidade"),
        )

    def __str__(self) -> str:
        return (
            f"{self._rua}, numero {self._numero}, {self._complemento}, "
            f"{self._cidade}, {self._estado}"
        )
