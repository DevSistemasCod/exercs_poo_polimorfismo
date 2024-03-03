from lista_generica import ListaGenerica


if __name__ == "__main__":
    # Teste com elementos de diferentes tipos
    lista = ListaGenerica()

    # Adição de elementos
    lista.adicionar_elemento(10)
    lista.adicionar_elemento("Texto")
    lista.adicionar_elemento(3.14)
    lista.adicionar_elemento([1, 2, 3])

    # Exibição de elementos
    lista.exibir_elementos()

    # Remoção de um elemento
    lista.remover_elemento("Texto")

    # Exibição após remoção
    lista.exibir_elementos()
