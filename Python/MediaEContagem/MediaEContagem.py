# Média e Contagem Acima da Média
# Construa um programa onde o usuário digitará seis notas (números reais). O programa
# deve calcular a média dessas notas e, em seguida, exibir quantas e quais notas ficaram
# estritamente acima da média calculada.
Notas = []
for i in range (6):
    Nota = float (input(f"Digite a sua nota {i+1}: "))
    Notas.append(Nota)
Media = sum(Notas) / 6
Contagem = 0
for i in range (6):
    if Notas[i] >= Media:
        print(f"A nota {Notas[i]} esta acima da média!")
        Contagem += 1
print(f"{Contagem} notas estão acima da média!")