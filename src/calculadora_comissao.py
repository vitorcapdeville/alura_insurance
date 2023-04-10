from typing import List

from src.modelo.apolice import Apolice
from src.modelo.apolice import TipoApolice


def _calcula_comissao_vida(apolice: Apolice) -> float:
    resultado = 0.005 * apolice.valor_premio + 100
    if apolice.valor_premio > 850000:
        return resultado + 1000
    return resultado


def _calcula_comissao_carro(apolice: Apolice) -> float:
    return 0.0035 * apolice.valor_premio + 75.5


def _calcula_comissao_casa(apolice: Apolice) -> float:
    return 0.002 * apolice.valor_premio


def _calcula_comissao_viagem(apolice: Apolice) -> float:
    return 200.0


class CalculadoraComissao:
    def __init__(self, apolices: List[Apolice]) -> None:
        self._apolices = apolices
        self._regra = {
            TipoApolice.VIDA: _calcula_comissao_vida,
            TipoApolice.CARRO: _calcula_comissao_carro,
            TipoApolice.CASA: _calcula_comissao_casa,
            TipoApolice.VIAGEM: _calcula_comissao_viagem,
        }

    def calcula(self) -> float:
        total = 0
        for apolice in self._apolices:
            total += self._regra[apolice.tipo](apolice)
        return total
