# Construa um jogo Quadrado Mágico 3X3, no qual o usuário preencherá o
# vetor com números de um a nove (sem repetir números) e a soma de cada
# linha, coluna e diagonais será igual a quinze.
# dos valores digitados deverão ser calculadas.
Matriz = []
NumerosUsados = []
for i in range(3):
    Linha = []
    for j in range(3):
        while True:
            Valor = int(input(f"Digite o valor [{i}][{j}]: "))
            if Valor < 1 or Valor > 9:
                print("Digite um número entre 1 e 9!")
            elif Valor in NumerosUsados:
                print("Numero já utilizado!")
            else:
                NumerosUsados.append(Valor)
                Linha.append(Valor)
                break
    Matriz.append(Linha)
print("\nQuadrado mágico:")
for Linha in Matriz:
    print(Linha)
Linhas = True
for i in range(3):
    if sum(Matriz[i]) != 15:
        Linhas = False
Colunas = True
for j in range(3):
    Soma = 0
    for i in range(3):
        Soma += Matriz[i][j]
    if Soma != 15:
        Colunas = False
Diagonal1 = Matriz[0][0] + Matriz[1][1] + Matriz[2][2]
Diagonal2 = Matriz[0][2] + Matriz[1][1] + Matriz[2][0]
if Linhas and Colunas and Diagonal1 == 15 and Diagonal2 == 15:
    print("Você formou um Quadrado Mágico!")
else:
    print("Não é um Quadrado Mágico!")