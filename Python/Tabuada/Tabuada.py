# Construa um programa onde o usuário digitará um valor e o programa
# mostrará, na tela, a tabuada de multiplicação deste número.
num = int (input("Digite um número: "))
for i in range (0, 10):
    tabuada = num * (i + 1)
    print(f"{num} X {i+1} = {tabuada}")
  