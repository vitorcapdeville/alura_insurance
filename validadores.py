from re import match

CPF_FORMATO = "[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}"
EMAIL_FORMATO = "[^@]+@[^@]+[.][^@]+"
NUMERO_SUSEP_FORMATO = "^154146[0-9]{11}"
ESTADOS = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}


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


# valida que estado possui uma sigla valida com base em ESTADOS
def valida_estado(estado):
    valida_arg_nao_nulo(estado, "estado")
    if len(estado) != 2:
        raise ValueError("estado deve ser a sigla e não o nome do estado.")
    if estado not in ESTADOS:
        raise ValueError("estado inválido.")
    return estado


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
