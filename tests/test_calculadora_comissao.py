from datetime import date
from uuid import UUID

from src.calculadora_comissao import CalculadoraComissao
from src.modelo.apolice import Apolice
from src.modelo.apolice import StatusApolice
from src.modelo.apolice import TipoApolice


def test_calcula_comissao_vida():
    apolice = Apolice(
        numero=UUID('12345678123456781234567812345678'),
        tipo=TipoApolice.VIDA,
        valor_beneficio=1000000,
        valor_premio=1000000,
        data_inicio_vigencia=date(2020, 1, 1),
        data_fim_vigencia=date(2020, 12, 31),
        status=StatusApolice.ATIVA
    )
    assert CalculadoraComissao([apolice]).calcula() == 6100.0


def test_calcula_comissao_vida_premio_menor_850000():
    apolice = Apolice(
        numero=UUID('12345678123456781234567812345678'),
        tipo=TipoApolice.VIDA,
        valor_beneficio=1000000,
        valor_premio=500000,
        data_inicio_vigencia=date(2020, 1, 1),
        data_fim_vigencia=date(2020, 12, 31),
        status=StatusApolice.ATIVA
    )
    assert CalculadoraComissao([apolice]).calcula() == 2600.0


def test_calcula_comissao_carro():
    apolice = Apolice(
        numero=UUID('12345678123456781234567812345678'),
        tipo=TipoApolice.CARRO,
        valor_beneficio=1000000,
        valor_premio=1000000,
        data_inicio_vigencia=date(2020, 1, 1),
        data_fim_vigencia=date(2020, 12, 31),
        status=StatusApolice.ATIVA
    )
    assert CalculadoraComissao([apolice]).calcula() == 3575.5


def test_calcula_comissao_casa():
    apolice = Apolice(
        numero=UUID('12345678123456781234567812345678'),
        tipo=TipoApolice.CASA,
        valor_beneficio=1000000,
        valor_premio=1000000,
        data_inicio_vigencia=date(2020, 1, 1),
        data_fim_vigencia=date(2020, 12, 31),
        status=StatusApolice.ATIVA
    )
    assert CalculadoraComissao([apolice]).calcula() == 2000.0


def test_calcula_comissao_viagem():
    apolice = Apolice(
        numero=UUID('12345678123456781234567812345678'),
        tipo=TipoApolice.VIAGEM,
        valor_beneficio=1000000,
        valor_premio=1000000,
        data_inicio_vigencia=date(2020, 1, 1),
        data_fim_vigencia=date(2020, 12, 31),
        status=StatusApolice.ATIVA
    )
    assert CalculadoraComissao([apolice]).calcula() == 200.0
