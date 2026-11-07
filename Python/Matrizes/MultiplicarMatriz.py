# Desenvolva um programa que solicite o preenchimento de uma matriz 3 × 3 com
# números inteiros e, em seguida, peça ao usuário um valor numérico constante
# (escalar). Utilizando laços de repetição aninhados, o programa deve multiplicar cada
# elemento da matriz original por esse valor escalar e exibir a matriz resultante
# formatada em linhas e colunas.Matriz = []
Matriz = []
for i in range(3):
    Linha = []
    for j in range(3):
        num = int(input(f"Digite o valor [{i}][{j}]: "))
        Linha.append(num)
    Matriz.append(Linha)
Valor = int (input("Infome um valor numérico constante: "))
for i in range(3):
    for j in range(3):
        Matriz[i][j] = Matriz[i][j] * Valor
for i in range(3):
    for j in range(3):
        print(Matriz[i][j], end="\t")
    print()