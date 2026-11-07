# Construa um programa que leia 10 números inteiros, armazene-os em uma lista e,
# em seguida, solicite um número adicional para consulta. O sistema deve verificar e
# exibir se esse valor está presente no vetor e a quantidade exata de vezes que ele se
# repete.
Lista = []
Contador = 0
for i in range (10):
    num = int (input(f"Digite o número {i+1}: "))
    Lista.append(num)
Consulta = int (input(f"Digite o número para localizar: "))
for i in range (10):
    if Lista[i] == Consulta:
        Condicao = True
        Contador += 1
    else:
        Condicao = False
if Condicao == True:
    print(f"Número {Consulta} encontrado {Contador} vez(es)!")
else:
    print(f"Número {Consulta} não encontrado!")