# Construa um programa onde o usuário digitará sete números e o programa
# escreverá, na tela, quantos deles são pares e quantos são ímpares.
listaNum = []
impar = 0 
par = 0 
for i in range(7):
    numero = int(input(f"Digite o número {i + 1}: "))
    listaNum.append(numero)
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"{par} números são pares e {impar} números são impares")