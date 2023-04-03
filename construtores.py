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


def separa_nome_sobre(nome_completo: str):
    nome_completo = nome_completo.strip()
    if " " in nome_completo:
        primeiro_nome, sobrenome = nome_completo.split(" ", 1)
        return primeiro_nome, sobrenome
    else:
        return nome_completo, ""


def ler_json(file_path):
    with open(file_path, "r") as f:
        data = load(f)
    return data


class CriarInstancia:
    @classmethod
    def from_json(cls, file_path: str):
        data = ler_json(file_path)
        return cls.from_dict(data)

    @staticmethod
    def from_dict(data: dict):
        pass


class CriarApolice(CriarInstancia):
    @staticmethod
    def from_dict(data: dict):
        return Apolice(
            TipoApolice(data.get("tipo")),
            data.get("valor_beneficio"),
            data.get("valor_premio"),
            datetime.fromisoformat(data.get("data_inicio_vigencia")),
            datetime.fromisoformat(data.get("data_fim_vigencia")),
            StatusApolice(data.get("status")),
        )


class CriarEndereco(CriarInstancia):
    @staticmethod
    def from_dict(data: dict):
        return Endereco(
            data.get("rua"),
            data.get("numero"),
            data.get("complemento"),
            data.get("cep"),
            data.get("estado"),
            data.get("cidade"),
        )


class CriarContato(CriarInstancia):
    @staticmethod
    def from_dict(data: dict):
        return Contato(
            data.get("celular"),
            data.get("telefone_residencial"),
            data.get("telefone_comercial"),
            data.get("email"),
        )


class CriarBeneficiario(CriarInstancia):
    @staticmethod
    def from_dict(data: dict):
        primeiro_nome, sobrenome = separa_nome_sobre(data.get("nome"))
        endereco = CriarEndereco.from_dict(data["endereco"])
        contato = CriarContato.from_dict(data["contato"])
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


class CriarSegurado(CriarInstancia):
    @staticmethod
    def from_dict(data: dict):
        primeiro_nome, sobrenome = separa_nome_sobre(data.get("nome"))
        endereco = CriarEndereco.from_dict(data["endereco"])
        contato = CriarContato.from_dict(data["contato"])
        return Segurado(
            primeiro_nome,
            sobrenome,
            datetime.fromisoformat(data.get("data_nascimento")),
            data.get("cpf"),
            data.get("rg"),
            endereco,
            contato,
            beneficiarios=[CriarBeneficiario.from_dict(b) for b in data["beneficiarios"]],
            apolices=[CriarApolice.from_dict(a) for a in data["apolices"]],
        )


class CriarCorretor(CriarInstancia):
    @staticmethod
    def from_dict(data: dict):
        primeiro_nome, sobrenome = separa_nome_sobre(data.get("nome"))
        contato = CriarContato.from_dict(data["contato"])
        return Corretor(
            primeiro_nome,
            sobrenome,
            data.get("cpf"),
            data.get("rg"),
            contato,
            data.get("numero_susep"),
            data.get("apolices"),
        )
