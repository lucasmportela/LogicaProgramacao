# Construa uma página/programa onde o usuário digitará o nome e o bairro de
# dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem
# alfabética.
Pessoas = []
for i in range(10):
    Nome = input(f"Digite seu nome {i + 1}: ")
    Bairro = input("Digite o seu bairro: ")
    Pessoas.append([Nome, Bairro])
# Ordena por pessoa
Pessoas.sort()
# Ordena por bairro
# Pessoas.sort (key=lambda x: x[1])
print("Pessoas em ordem alfabética:")
for Pessoa in Pessoas:
    print(f"Nome: {Pessoa[0]} | Bairro: {Pessoa[1]}")
