sair = False
while not sair:
    entrada = input("Digite a operação (ex: 10 + 5): ")
    operador1, operacao, operador2 = entrada.split()
    operador1 = float(operador1)
    operador2 = float(operador2)
    if operacao == "+":
        resultado = operador1 + operador2
    elif operacao == "-":
        resultado = operador1 - operador2
    elif operacao == "/":
        if operador2 != 0:
            resultado = operador1 / operador2
        else:
            print("Erro: divisão por zero!")
            continue
    elif operacao == "*":
        resultado = operador1 * operador2
    else:
        print("Operação inválida!")
        continue
    print(f"Resultado da operação é: {resultado:.2f}")
    condicao = input("Deseja sair? Sim | Não ").strip().lower()
    if condicao == "sim":
        sair = False