# Criar classes que recebem dict e retornam instancias de cada classe no modelo.
from abc import ABC
from abc import abstractmethod
from datetime import date
from typing import Dict
from uuid import UUID

from src.modelo.apolice import Apolice
from src.modelo.apolice import StatusApolice
from src.modelo.apolice import TipoApolice
from src.modelo.beneficiario import Beneficiario
from src.modelo.beneficiario import TipoBeneficiario
from src.modelo.contato import Contato
from src.modelo.corretor import Corretor
from src.modelo.endereco import Endereco
from src.modelo.endereco import Estado
from src.modelo.segurado import Segurado


def separa_nome_sobrenome(nome_completo: str) -> tuple[str, str]:
    nome_completo = nome_completo.strip()
    if " " in nome_completo:
        primeiro_nome, sobrenome = nome_completo.split(" ", 1)
        return primeiro_nome, sobrenome
    else:
        return nome_completo, ""


class Conversor(ABC):
    def __init__(self, dados: Dict):
        self.dados = dados

    @abstractmethod
    def __call__(self):
        pass


class ApoliceConversor(Conversor):
    def __call__(self):
        data = self.dados
        return Apolice(
            UUID(data.get("numero")),
            TipoApolice(data.get("tipo")),
            data.get("valor_beneficio"),
            data.get("valor_premio"),
            date.fromisoformat(data.get("data_inicio_vigencia")),
            date.fromisoformat(data.get("data_fim_vigencia")),
            StatusApolice(data.get("status")),
        )


class BeneficiarioConversor(Conversor):
    def __call__(self):
        data = self.dados
        primeiro_nome, sobrenome = separa_nome_sobrenome(data.get("nome"))
        endereco = EnderecoConversor(data["endereco"])()
        contato = ContatoConversor(data["contato"])()
        return Beneficiario(
            primeiro_nome,
            sobrenome,
            date.fromisoformat(data.get("data_nascimento")),
            data.get("cpf"),
            data.get("rg"),
            endereco,
            contato,
            TipoBeneficiario(data.get("tipo")),
        )


class EnderecoConversor(Conversor):
    def __call__(self):
        data = self.dados
        return Endereco(
            data.get("rua"),
            data.get("numero"),
            data.get("complemento"),
            data.get("cep"),
            Estado(data.get("estado")),
            data.get("cidade"),
        )


class ContatoConversor(Conversor):
    def __call__(self):
        data = self.dados
        return Contato(
            data.get("celular"),
            data.get("telefone_residencial"),
            data.get("telefone_comercial"),
            data.get("email"),
        )


class CorretorConversor(Conversor):
    def __call__(self):
        data = self.dados
        primeiro_nome, sobrenome = separa_nome_sobrenome(data.get("nome"))
        contato = ContatoConversor(data["contato"])()
        return Corretor(
            primeiro_nome,
            sobrenome,
            data.get("cpf"),
            data.get("rg"),
            contato,
            data.get("numero_susep"),
            [ApoliceConversor(apolice)() for apolice in data.get("apolices")],
        )


class SeguradoConversor(Conversor):
    def __call__(self):
        data = self.dados
        primeiro_nome, sobrenome = separa_nome_sobrenome(data.get("nome"))
        endereco = EnderecoConversor(data["endereco"])()
        contato = ContatoConversor(data["contato"])()
        return Segurado(
            primeiro_nome,
            sobrenome,
            date.fromisoformat(data.get("data_nascimento")),
            data.get("cpf"),
            data.get("rg"),
            endereco,
            contato,
            [BeneficiarioConversor(beneficiario)() for beneficiario in data.get("beneficiarios")],
            [ApoliceConversor(apolice)() for apolice in data.get("apolices")],
        )
