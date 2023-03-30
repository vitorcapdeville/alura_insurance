from apolice import Apolice, TipoApolice
from typing import List


def _calcula_comissao_vida(apolice: Apolice):
    if apolice.valor_beneficio > 850000:
        return 0.005 * apolice.valor_beneficio + 100
    else:
        return 0.005 * apolice.valor_beneficio


def _calcula_comissao_carro(apolice: Apolice):
    return 0.0035 * apolice.valor_beneficio + 75.5


def _calcula_comissao_casa(apolice: Apolice):
    return 0.002 * apolice.valor_beneficio


def _calcula_comissao_viagem(apolice: Apolice):
    return 200


class CalculadoraComissao:
    def __init__(self, apolices: List[Apolice]) -> None:
        self._apolices = apolices
        self._regra = {
            TipoApolice.VIDA: _calcula_comissao_vida,
            TipoApolice.CARRO: _calcula_comissao_carro,
            TipoApolice.CASA: _calcula_comissao_casa,
            TipoApolice.VIAGEM: _calcula_comissao_viagem,
        }

    def calcula(self):
        total = 0
        for apolice in self._apolices:
            total += self._regra[apolice.tipo](apolice)
        return total
