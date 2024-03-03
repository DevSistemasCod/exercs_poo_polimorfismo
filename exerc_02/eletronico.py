from item import Item

class Eletronico(Item):
    def __init__(self, identificacao, nome, preco, imposto):
        super().__init__(identificacao, nome, preco, imposto)

    def exibir_informacoes(self):
        super().exibir_informacoes()

    def calcular_preco(self):
        return (super().get_preco() + super().get_imposto()) + (0.08 * super().get_preco())
