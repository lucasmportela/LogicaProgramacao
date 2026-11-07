# Monitoramento Térmico de Servidores em Rack
# a. Desenvolva um módulo de console para auditar a temperatura de operação de servidores
# organizados em um rack de data center. O sistema deve gerenciar uma matriz 33, onde cada
# linha representa um rack físico (Rack 0, Rack 1 e Rack 2) e cada coluna representa um sensor
# de temperatura instalado (Sensor 0, Sensor 1 e Sensor 2).
# i. Regras de Negócio e Requisitos:
# 1. O programa deve preencher a matriz 33 com as temperaturas registradas em
# graus Celsius (valores do tipo float).
# 2. Utilize um laço while para validar individualmente a entrada de cada sensor,
# aceitando apenas temperaturas contidas na faixa operacional entre 10.0C e
# 90.0C.
# 3. Para cada um dos três racks (linhas da matriz), o programa deve calcular e
# exibir a temperatura média dos sensores que o compõem.
# 4. Identifique o ponto crítico da estrutura: descubra a maior temperatura
# absoluta registrada em toda a matriz e exiba o seu valor juntamente com as
# coordenadas exatas da sua localização (número do rack/linha e número do
# sensor/coluna).
# 5. Imprima a matriz completa formatada em linhas e colunas.
# 6. Caso a maior temperatura absoluta encontrada seja igual ou superior a 75.0C,
# exiba uma mensagem de "ALERTA: Ponto Crítico de Sobreaquecimento
# Detectado".
# ii. Restrição Técnica: A manipulação da matriz bidimensional deve ser realizada por
# meio de laços for aninhados. É proibida a utilização de funções prontas de biblioteca
# ou funções nativas de buscas (como max(), min()), sendo obrigatória a
# implementação manual de acumuladores e controle condicional de extremos. É
# vedado o uso de estruturas não vistas em sala.

Matriz = []
Temp = 0.0
Maior = 0.0
coordenadai = 0
coordenadaj = 0
TempMediaLista = []
condicao = False
for i in range (3):
    Linha = [] #cria a linha
    TempMedia = 0 #zera a temperatura media atual
    for j in range (3):
        while 10.0 > Temp or Temp > 90.0: #verifica se a temperatura informada está entre 10.0 e 90.0
            Temp = float(input(f"Digite a temperatura em graus Celsius do hack {i} : ")) #recebe a temperatura atual
        if Temp > Maior: #verifica se a temperatura atual é a maior 
            Maior = Temp #receve a temperatura maior
            coordenadai = i #guarda a cordenada de linha
            coordenadaj = j #guarda a cordenada de coluna
        if Temp >= 75.0: #verifica se a temperatura é maior ou igual que 75
            condicao = True #ativa a condicao se for maior
        Linha.append(Temp) #insere os valores da temperatura na linha
        TempMedia += Temp #soma todas as temperaturas da linha
        Temp = 0 #zera o valor atual de temperatura
    Matriz.append(Linha) #insere a linha nas colunas
    TempMediaLista.append(TempMedia/len(Linha)) #calcula a media de temperatura do hack atual
for Linha in Matriz: #exibe a matriz
    print(Linha)
print(f"Temperatura média: {TempMediaLista}") #exibe a temperatura média de cada hack
print(f"Maior temperatura média registrada: {Maior} em { {coordenadai} } { {coordenadaj} }") #exibe a maior temperatura média registrada
if condicao == True: #se a condição for true exibe o alerta
    print("ALERTA: Ponto Crítico de Sobreaquecimento Detectado")
