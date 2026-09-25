class Biblioteca:
    nome_da_biblioteca = str
    situacao = bool
    def __init__(self, nome_da_biblioteca, situacao):
        self.nome_da_biblioteca = nome_da_biblioteca
        self.situacao = situacao
    def __str__(self):
        return self.nome_da_biblioteca


biblioteca_senai = Biblioteca('Biblioteca do senai', True)
print(biblioteca_senai)