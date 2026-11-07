# Construa um programa/página onde o usuário irá criar uma classe com nome, idade e
# altura (em centímetros). O programa dirá se a pessoa é maior ou menor de idade.
class Dados:
    def __init__(self, Nome, Idade, Altura):
        self.Nome= Nome
        self.Idade = Idade
        self.Altura = Altura
    def Verificar(self):
        if self.Idade >= 18:
            return ("maior de idade")
        else:
            return ("menor de idade")
for i in range(5):
    Nome = str (input(f"Digite seu nome {i+1}: "))
    Idade = int (input("Digite sua idade: "))
    Altura = float(input("Digite sua altura: "))
    Pessoa = Dados(Nome, Idade, Altura)
    print(f"{Nome} você tem {Altura:.2f} de altura é {Pessoa.Verificar()}")
