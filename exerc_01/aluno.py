from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, disciplinas, nro_matricula):
        super().__init__(nome, idade)
        self.__disciplinas = disciplinas
        self.__nro_matricula = nro_matricula

    # Getters
    @property
    def disciplina(self):
        return self.__disciplinas

    @property
    def nro_matricula(self):
        return self.__nro_matricula

    # Setters
    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplinas = disciplina

    @nro_matricula.setter
    def nro_matricula(self, nro_matricula):
        self.__nro_matricula = nro_matricula

    # Método específico
    def estudar(self):
        return "Estou estudando!"

    # Herança por meio do super()
    # polimorfimos - ao adicionarmos o print específicio
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Identificação do Aluno: {self.__nro_matricula}")
