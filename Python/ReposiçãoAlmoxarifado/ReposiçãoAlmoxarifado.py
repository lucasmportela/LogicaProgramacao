# Construa um sistema de controle de reposição para almoxarifado utilizando vetores
# unidimensionais para gerenciar 6 itens industriais.
# ● Regras de Negócio e Requisitos:
# 1. O programa deve preencher duas listas paralelas de tamanho fixo (6
# posições): uma contendo o código numérico de cada produto e outra
# contendo o respectivo saldo em estoque.
# 2. Solicite ao operador o valor do "Estoque Mínimo de Segurança" (um
# número inteiro único para a verificação de toda a linha).
# 3. Realize uma varredura nas estruturas e identifique:
# ■ Quais produtos estão com saldo estritamente abaixo do estoque
# mínimo, exibindo seu código e quantidade atual;
# ■ O código e a quantidade do item que possui o menor saldo
# absoluto no almoxarifado;
# ■ O código e a quantidade do item com maior saldo absoluto.
# 4. Caso nenhum produto esteja abaixo do estoque de segurança, exiba a
# mensagem "Estoque Operando em Parâmetros Normais".
# ● Restrição Técnica: Utilize laços de repetição (for ou while) com controle de
# índices para percorrer as listas de forma sincronizada.
Saldo = []
Codigo = [] 
Condicao = True
for i in range(6):
        num = int(input(f"Digite o código do produto {i+1}: "))
        Codigo.append(num)
        num = int(input(f"Informe o saldo em estoque do produto {i+1}: "))
        Saldo.append(num)
Minimo = int(input(f"Informe o Estoque Mínimo de Segurança: "))
SaldoMaior = Saldo[0]
CodigoMaior = Codigo[0]
SaldoMenor = Saldo[0]
CodigoMenor = Codigo[0]
for i in range(6):
    if Saldo[i] < Minimo:
        print(f"O produto de código {Codigo[i]} com uma quantidade de: {Saldo[i]} está abaixo do Estoque Mínimo de Segurança!")
        Condicao = False
    if Saldo[i] < SaldoMenor:
        SaldoMenor = Saldo[i]
        CodigoMenor = Codigo[i] 
    if Saldo[i] > SaldoMaior:
        SaldoMaior = Saldo[i]
        CodigoMaior = Codigo[i]
if Condicao == True:
    print("Estoque Operando em Parâmetros Normais!")
print(F"Saldos:  {Saldo}\nCódigos: {Codigo}")
print(f"O produto com o código: {CodigoMenor} tem o menor saldo de: {SaldoMenor}")
print(f"O produto com o código: {CodigoMaior} tem o maior saldo de: {SaldoMaior}")      