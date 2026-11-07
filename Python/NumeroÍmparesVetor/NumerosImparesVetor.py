# Construa um programa que receba 8 números inteiros e os guarde em um vetor. Em
# seguida, crie um segundo vetor de mesmo tamanho no qual os números ímpares do
# vetor original sejam multiplicados por 2 e os números pares permaneçam
# inalterados. Ao final, exiba os dois vetores.
Lista = []
for i in range (8):
    num = int (input(f"Digite o número {i+1}: "))
    Lista.append(num)
Impares = []
for i in range (8):
    if Lista[i] % 2 == 0:
        Impares.append(Lista[i]) 
    else:
        Impares.append(Lista[i]*2) 
print(Lista)
print(Impares)