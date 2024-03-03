from item import Item

class Livro(Item):
    def __init__(self, identificacao, titulo, escritor, tema, editora, num_paginas, ano_publicacao, preco, imposto):
        super().__init__(identificacao, titulo, preco, imposto)
        self.__titulo = titulo
        self.__escritor = escritor
        self.__tema = tema
        self.__editora = editora
        self.__num_paginas = num_paginas
        self.__ano_publicacao = ano_publicacao

    @property
    def titulo(self):
        return self.__titulo

    @property
    def escritor(self):
        return self.__escritor

    @property
    def tema(self):
        return self.__tema

    @property
    def editora(self):
        return self.__editora

    @property
    def num_paginas(self):
        return self.__num_paginas

    @property
    def ano_publicacao(self):
        return self.__ano_publicacao

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Título: {self.__titulo}, Escritor: {self.__escritor}, Tema: {self.__tema}, Editora: {self.__editora}, Número de Páginas: {self.__num_paginas}, Ano de Publicação: {self.__ano_publicacao}")

    def calcular_preco(self):
        return (super().get_preco() + super().get_imposto()) + (0.02 * super().get_preco())
