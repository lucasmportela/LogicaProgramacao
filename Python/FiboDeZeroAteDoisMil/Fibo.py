# Construa um programa que exiba a sequência de Fibonacci de zero até dois
# mil.
contagem = 0
result = 0
while (contagem != 1597):
    def fibo(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2)
    result = result + 1
    contagem = fibo(result)
    print (contagem)
    