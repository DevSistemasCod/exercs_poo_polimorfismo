def soma_elementos(dados):
    if isinstance(dados, list):
        for num in dados:
            if not isinstance(num, (int, float)):
                return print("A lista deve conter apenas números inteiros ou de ponto flutuante.")
        
        # Se for uma lista de números, retorna a soma dos elementos
        soma = 0
        for num in dados:
            soma = soma + num
        return soma
    
    elif isinstance(dados, str):
        # Se for uma string, retorna a concatenação dos caracteres
        concatenacao = " "
        for char in dados:
            concatenacao =  concatenacao + char + " "
        return concatenacao.strip()  # Remove o espaço extra no final
    
    else:
        return print("Argumento não suportado. A função soma_elementos aceita apenas listas de números ou strings.")
