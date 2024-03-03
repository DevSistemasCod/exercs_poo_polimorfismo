from texto import Texto

# Teste de concatenação
texto1 = Texto("Olá")
texto2 = Texto("mundo")
concatenado = texto1 + texto2
print(f"Concatenado: {concatenado}")

# Teste de concatenação com espaço
concatenado_com_espaco = texto1 + "" + texto2
print(f"Concatenado com espaço: {concatenado_com_espaco}")

# Teste de multiplicação
repetido = texto1 * 3
print(f"Repetido 3 vezes: {repetido}")
