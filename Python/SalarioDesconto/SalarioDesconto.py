# Faça um programa que receba um salário
# e faça um desconto de 6% e informe o valor
Salario = float (input ("Digite seu salário: "))
print (F"Seu desconto 6% do vale transporte é de: {Salario * 0.06}")
print (F"Seu desconto 3% do plano de saúde é de: {Salario * 0.03}")
Descontos = (Salario * 0.03) + (Salario * 0.06) 
print (f"Seu salário com os descontos é no valor de:{Salario - Descontos}")