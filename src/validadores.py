from datetime import date
from re import match
from typing import Any
from typing import List

from dateutil.relativedelta import relativedelta

CPF_FORMATO = "^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$"
EMAIL_FORMATO = "^[^@]+@[^@]+[.][^@]+$"
NUMERO_SUSEP_FORMATO = "^154146[0-9]{11}$"


def calcula_idade_anos(data_nascimento: date, data_calculo: date) -> int:
    return relativedelta(data_calculo, data_nascimento).years


def valida_cpf(cpf: str) -> List[Exception]:
    erros = []
    erros += valida_arg_nao_nulo(cpf, "cpf")
    if not match(CPF_FORMATO, cpf or ""):
        erros += [ValueError("cpf inválido.")]
    return erros


def valida_nome(nome: str, arg_name: str) -> List[Exception]:
    erros = []
    erros += valida_arg_nao_nulo(nome, arg_name)
    if len(nome) < 2:
        erros += [ValueError(f"{arg_name} deve possuir pelo menos 2 caracteres.")]
    return erros


def valida_arg_nao_nulo(arg: Any, arg_name: str) -> List[Exception]:
    erros = []
    if not arg:
        erros += [ValueError(f"{arg_name} não pode ser vazio.")]
    return erros


def valida_beneficiarios(beneficiarios: List) -> List[Exception]:
    erros = []
    if not isinstance(beneficiarios, list):
        erros += [ValueError("beneficiarios deve ser uma lista.")]
    if len(beneficiarios) > 10:
        erros += [ValueError("beneficiarios deve ter no máximo 10 elementos.")]
    return erros


def valida_email(email: str) -> List[Exception]:
    erros = []
    erros += valida_arg_nao_nulo(email, "email")
    if not match(EMAIL_FORMATO, email):
        erros += [ValueError("email inválido.")]
    return erros


def valida_numero_susep(numero_susep: str) -> List[Exception]:
    erros = []
    erros += valida_arg_nao_nulo(numero_susep, "numero_susep")
    if len(numero_susep) != 17:
        erros += [ValueError("numero_susep deve possuir 17 caracteres.")]
    if not match(NUMERO_SUSEP_FORMATO, numero_susep):
        erros += [ValueError("numero_susep inválido.")]
    return erros


def valida_positivo(valor: float, arg_name: str) -> List[Exception]:
    erros = []
    erros += valida_arg_nao_nulo(valor, arg_name)
    if valor <= 0:
        erros += [ValueError(f"{arg_name} deve ser positivo.")]
    return erros


def valida_vigencia(data_inicio: date, data_fim: date) -> List[Exception]:
    erros = []
    erros += valida_arg_nao_nulo(data_inicio, "data_inicio")
    erros += valida_arg_nao_nulo(data_fim, "data_fim")
    if data_inicio > data_fim:
        erros += [ValueError("data_inicio deve ser anterior a data_fim.")]
    return erros


def valida_maioridade(data_nascimento: date, data_inicio: date) -> List[Exception]:
    erros = []
    if calcula_idade_anos(data_nascimento, data_inicio) <= 18:
        erros += [ValueError("Segurado não pode ser menor de idade.")]
    return erros
