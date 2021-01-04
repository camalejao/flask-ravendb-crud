class Autor(object):
    def __init__(self, nome):
        self.nome = nome

class Livro(object):
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor