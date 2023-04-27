from datetime import date

import pytest

from src.modelo.pessoa import Pessoa


def test_nome_completo():
    pessoa = Pessoa(
        primeiro_nome="João",
        sobrenome="Silva",
        data_nascimento=date(2000, 1, 1),
        cpf="123.456.789-01",
        rg="123456789",
        endereco=None,
        contato=None
    )
    assert pessoa.nome_completo() == "João Silva"



def test_nome_sobrenome_nao_pode_ser_vazio():
    with pytest.raises(Exception):
        Pessoa(
            primeiro_nome="",
            sobrenome="Silva",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456.789-01",
            rg="123456789",
            endereco=None,
            contato=None
        )
    with pytest.raises(Exception):
        Pessoa(
            primeiro_nome="João",
            sobrenome="",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456.789-01",
            rg="123456789",
            endereco=None,
            contato=None
        )


def test_nome_sobrenome_deve_ter_pelo_menos_2_caracteres():
    with pytest.raises(Exception):
        Pessoa(
            primeiro_nome="J",
            sobrenome="Silva",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456.789-01",
            rg="123456789",
            endereco=None,
            contato=None
        )
    with pytest.raises(Exception):
        Pessoa(
            primeiro_nome="João",
            sobrenome="S",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456.789-01",
            rg="123456789",
            endereco=None,
            contato=None
        )


def test_cpf_deve_ser_valido():
    with pytest.raises(Exception):
        Pessoa(
            primeiro_nome="João",
            sobrenome="Silva",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456789-00",
            rg="123456789",
            endereco=None,
            contato=None
        )


def test_rg_nao_pode_ser_vazio():
    with pytest.raises(Exception):
        Pessoa(
            primeiro_nome="João",
            sobrenome="Silva",
            data_nascimento=date(2000, 1, 1),
            cpf="123.456.789-01",
            rg="",
            endereco=None,
            contato=None
        )
