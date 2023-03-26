class Contato:
    def __init__(self, celular, telefone_residencial, telefone_comercial, email):
        self._celular = celular
        self._telefone_residencial = telefone_residencial
        self._telefone_comercial = telefone_comercial
        self._email = email

    def __str__(self):
        return (
            f"celular: {self._celular}, telefone_residencial: {self._telefone_residencial}, telefone_comercial: "
            f"{self._telefone_comercial}, email: {self._email}"
        )
