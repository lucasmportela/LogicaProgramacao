# Dada uma matriz 3x3 com números inteiros, descubra qual é o maior valor
# dentro dela e informe exatamente em qual linha e coluna ele foi encontrado.
Numeros = []
maior = 0
indice = []
for i in range (3):
    Linha = []
    for j in range (3):
        num = int (input(f"Digite um numero [{i}][{j}]: "))
        Linha.append(num)
        if num > maior:
            maior = num
            indice = [i, j]
    Numeros.append(Linha)
for Linha in Numeros:
    print(Linha)
print(f"O maior número é: {maior} localizado no indice: {indice}")