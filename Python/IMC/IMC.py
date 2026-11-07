# Construa uma página onde o usuário digitará o seu peso e a sua altura e o programa
# irá calcular o IMC (peso/altura). Caso o IMC seja maior que 25 exibirá, na tela, “Acima
# do Peso Ideal”. Caso contrário, “Peso OK”.
Peso = float(input("Informe o seu peso: "))
Altura = float(input("Informe a sua altura: "))
if Peso/(Altura*Altura) > 25:
    print("Acima do Peso Ideal")
else:
    print("Peso ok") 