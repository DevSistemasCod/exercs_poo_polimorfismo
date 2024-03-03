from aluno import Aluno
from  professor import Professor

if __name__ == "__main__":
    # Criando um aluno
    aluno = Aluno("João", 18, ["POO", "LM"], 1234)
    print("Saída Aluno")
    print(aluno.estudar())
    aluno.exibir_informacoes()

    print("")
    # Criando um professor
    professor = Professor("Carlos", 35, ["TurmaAF2", "TurmaAF5"], 1456)
    print("Saída Professor")
    print(professor.ensinar())
    professor.exibir_informacoes()
