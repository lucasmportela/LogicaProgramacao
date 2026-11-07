# Substituição de Valores Negativos
# Construa um programa onde o usuário digitará dez números inteiros para preencher um
# vetor. Em seguida, o programa deve percorrer o vetor e substituir todos os números
# negativos por zero, exibindo o vetor final na tela.
Numeros = []
for i in range (10):
    Num = int (input(f"Digite o número {i+1}: "))
    Numeros.append(Num)
for i in range (10):
    if Numeros[i] < 0:
        Numeros[i] = 0
print(Numeros)