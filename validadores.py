from re import match

CPF_FORMATO = "[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}"
EMAIL_FORMATO = "[^@]+@[^@]+[.][^@]+"
NUMERO_SUSEP_FORMATO = "^154146[0-9]{11}"


def valida_cpf(cpf):
    valida_arg_nao_nulo(cpf, "cpf")
    if not match(CPF_FORMATO, cpf):
        raise ValueError("cpf inválido.")
    return cpf


def valida_nome(nome, arg_name):
    valida_arg_nao_nulo(nome, arg_name)
    if len(nome) < 2:
        raise ValueError(f"{arg_name} deve possuir pelo menos 2 caracteres.")
    return nome


def valida_arg_nao_nulo(arg, arg_name):
    if not arg:
        raise ValueError(f"{arg_name} não pode ser vazio.")
    return arg


def valida_beneficiarios(beneficiarios):
    if not isinstance(beneficiarios, list):
        raise ValueError("beneficiarios deve ser uma lista.")
    if len(beneficiarios) > 10:
        raise ValueError("beneficiarios deve ter no máximo 10 elementos.")
    return beneficiarios


def valida_email(email):
    valida_arg_nao_nulo(email, "email")
    if not match(EMAIL_FORMATO, email):
        raise ValueError("email inválido.")


def valida_numero_susep(numero_susep):
    valida_arg_nao_nulo(numero_susep, "numero_susep")
    if len(numero_susep) != 17:
        raise ValueError("numero_susep deve possuir 17 caracteres.")
    if not match(NUMERO_SUSEP_FORMATO, numero_susep):
        raise ValueError("numero_susep inválido.")
    return numero_susep


def valida_positivo(valor, arg_name):
    valida_arg_nao_nulo(valor, arg_name)
    if valor <= 0:
        raise ValueError(f"{arg_name} deve ser positivo.")
    return valor


def valida_vigencia(data_inicio, data_fim):
    valida_arg_nao_nulo(data_inicio, "data_inicio")
    valida_arg_nao_nulo(data_fim, "data_fim")
    if data_inicio > data_fim:
        raise ValueError("data_inicio deve ser anterior a data_fim.")
    return data_inicio, data_fim
