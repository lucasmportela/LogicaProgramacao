# Implemente um programa que receba as temperaturas médias registradas durante
# os 7 dias da semana (armazenadas em um vetor de números reais). O programa
# deve calcular a média aritmética semanal e, em seguida, exibir quais temperaturas
# registradas ficaram estritamente abaixo dessa média.
Lista = []
Total = 0 
Media = 0
for i in range (7):
    num = float (input(f"Digite a temperatura média do dia {i+1} da semana: "))
    Lista.append(num)
Media = sum(Lista)/7
for i in range (7):
    if Lista[i] < Media:
        print(f"A temperatura do dia {i+1} está abaixo da média!")