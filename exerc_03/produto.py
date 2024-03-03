class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self._nome = nome
        self._preco_unitario = preco_unitario
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @property
    def preco_unitario(self):
        return self._preco_unitario

    @property
    def quantidade(self):
        return self._quantidade

    @preco_unitario.setter
    def preco_unitario(self, preco):
        self._preco_unitario = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    def exibir_informacoes(self):
        print(f"Nome: {self._nome}, Preço Unitário: R${self._preco_unitario}, Quantidade: {self._quantidade}")

    def calcular_preco_total(self):
        return (self._preco_unitario * self._quantidade) * 1.05
