# Construa um programa onde o usuário digitará cinco números e o programa
# deverá colocar esses números dentro do vetor em ordem crescente.
numeros = []
for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
for i in range(5):
    for j in range(i + 1, 5):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print(f"Ordem Crescente: {numeros}")
