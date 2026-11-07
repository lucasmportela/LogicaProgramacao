# Desenvolva um programa que solicite dois números inteiros representando os
# limites de um intervalo [A, B] (garantindo que A ≤ B). O programa deve iterar sobre
# o intervalo utilizando uma estrutura de repetição e calcular a soma apenas dos
# números ímpares presentes nele, exibindo o resultado final ao usuário.
Soma = 0 
A = int (input("Digite o valor de A: "))
B = int (input("Digite o valor de B: "))
if A <= B:
    while(B >= A):
        if B % 2 != 0:
            Soma = B + Soma
        B -= 1
    print(Soma)
else:
    print("Intervalo inválido!")