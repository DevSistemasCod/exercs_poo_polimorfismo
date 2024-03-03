from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, turmas, nro_identificacao):
        super().__init__(nome, idade)
        self.__turmas = turmas
        self.__nro_identificacao = nro_identificacao

       # Getters
    @property
    def turmas(self):
        return self.__turmas

    @property
    def nro_identificacao(self):
        return self.__nro_identificacao

    # Setters
    @turmas.setter
    def turmas(self, turmas):
        self.__turmas = turmas

    @nro_identificacao.setter
    def nro_identificacao(self, nro_identificacao):
        self.__nro_identificacao = nro_identificacao

    # Método específico
    def ensinar(self):
        return "Estou ensinando!"

    # Herança por meio do super()
    # polimorfimos - ao adicionarmos o print específicio
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Identificação do Professor: {self.__nro_identificacao}")
