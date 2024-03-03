from polimorfimos_ad_hoc import soma_elementos

if __name__ == "__main__":
    # Teste de uso da função
    lista_numeros = [1, 2, 3, 4, 5]
    resultado_numeros = soma_elementos(lista_numeros)
    print(f"Soma dos números na lista: {resultado_numeros}")

    texto = "Hello"
    resultado_texto = soma_elementos(texto)
    print(f"Concatenação dos caracteres na string come espaço: {resultado_texto}")
