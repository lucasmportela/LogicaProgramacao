cond = 0 
while cond != 1:
        print("1|Soma")
        print("2|Subtração")
        print("3|Divisão")
        print("4|Multiplicação")
        operacao = int (input("Escolha uma operação: "))

        ope1 = float(input("Operador 1: "))
        ope2 = float(input("Operador 2: "))

        if operacao == 1:
          res = float(ope1) + float(ope2)
          cond = 1

        elif operacao == 2:
          res = float(ope1) - float(ope2)
          cond = 1

        elif operacao == 3:
          res = float(ope1) / float(ope2)
          cond = 1

        elif operacao == 4:
          res = float(ope1) * float(ope2)
          cond = 1

        else:
            print("Operação invalida")     

print("Resultado é:", res)