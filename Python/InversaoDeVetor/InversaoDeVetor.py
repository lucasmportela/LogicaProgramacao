# Inversão de Vetor
# Construa um programa onde o usuário digitará cinco números para preencher um vetor. O
# programa deve criar um segundo vetor que contenha os mesmos elementos do primeiro,
# porém na ordem inversa, e exibir o novo vetor na tela.

Numeros = []
Invertido = []
for i in range (5):
    Num = float (input(f"Digite o número {i+1}: "))
    Numeros.append(Num)
for i in range(4, -1, -1):
    Invertido.append(Numeros[i])
print(Invertido)