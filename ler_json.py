from datetime import datetime
from json import load

from apolice import Apolice
from apolice import StatusApolice
from apolice import TipoApolice
from beneficiario import Beneficiario
from beneficiario import TipoBeneficiario
from contato import Contato
from corretor import Corretor
from endereco import Endereco
from segurado import Segurado


def ler_json(file_path):
    with open(file_path, "r") as f:
        data = load(f)
    return data


def separa_nome_sobre(nome_completo: str):
    nome_completo = nome_completo.strip()
    if " " in nome_completo:
        primeiro_nome, sobrenome = nome_completo.split(" ", 1)
        return primeiro_nome, sobrenome
    else:
        return nome_completo, ""


def apolice_factory(file_path: str):
    data = ler_json(file_path)
    return Apolice(
        data.get("numero"),
        TipoApolice(data.get("tipo")),
        data.get("valor_beneficio"),
        datetime.fromisoformat(data.get("data_inicio_vigencia")),
        datetime.fromisoformat(data.get("data_fim_vigencia")),
        StatusApolice(data.get("status")),
    )


def endereco_factory(file_path: str):
    with open(file_path, "r") as f:
        data = load(f)
    return Endereco(
        data.get("rua"),
        data.get("numero"),
        data.get("complemento"),
        data.get("cep"),
        data.get("estado"),
        data.get("cidade"),
    )


def beneficiario_factory(file_path: str):
    with open(file_path, "r") as f:
        data = load(f)
    primeiro_nome, sobrenome = separa_nome_sobre(data.get("nome"))
    endereco = endereco_factory(file_path)
    contato = contato_factory(file_path)
    return Beneficiario(
        primeiro_nome,
        sobrenome,
        datetime.fromisoformat(data.get("data_nascimento")),
        data.get("cpf"),
        data.get("rg"),
        endereco,
        contato,
        TipoBeneficiario(data.get("tipo")),
    )


def contato_factory(file_path: str):
    with open(file_path, "r") as f:
        data = load(f)
    return Contato(
        data.get("celular"),
        data.get("telefone_residencial"),
        data.get("telefone_comercial"),
        data.get("email"),
    )


def corretor_factory(file_path: str):
    with open(file_path, "r") as f:
        data = load(f)
    primeiro_nome, sobrenome = separa_nome_sobre(data.get("nome"))
    contato = contato_factory(file_path)
    return Corretor(
        primeiro_nome,
        sobrenome,
        data.get("cpf"),
        data.get("rg"),
        contato,
        data.get("numero_susep"),
        [Apolice(**apolice) for apolice in data.get("apolices")],
    )


def segurado_factory(file_path: str):
    with open(file_path, "r") as f:
        data = load(f)
    primeiro_nome, sobrenome = separa_nome_sobre(data.get("nome"))
    endereco = endereco_factory(file_path)
    contato = contato_factory(file_path)
    return Segurado(
        primeiro_nome,
        sobrenome,
        datetime.fromisoformat(data.get("data_nascimento")),
        data.get("cpf"),
        data.get("rg"),
        endereco,
        contato,
        [Beneficiario(**beneficiario) for beneficiario in data.get("beneficiarios")],
        [Apolice(**apolice) for apolice in data.get("apolices")],
    )
