# Pegue uma matriz 3x3 e gere uma nova matriz onde as linhas da original
# viram as colunas da nova.
Numeros = []
Invertido = []
for i in range (3):
    Linha = []
    for j in range (3):
        num = int (input(f"Digite um numero [{i}][{j}]: "))
        Linha.append(num)
    Numeros.append(Linha)
for i in range (3):
    Linha = []
    for j in range (3):
         Linha.append(Numeros[j][i])
    Invertido.append(Linha)
for Linha in Invertido:
    print(Linha)    