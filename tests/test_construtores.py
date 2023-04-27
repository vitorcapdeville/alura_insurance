from datetime import date
from unittest.mock import mock_open
from unittest.mock import patch

from src.leitor_arquivo import LerArquivo
from src.modelo.apolice import Apolice


def test_ler_arquivo_retorna_dicionario_corretamente():
    leitor = LerArquivo("arquivo.json")
    conteudo_arquivo = '{"nome": "João"}'
    with patch("builtins.open", mock_open(read_data=conteudo_arquivo)):
        dados = leitor.ler()
        assert dados['nome'] == 'João'


def test_classe_eh_criada_corretamente_a_partir_de_json():
    conteudo_arquivo = """
    {
      "numero": "12345678123456781234567812345678",
      "tipo": "VIDA",
      "valor_premio": 100,
      "valor_beneficio": 100000,
      "data_inicio_vigencia": "2019-01-01",
      "data_fim_vigencia": "2019-12-31",
      "status": "ATIVA"
    }
    """
    with patch("builtins.open", mock_open(read_data=conteudo_arquivo)):
        dados = LerArquivo("arquivo.json").ler()
        apolice = Apolice.parse_obj(dados)
        assert apolice.data_inicio_vigencia == date(2019, 1, 1)
        assert apolice.valor_beneficio == 100000
