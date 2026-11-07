# Construa um programa onde o usuário digitará um número e o programa
# completará o número digitado até 0, apenas com números pares.
num = int (input ("informe um número: "))
for i in range(num, -1, -1):
    if (i % 2 == 0):
        print (i)