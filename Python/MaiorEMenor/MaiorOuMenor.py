# construa um programa que receba dois valores
# e compare se um é maior ou menor que o outro
# ou igual
num1 = float (input("informe o número 1: "))
num2 = float (input("informe o número 2: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num2 > num1:
    print(f"{num2} é maior que {num1}")
else:
    print(f"{num1} e {num2} são iguais")
