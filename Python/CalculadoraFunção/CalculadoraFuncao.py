import operator
def calcular(var1, var2, op):
    return op(var1, var2)
operacoes = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul
}
while True:
    operador = input("Escolha uma operação: ")
    if operador == "sair":
        break
    if operador not in operacoes:
        print("Operação inválida!")
        continue
    var1 = float(input("Variável 1: "))
    var2 = float(input("Variável 2: "))
    resultado = calcular(var1, var2, operacoes[operador])
    print("Resultado:", resultado)