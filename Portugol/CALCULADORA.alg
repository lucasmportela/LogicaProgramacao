algoritmo "CALCULADORA"

    var
    operacao, sair: caractere
    num1, num2, resultado: real

    inicio
        sair <- "N"
        enquanto (sair != "N") faca
            escreva("Escolha o primeiro número: ")
            leia(num1)

            escreva("Escolha o segundo número: ")
            leia(num2)

            escreva("Escolha uma função | + | * | / | - |")
            leia(operacao)

            se (operacao = "+") entao
                resultado <- num1 + num2
            senao se (operacao = "*") entao
                    resultado <- num1 * num2
            senao se (operacao = "/") entao
                resultado <- num1 / num2
            senao se (operacao = "-") entao
                    resultado <- num1 - num2
            senao 
                resultado <- "ERRO"
            fimse
             fimse
              fimse
               fimse
            escreva("Resultado da operação de ", num1," ", operacao, " " , num2, " = ", resultado)
            escreva("\nDeseja sair S/N?")
            leia(sair)
        fimenquanto
    fim

fimalgoritmo