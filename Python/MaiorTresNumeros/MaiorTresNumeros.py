# Construa um programa onde o usuário digitará três números e o programa
# exibirá, na tela, o maior entre eles.
num1 = float (input("Digite o primeiro número: "))
num2 = float (input("Digite o segundo número: "))
num3 = float (input("Digite o terceiro número: "))

if (num1 > num2 and num1 > num3):
    print(f"{num1} é maior que {num2} e {num3}")
elif (num2 > num1 and num2 > num3):
    print(f"{num2} é maior que {num1} e {num3}")
elif(num3 > num1 and num3 > num1): 
    print(f"{num3} é maior que {num1} e {num2}")
else:
    print("Números iguais")