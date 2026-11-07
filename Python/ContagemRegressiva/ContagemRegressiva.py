# Construa uma página/programa onde o usuário digitará um número, a página fará
# uma contagem regressiva até zero e, depois, contará de zero até o número que o
# usuário digitou.
Numero = int (input("Digite um número: "))
def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)
def progressiva(x):
    if x == Numero:
            print("Acabou")
    else:
        print(x)
        progressiva(x+1)
contagem = regressiva(Numero)
contagem = progressiva(0)
