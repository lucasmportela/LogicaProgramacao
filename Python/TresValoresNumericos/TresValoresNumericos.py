# Escreva um programa em Python que receba três valores numéricos reais (a,
# b e c) representando os comprimentos dos lados de um triângulo.
# ◆ O programa deve primeiro verificar a condição de existência geométrica:
# a soma de dois lados quaisquer deve ser estritamente maior que o
# terceiro lado.
# ◆ Caso a condição seja atendida, classifique o triângulo em Equilátero,
# Isósceles ou Escaleno.
# ◆ Se as medidas não formarem um triângulo, exiba uma mensagem de
# erro.
a = float (input ("Informe o valor de a: "))
b = float (input ("Informe o valor de b: "))
c = float (input ("Informe o valor de c: "))

if(a + b > c and a + c > b and b + c > a):
    if (a == b == c):
        print("Equilátero")
    elif(a != b != c):
        print("Escaleno")
    elif(a == b or a == c or b == c):
        print("Isósceles")
else:
        print("Erro")