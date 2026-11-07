# Construa um programa/página onde o usuário irá digitar a sua idade e, caso a idade
# seja maior ou igual a 18, terá como resposta “Maior de Idade”. Caso contrário, “Menor
# de Idade”.
Idade = int(input("Digite a sua idade: "))
if Idade >= 18:
    print("Maior de Idade")
else:
    print("Menor de Idade")