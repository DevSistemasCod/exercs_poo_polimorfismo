from item import Item

class Vestuario(Item):
    def __init__(self, identificacao, nome, descricao, tamanho, preco, imposto):
        super().__init__(identificacao, nome, preco, imposto)
        self.__descricao = descricao
        self.__tamanho = tamanho

    @property
    def descricao(self):
        return self.__descricao

    @property
    def tamanho(self):
        return self.__tamanho

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Descrição: {self.__descricao}, Tamanho: {self.__tamanho}")

    def calcular_preco(self):
        return (super().get_preco() + super().get_imposto()) + (0.07 * super().get_preco())

