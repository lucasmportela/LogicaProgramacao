# 1. Tendo uma matriz numérica 3x3:
# ◆ substitua múltiplos de 3 por Fus;
# ◆ substitua múltiplos de 5 por Ro;
# ◆ substitua múltiplos de 3 e de 5 por Dah.
Numeros = []
for i in range (3):
    Linha = []
    for j in range (3):
        num = int (input(f"Digite um numero [{i}][{j}]: "))
        if num % 3 == 0 and num % 5 == 0:
            num = "Dah"
        elif num % 3 == 0:
            num = "Fus"
        elif num % 5 == 0:
            num = "Ro"
        Linha.append(num)
    Numeros.append(Linha)
for Linha in Numeros:
    print(Linha)