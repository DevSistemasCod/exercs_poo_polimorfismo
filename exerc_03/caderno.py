from produto import Produto

class Caderno(Produto):
    def __init__(self, nome, preco_unitario, quantidade, identificacao, num_paginas, fabricante):
        super().__init__(nome, preco_unitario, quantidade)
        self.__identificacao = identificacao
        self.__num_paginas = num_paginas
        self.__fabricante = fabricante

    @property
    def identificacao(self):
        return self.__identificacao

    @property
    def num_paginas(self):
        return self.__num_paginas

    @property
    def fabricante(self):
        return self.__fabricante

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Identificação do Caderno: {self.__identificacao}, Número de Páginas: {self.__num_paginas}, Fabricante: {self.__fabricante}")

    def calcular_preco_total(self):
        return (super().preco_unitario * super().quantidade) * 1.10
       
