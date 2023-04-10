from json import load

from src.modelo.componente_seguro import ComponenteSeguro


class LerArquivo:
    def __init__(self, arquivo: str):
        self._regra = {
            "json": ler_json,
        }
        self._arquivo = arquivo

    def ler(self) -> dict:
        extensao = self._arquivo.split(".")[-1]
        return self._regra[extensao](self._arquivo)


def criar_classe(class_obj: ComponenteSeguro, arquivo: str) -> object:
    data = LerArquivo(arquivo).ler()
    return class_obj.from_dict(data)


def separa_nome_sobrenome(nome_completo: str) -> tuple[str, str]:
    nome_completo = nome_completo.strip()
    if " " in nome_completo:
        primeiro_nome, sobrenome = nome_completo.split(" ", 1)
        return primeiro_nome, sobrenome
    else:
        return nome_completo, ""


def ler_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        data = load(f)
    return data
