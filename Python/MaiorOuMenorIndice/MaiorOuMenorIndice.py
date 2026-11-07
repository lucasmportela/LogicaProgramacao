# Maior e Menor Valor com Índices
# Construa um programa onde o usuário digitará dez números inteiros. O programa deve
# identificar qual é o maior e qual é o menor número digitado, exibindo também a posição
# (índice) em que cada um deles se encontra no vetor.
Numeros = []
for i in range(10):
    Num = int(input(f"Digite o número {i + 1}: "))
    Numeros.append(Num)
Menor = Numeros[0]
Maior = Numeros[0]
IndiceMenor = 0
IndiceMaior = 0
for i in range(1, 10):
    if Numeros[i] < Menor:
        Menor = Numeros[i]
        IndiceMenor = i
    if Numeros[i] > Maior:
        Maior = Numeros[i]
        IndiceMaior = i
print(f"Maior número: {Maior} e seu índice: {IndiceMaior}")
print(f"Menor número: {Menor} e seu índice: {IndiceMenor}")
