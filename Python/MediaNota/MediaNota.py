# Construa um programa onde o usuário digitará duas notas escolares e o
# programa irá calcular a média e, caso seja menor que 6, exibirá na tela:
# “Aluno Reprovado”. Caso seja maior ou igual a 6 exibirá na tela: “Aluno
# Aprovado”.
nota1 = float (input("Digite sua primeira nota: "))
nota2 = float (input("Digite sua segunda nota: "))
media = float
media = (nota1 + nota2)/2
if(media < 6):
    print(f"{media} Aluno Reprovado")
else:
    print(f"{media} Aluno aprovado")