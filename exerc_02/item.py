class Item:
    def __init__(self, identificacao, nome, preco, imposto):
        self._identificacao = identificacao
        self._nome = nome
        self._preco = preco
        self._imposto = imposto

    
    def get_identificacao(self):
        return self._identificacao

    
    def get_nome(self):
        return self._nome

    
    def get_preco(self):
        return self._preco

   
    def get_imposto(self):
        return self._imposto

    
    def set_preco(self, preco):
        self._preco = preco

    def exibir_informacoes(self):
        print(f"Identificação: {self._identificacao}, Nome: {self._nome}, Preço: {self._preco}, Imposto: {self._imposto * 100}%")

    def calcular_preco(self):
        return ((self._preco + self._imposto) + (0.015 * self._preco))
