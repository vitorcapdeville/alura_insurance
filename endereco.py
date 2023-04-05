from enum import Enum
from typing import Optional

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


class Endereco:
    def __init__(
        self,
        rua: str,
        numero: str,
        complemento: Optional[str],
        cep: str,
        estado: Estado,
        cidade: str
    ) -> None:
        self._rua: str = valida_arg_nao_nulo(rua.title(), "rua")
        self._numero: str = valida_arg_nao_nulo(numero, "numero")
        self._complemento: Optional[str] = complemento
        self._cep: str = valida_arg_nao_nulo(cep, "cep")
        self._estado: Estado = estado
        self._cidade: str = valida_arg_nao_nulo(cidade.title(), "cidade")

    @classmethod
    def from_dict(cls, data):
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
