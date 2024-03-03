from caderno import Caderno
from livro import Livro

# Teste com Caderno
caderno1 = Caderno("Caderno Grande", 15.0, 2, 101, 200, "Faber Castell")
caderno1.exibir_informacoes()
print(f"Preço Total: R${caderno1.calcular_preco_total():.2f}\n")

# Teste com Livro
livro1 = Livro("Dom Casmurro", 30.0, 1, "Romance", "Machado de Assis", "Editora XYZ")
livro1.exibir_informacoes()
print(f"Preço Total: R${livro1.calcular_preco_total():.2f}\n")
