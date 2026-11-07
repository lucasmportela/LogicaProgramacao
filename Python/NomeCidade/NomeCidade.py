# Construa um programa/página onde o usuário irá digitar seu nome e cidade
# de onde está digitando.
# ◆ Essas informações passarão para uma função e, caso a cidade seja “Rio de
# Janeiro”, a resposta, além do nome da pessoa, escreverá “Seja Bem-vindo à
# Cidade Maravilhosa”.
# ◆ Caso contrário, exibirá apenas o nome e a cidade digitada (utilizar passagem de
# parâmetros).
nome = input("Digite seu nome: ")
cidade = input("Digite a cidade em que você está: ")
def mensagem(nome, cidade):
    if cidade == "Rio de Janeiro":
        print(f"{nome} Seja Bem-vindo à Cidade Maravilhosa!")
    else:
        print(f"{nome} você está em {cidade}")
mensagem(nome, cidade)

