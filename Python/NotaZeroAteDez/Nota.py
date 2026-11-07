# Construa um programa que só aceite notas escolares entre zero e dez
# (treinamento para controle de erros).
sair = "não"
while (sair != "sim"):
    try:
        nota = int (input("Informe a sua nota (0 até 10): "))
        if (0 <= nota <= 10):
            print(f"Sua nota é: {nota}")
        else:
            print("Erro: a nota deve estar entre 0 e 10")
    except ValueError:
        print("Erro: entrada inválida. Digite um número inteiro.")
    sair = str (input ("Deseja sair? (sim/não): ")).strip().lower()