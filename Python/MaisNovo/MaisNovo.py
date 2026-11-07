# Construa um programa que o usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.
Lista = []
MaisNovo = []
for i in range(3):
    Nome = input(f"Digite seu nome {i + 1}: ")
    Idade = int(input("Digite a sua idade: "))
    Lista.append([Nome, Idade])
# MaisNovo = min(Lista, key=lambda pessoa: pessoa[1])
MaisNovo = 0
for i in range(1, len(Lista)):
    if Lista[i][1] < Lista[MaisNovo][1]:
       MaisNovo = i
print(f"{Lista[MaisNovo][0]} é o mais novo!")
