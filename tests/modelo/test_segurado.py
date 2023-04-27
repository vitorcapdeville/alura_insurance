from datetime import date
from uuid import UUID

import pytest

from src.conversores import SeguradoConversor
from src.modelo.apolice import Apolice
from src.modelo.apolice import StatusApolice
from src.modelo.apolice import TipoApolice
from src.modelo.beneficiario import Beneficiario
from src.modelo.beneficiario import TipoBeneficiario
from src.modelo.segurado import Segurado

beneficiarios = [
    Beneficiario(
        "João",
        "da Silva",
        date(1990, 1, 1),
        "123.456.789-00",
        "123456789",
        None,
        None,
        TipoBeneficiario("AMIGO")
    )
]
apolices = [
    Apolice(
        UUID('72900b51-b41a-4580-b9bc-3b17636de44b'),
        TipoApolice("VIDA"),
        3000.0,
        600,
        date(2020, 1, 1),
        date(2020, 12, 31),
        StatusApolice("ATIVA")
    ),
    Apolice(
        UUID('ea8f199c-e3a5-4f1e-914f-62c0f1ef976a'),
        TipoApolice("CARRO"),
        1000.0,
        100,
        date(2020, 1, 1),
        date(2020, 12, 31),
        StatusApolice("CANCELADA")
    ),
]


def test_segurado_conversor():
    data = {
        "nome": "João da Silva",
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
                "nome": "Maria da Silva",
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
    segurado = SeguradoConversor(data)()
    assert isinstance(segurado, Segurado)


def test_segurado_str():
    segurado = Segurado(
        "João",
        "Silva",
        date(2000, 1, 1),
        "123.456.789-00",
        "123456789",
        None,
        None,
        beneficiarios,
        apolices
    )
    assert str(
        segurado
    ) == "nome_completo: João Silva, data_nascimento: 01/01/2000, classe: Segurado, beneficio_total: 4,000.00"


def test_beneficio_total():
    segurado = Segurado(
        "João",
        "Silva",
        date(2000, 1, 1),
        "123.456.789-00",
        "123456789",
        None,
        None,
        beneficiarios,
        apolices
    )
    assert segurado.beneficio_total() == 4000


def test_apolice_nao_pode_ser_vazio():
    with pytest.raises(Exception):
        Segurado(
            "João",
            "Silva",
            date(2000, 1, 1),
            "123.456.789-00",
            "123456789",
            None,
            None,
            beneficiarios,
            []
        )


def test_nao_pode_ter_mais_que_10_beneficiarios():
    with pytest.raises(Exception):
        Segurado(
            "João",
            "Silva",
            date(2000, 1, 1),
            "123.456.789-00",
            "123456789",
            None,
            None,
            beneficiarios * 11,
            apolices
        )
