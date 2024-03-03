from livro import Livro
from eletronico import Eletronico
from vestuario import Vestuario

# Teste com Livro
livro1 = Livro(1, "Dom Casmurro", "Machado de Assis", "Romance", "Editora ABC", 300, 1899, 50.0, 0.1)
print()
livro1.exibir_informacoes()
print("Preço Final: R$",livro1.calcular_preco())

# Teste com Eletrônico
eletronico1 = Eletronico(2, "Smartphone", 800.0, 0.15)
print()
eletronico1.exibir_informacoes()
print("Preço Final: R$",eletronico1.calcular_preco())

# Teste com Vestuário (continuação)
vestuario1 = Vestuario(3, "Camiseta", "Camiseta branca com estampa", "M", 25.0, 0.12)
print()
vestuario1.exibir_informacoes()
print("Preço Final: R$",vestuario1.calcular_preco())

