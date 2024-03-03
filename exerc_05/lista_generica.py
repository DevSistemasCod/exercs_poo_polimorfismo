class ListaGenerica:
    def __init__(self):
        self.__elementos = []

    def adicionar_elemento(self, elemento):
        # Método de adição independente do tipo de elemento
        self.__elementos.append(elemento)

    def remover_elemento(self, elemento):
        # Método de remoção independente do tipo de elemento
        if elemento in self.__elementos:
            self.__elementos.remove(elemento)
        else:
            print(f"{elemento} não encontrado na lista.")

    def exibir_elementos(self):
        # Método de exibição independente do tipo de elemento
        print("\nElementos na lista:")
        for elemento in self.__elementos:
            print(elemento)
