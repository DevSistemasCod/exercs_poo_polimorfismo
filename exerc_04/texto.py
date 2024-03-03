class Texto:
    def __init__(self, conteudo):
        self.__conteudo = conteudo

    @property
    def conteudo(self):
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo):
        self.__conteudo = conteudo


    # isinstance é usado para garantir que os operandos 
    # sejam instâncias da classe Texto antes de realizar 
    # as operações de concatenação ou multiplicação. 
    # Isso é uma prática comum para garantir que as operações 
    # específicas para essa classe sejam aplicadas apenas a 
    # objetos compatíveis.

    def __add__(self, outro_texto):
        # Sobrecarga do operador '+'
        if isinstance(outro_texto, Texto):
            return Texto(self.__conteudo + outro_texto.conteudo)
        elif isinstance(outro_texto, str):
            return Texto(self.__conteudo + " " + outro_texto)
        else:
            print("A operação de concatenação é suportada apenas entre objetos da classe Texto ou uma string.")
            return None
        

    def __mul__(self, multiplicador):
        # Sobrecarga do operador '*'
        if isinstance(multiplicador, int):
            return Texto(self.__conteudo * multiplicador)
        else:
            return print("A operação de multiplicação é suportada apenas com um número inteiro.")


    def __str__(self):
        return self.__conteudo
