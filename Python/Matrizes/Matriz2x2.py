# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.
Matriz = []
soma = 0
contador = 0
for i in range(2):
    Linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        Linha.append(valor)
    Matriz.append(Linha)
for Linha in range (len(Matriz)):
    for Coluna in range (len(Matriz[Linha])):
        soma += Matriz[Coluna][Linha]
        contador += 1
media = soma/contador
print(f"Média: {media} \nSoma: {soma}")
