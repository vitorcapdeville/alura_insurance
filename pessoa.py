from datetime import date
from typing import Optional

from dateutil.relativedelta import relativedelta

from contato import Contato
from endereco import Endereco
from validadores import valida_arg_nao_nulo
from validadores import valida_cpf
from validadores import valida_nome


class Pessoa:
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
        self._primeiro_nome = valida_nome(primeiro_nome, "primeiro_nome")
        self._sobrenome = valida_nome(sobrenome, "sobrenome")
        self._data_nascimento = data_nascimento
        self._cpf = valida_cpf(cpf)
        self._rg = valida_arg_nao_nulo(rg, "rg")
        self._endereco = endereco
        self._contato = contato

    def __str__(self):
        return (
            f"nome_completo: {self.nome_completo()}, data_nascimento:"
            f" {self._data_nascimento.strftime('%d/%m/%Y')}, classe: {self.__class__.__name__}"
        )

    def nome_completo(self):
        return f"{self._primeiro_nome} {self._sobrenome}"

    def idade(self, data_calculo: date = date.today()):
        return relativedelta(data_calculo, self._data_nascimento).years
