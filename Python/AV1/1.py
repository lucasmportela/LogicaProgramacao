# Construa um programa em Python que solicite 6 números inteiros ao usuário e os armazene em
# uma lista. Em seguida, percorra a lista para calcular a média aritmética de todos os valores
# informados e determinar a quantidade de números pares presentes. Ao final da execução, o
# programa deve exibir a lista completa, o valor da média calculada e o total de elementos pares
# encontrados.
Numeros = []
ContadorPares = 0
Media = 0
for i in range (6): 
    Num = int(input(f"Informe o numero inteiro {i+1}: "))
    Numeros.append(Num) #Cria a lista de inteiros
for Num in Numeros:
    Media += Num/len(Numeros) #calcula a media
    if Num % 2 == 0: #verifica se o numero atual é par
        ContadorPares += 1 #conta os pares
print(Numeros) #exibe a lista
print(f"Média aritimética: {Media}") #exibe a media aritimética
print(f"Total de elementos pares: {ContadorPares}") #exebe os elementos pares
