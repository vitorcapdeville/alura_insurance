from typing import Optional

from validadores import valida_arg_nao_nulo
from validadores import valida_estado


class Endereco:
    def __init__(
        self,
        rua: str,
        numero: str,
        complemento: Optional[str],
        cep: str,
        estado: str,
        cidade: str
    ) -> None:
        self._rua: str = valida_arg_nao_nulo(rua.title(), "rua")
        self._numero: str = valida_arg_nao_nulo(numero, "numero")
        self._complemento: Optional[str] = complemento
        self._cep: str = valida_arg_nao_nulo(cep, "cep")
        self._estado: str = valida_estado(estado)
        self._cidade: str = valida_arg_nao_nulo(cidade.title(), "cidade")

    def __str__(self) -> str:
        return (
            f"{self._rua}, numero {self._numero}, {self._complemento}, "
            f"{self._cidade}, {self._estado}"
        )
