# Construa um programa onde o usuário digitará dois números, utilizando
# passagem de parâmetros e, dentro da função, irá calcular a soma desses
# dois números.
def soma(a, b):
    return a + b
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = soma(num1, num2)
print(f"A soma dos números é: {resultado}")
