# Desenvolva um módulo de console para auditar o consumo de combustível de
# veículos que retornam à base operacional ao longo de um turno de trabalho.
# ● Regras de Negócio e Requisitos:
# 1. O programa deve processar múltiplos veículos de forma contínua até
# que o operador digite 0 na quilometragem percorrida para sinalizar o
# fim do expediente.
# 2. Para cada veículo válido, solicite a distância percorrida (em km) e a
# quantidade de combustível consumida (em litros). Utilize um laço while
# para validar que o volume de combustível seja estritamente maior que
# zero antes de prosseguir com o cálculo.
# 3. Calcule o consumo médio (km/l) e classifique o desempenho do
# veículo:
# ■ Consumo maior ou igual a 12. 0km/l: "Econômico";
# ■ Consumo entre 9. 0km/l e 11. 9km/l: "Padrão";
# ■ Consumo inferior a 9. 0km/l: "Alto Consumo".
# 4. Exiba a classificação do veículo processado.
# 5. Ao encerrar o expediente, exiba:
# ■ O total de veículos auditados;
# ■ A quilometragem total acumulada pela frota;
# ■ A média geral de consumo da frota no turno.
# ● Restrição Técnica: O processamento deve utilizar unicamente
# acumuladores e variáveis numéricas primitivas (float e int), sem o uso de
# listas ou estruturas compostas.
consumo = 0
contadorkm = 0
contador = 0
media = 0
km = float(input("Informe a distãncia em km percorrida: "))
while km != 0:
    litro = 0
    while litro == 0:
        litro = float(input("Informe a quantidade de combustível em litros consumida: "))
    consumo = km / litro
    if consumo >= 12:
        print("Econômico")
    elif 9 <= consumo < 12:
        print("Padrão")
    elif(consumo < 9):
        print("Alto Consumo")
    media += consumo
    contador += 1
    contadorkm += km
    km = float(input("Informe a distãncia em km percorrida: "))
print(f"Quantidade de veículos auditados: {contador}")
print(f"Media geral de consumo da frota no turno: {media}")
print(f"Quilometragem total da frota: {contadorkm}")