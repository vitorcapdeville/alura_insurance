from json import load


class LerArquivo:
    def __init__(self, arquivo: str):
        self._regra = {
            "json": ler_json,
        }
        self._arquivo = arquivo

    def ler(self) -> dict:
        extensao = self._arquivo.split(".")[-1]
        return self._regra[extensao](self._arquivo)


def ler_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        data = load(f)
    return data
