# Construa um programa que exiba a sequência de Fibonacci
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
contagem = fibo(4)
print (contagem)