# Construa um programa onde o usuário digitará dez números. O programa
# deverá calcular quais deles são maiores que dez.
listaNum = []
maior = 0
for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    listaNum.append(numero)
    if numero > 10:
        maior += 1
print(f"{maior} números são maiores que 10!")