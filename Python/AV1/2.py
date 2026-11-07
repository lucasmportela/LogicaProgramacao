# Desenvolva um programa em Python que leia 10 números inteiros e os armazene em um vetor
# original. A partir dessa estrutura, crie duas novas listas independentes: uma lista denominada pares,
# contendo cada número par do vetor original multiplicado por 3, e uma lista denominada ímpares,
# contendo os números ímpares mantidos com seus valores inalterados. Ao final, o programa deve
# exibir o vetor original, os dois novos vetores resultantes e a contagem exata de elementos alocados
# em cada um deles.
Numeros = []
Pares = []
Impares = []
for i in range (10):
    Num = int (input(f"Digite o número {i+1}: "))
    Numeros.append(Num) #Cria o vetor original
for Num in Numeros: 
    if Num % 2 == 0: #verifica se é par
        Pares.append(Num*3) #Coloca os pares em uma lista separada e multiplica os pares por 3
    else:
        Impares.append(Num)  #Coloca os impares em uma lista separada
print(f"Vetor original: {Numeros}") #mostra o vetor original
print(f"Lista números pares: {Pares} \nQuantidade de elementos alocados: {len(Pares)}") #mostra a lista de pares e sua quantidade
print(f"Lista números Impares: {Impares} \nQuantidade de elementos alocados: {len(Impares)}") #mostra a lista de impares e sua quantidade