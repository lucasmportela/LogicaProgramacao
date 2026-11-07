# Busca de Elemento e Posição
# Construa um programa que peça ao usuário para digitar oito números e os guarde em um
# vetor. Depois, o programa deve pedir um número adicional e informar se esse número está
# presente no vetor. Se estiver, informe em qual posição (índice) ele foi encontrado pela
# primeira vez.

Numeros = []
for i in range (8):
    Num = float (input(f"Digite o número {i+1}: "))
    Numeros.append(Num)
NumAdd = float (input("Digite um número para buscar: "))
for i in range (8):
    if Numeros[i] == NumAdd:
        print(f"O numero {Numeros[i]} aparece no index {i}!")
        break