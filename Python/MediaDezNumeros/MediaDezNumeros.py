# Construa uma página/programa onde o usuário digitará dez números e o programa
# somará e calculará a média dos números digitados.
Numeros = []
Soma = 0
for i in range(10):
    Numero = float (input(f"Digite o numero {i+1}: "))
    Numeros.append(Numero)
    Soma = Numero + Soma
print(f"Media dos números digitados: {Soma/10}")