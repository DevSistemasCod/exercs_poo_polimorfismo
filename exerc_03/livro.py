from produto import Produto

class Livro(Produto):
    def __init__(self, nome, preco_unitario, quantidade, tema, autor, editora):
        super().__init__(nome, preco_unitario, quantidade)
        self.__tema = tema
        self.__autor = autor
        self.__editora = editora

    @property
    def tema(self):
        return self.__tema

    @property
    def autor(self):
        return self.__autor

    @property
    def editora(self):
        return self.__editora

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tema do Livro: {self.__tema}, Autor: {self.__autor}, Editora: {self.__editora}")

    def calcular_preco_total(self):
        return (super().preco_unitario * super().quantidade) + 10.0
