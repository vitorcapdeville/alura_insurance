import pytest

from pessoa import valida_cpf


def test_valida_cpf():
    assert valida_cpf("123.456.789-00") == "123.456.789-00"
    # testar casos em que valida_cpf deveria levantar erro usando pytest.raises
    with pytest.raises(ValueError):
        valida_cpf(None)
        valida_cpf("123.456.789-0")
        valida_cpf("123.456.789-000")
