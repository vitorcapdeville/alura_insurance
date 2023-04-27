from datetime import date
from uuid import UUID

import pytest

from src.modelo.apolice import Apolice
from src.modelo.apolice import StatusApolice
from src.modelo.apolice import TipoApolice
from src.modelo.beneficiario import Beneficiario
from src.modelo.beneficiario import TipoBeneficiario
from src.modelo.segurado import Segurado

beneficiarios = [
    Beneficiario(
        primeiro_nome="João",
        sobrenome="da Silva",
        data_nascimento=date(1990, 1, 1),
        cpf="123.456.789-00",
        rg="123456789",
        endereco=None,
        contato=None,
        tipo=TipoBeneficiario("AMIGO")
    )
]
apolices = [
    Apolice(
        numero=UUID('72900b51-b41a-4580-b9bc-3b17636de44b'),
        tipo=TipoApolice("VIDA"),
        valor_beneficio=3000.0,
        valor_premio=600,
        data_inicio_vigencia=date(2020, 1, 1),
        data_fim_vigencia=date(2020, 12, 31),
        status=StatusApolice("ATIVA")
    ),
    Apolice(
        numero=UUID('ea8f199c-e3a5-4f1e-914f-62c0f1ef976a'),
        tipo=TipoApolice("CARRO"),
        valor_beneficio=1000.0,
        valor_premio=100,
        data_inicio_vigencia=date(2020, 1, 1),
        data_fim_vigencia=date(2020, 12, 31),
        status=StatusApolice("CANCELADA")
    ),
]


def test_segurado_conversor():
    data = {
        "primeiro_nome": "João",
        "sobrenome": "da Silva",
        "data_nascimento": "1990-01-01",
        "cpf": "123.456.789-00",
        "rg": "123456789",
        "endereco": {
            "rua": "Rua das Flores",
            "numero": "123",
            "complemento": "Apto 101",
            "bairro": "Centro",
            "cidade": "São Paulo",
            "estado": "SP",
            "cep": "12345678",
        },
        "contato": {
            "email": "email@provedor.com",
            "celular": "11987654321",
        },
        "beneficiarios": [
            {
                "primeiro_nome": "Maria",
                "sobrenome": "da Silva",
                "data_nascimento": "1990-01-01",
                "cpf": "123.456.789-00",
                "rg": "123456789",
                "tipo": "PARENTE",
                "endereco": {
                    "rua": "Rua das Flores",
                    "numero": "123",
                    "complemento": "Apto 101",
                    "bairro": "Centro",
                    "cidade": "São Paulo",
                    "estado": "SP",
                    "cep": "12345678",
                },
                "contato": {
                    "email": "maria@gmail.com",
                    "celular": "11987654321",
                },
            },
        ],
        "apolices": [
            {
                "numero": "72900b51-b41a-4580-b9bc-3b17636de44b",
                "tipo": "VIDA",
                "valor_beneficio": 3000.0,
                "valor_premio": 600.0,
                "data_inicio_vigencia": "2020-01-01",
                "data_fim_vigencia": "2020-12-31",
                "status": "ATIVA",
            },
        ],
    }
    segurado = Segurado.parse_obj(data)
    assert isinstance(segurado, Segurado)


def test_beneficio_total():
    segurado = Segurado(
        primeiro_nome="João",
        sobrenome="Silva",
        data_nascimento=date(2000, 1, 1),
        cpf="123.456.789-00",
        rg="123456789",
        endereco=None,
        contato=None,
        beneficiarios=beneficiarios,
        apolices=apolices
    )
    assert segurado.beneficio_total() == 4000


def test_apolice_nao_pode_ser_vazio():
    with pytest.raises(Exception):
        Segurado(
            primeiro_nome="João",
            sobrenome="Silva",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456.789-00",
            rg="123456789",
            endereco=None,
            contato=None,
            beneficiarios=beneficiarios,
            apolices=[]
        )


def test_nao_pode_ter_mais_que_10_beneficiarios():
    with pytest.raises(Exception):
        Segurado(
            primeiro_nome="João",
            sobrenome="Silva",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456.789-00",
            rg="123456789",
            endereco=None,
            contato=None,
            beneficiarios=beneficiarios * 11,
            apolices=apolices
        )
