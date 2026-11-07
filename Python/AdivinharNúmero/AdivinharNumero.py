# O programa irá sortear um número entre 1 e 100, e temos que adivinhar qual
# foi esse número.
import random
num = random.randint(1, 100)
print(num)
tentativa = int(input("Adivinhe o número: "))
if (tentativa == num):
    print("Acertou!")
else:
    print("Errou!")     