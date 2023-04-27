from datetime import date

import pytest

from src.modelo.pessoa import Pessoa


def test_nome_completo():
    pessoa = Pessoa("João", "Silva", date(2000, 1, 1), "123.456.789-01", "123456789", None, None)
    assert pessoa.nome_completo() == "João Silva"


def test_str():
    pessoa = Pessoa("João", "Silva", date(2000, 1, 1), "123.456.789-01", "123456789", None, None)
    assert str(pessoa) == "nome_completo: João Silva, data_nascimento: 01/01/2000, classe: Pessoa"


def test_nome_sobrenome_nao_pode_ser_vazio():
    with pytest.raises(Exception):
        Pessoa("", "Silva", date(2000, 1, 1), "123.456.789-01", "123456789", None, None)
    with pytest.raises(Exception):
        Pessoa("Joao", "", date(2000, 1, 1), "123.456.789-01", "123456789", None, None)


def test_nome_sobrenome_deve_ter_pelo_menos_2_caracteres():
    with pytest.raises(Exception):
        Pessoa("J", "Silva", date(2000, 1, 1), "123.456.789-01", "123456789", None, None)
    with pytest.raises(Exception):
        Pessoa("Joao", "S", date(2000, 1, 1), "123.456.789-01", "123456789", None, None)


def test_cpf_deve_ser_valido():
    with pytest.raises(Exception):
        Pessoa("Joao", "Silva", date(2000, 1, 1), "123.456789-00", "123456789", None, None)


def test_rg_nao_pode_ser_vazio():
    with pytest.raises(Exception):
        Pessoa("Joao", "Silva", date(2000, 1, 1), "123.456.789-00", "", None, None)
