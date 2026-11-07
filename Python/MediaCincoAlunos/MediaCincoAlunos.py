# Construa uma página onde o usuário digitará o nome e a média de cinco
# alunos e o programa só aceitará a média do aluno caso ela esteja entre zero
# e dez.
Lista = []
i = 0
for i in range(5):
    Nome = str(input(f"Digite o seu nome aluno {i + 1}: "))
    Media = float(input("Digite a sua média: "))
    while ( Media < 0 or Media > 10):
        print("Media Invalida!")
        Media = float(input("Digite a sua média: "))
    Lista.append([Nome, Media])
print(Lista)

