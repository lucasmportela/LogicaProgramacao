# 4. Auditoria de Eficiência Energética de Linha Industrial
# a. Desenvolva um sistema de console para auditar o consumo elétrico de maquinários em uma
# linha de produção industrial. O sistema deve monitorar 5 máquinas utilizando vetores
# unidimensionais.
# i. Regras de Negócio e Requisitos:
# 1. O programa deve preencher duas listas paralelas de tamanho fixo (5
# posições): uma contendo o código numérico de identificação de cada
# máquina e outra contendo o respectivo consumo registrado em quilowatt-
# hora (kWh).
# Visto pós correção Instrutor: Renan Procópio Duarte Aluno:
# 2. Para cada máquina, o sistema deve validar a entrada do consumo através de
# um laço while, garantindo que o valor informado em kWh seja estritamente
# maior que zero antes de passar para a máquina seguinte.
# 3. Solicite ao operador o valor do "Teto Operacional de Consumo" (número real
# único para a verificação de toda a linha industrial).
# 4. Realize uma varredura nas estruturas e identifique:
# a. Quais máquinas ultrapassaram o teto operacional, exibindo seu
# código e o consumo registrado;
# b. O código e o consumo da máquina com o maior consumo absoluto da
# planta;
# c. A média aritmética de consumo de todas as 5 máquinas.
# 5. Caso nenhuma máquina tenha ultrapassado o teto operacional, o programa
# deve exibir a mensagem: "Operação Dentro dos Parâmetros de Eficiência".
# ii. Restrição Técnica: Utilize laços de repetição (for ou while) com controle explícito de
# índices para percorrer as listas de forma sincronizada. É vedado o uso de funções
# prontas da linguagem para busca (como max(), min()), devendo a identificação de
# extremos e acumulações ser realizada puramente por lógica de varredura e variáveis
# de controle. É vedado o uso de estruturas não vistas em sala.

NumIdent = []
Consumo = []
Num = 0
Maior = 0
MaiorNumIdent = 0
Media = 0 
Condicao = True #condição para Operação Dentro dos Parâmetros de Eficiência
for i in range(5):
    kWh = 0
    Num = int(input(f"Informe o número de identificação da máquina {i+1}: "))
    NumIdent.append(Num) #coloca o numero da maquina atual na lista 
    while kWh <= 0: #condição de kWh ser maior que 0
        kWh = float(input("Informe o consumo em kWh: "))
        Consumo.append(kWh) #coloca o valor de kWh da maquina atual na lista
TetoOperacinal = float(input("Informe o valor do Teto Operacional de Consumo: ")) #recebe o valor do Teto Operacional de Consumo
for i in range(5):
    Media += Consumo[i]/len(NumIdent) #calcula a média de consumo
    if Consumo[i] > TetoOperacinal: #verifica se o valor da maquina atual ultrapassou o Teto Operacional de Consumo
        print(f"A máquina de código: {NumIdent[i]} \nUltrapassou o Teto Operacional de Consumo com: {Consumo[i]} ")
        Condicao = False #nega a condição se algum valor tiver ultrapassado o Teto Operacional de Consumo
    if Consumo[i] > Maior: #verifica se o valor de kWh é o maior da lista
        Maior = Consumo[i]  #pega o valor de kWh do maior
        MaiorNumIdent = NumIdent[i] #pega o código da máquina de maior consumo
print(f"O maquinário de código: {MaiorNumIdent} \nPossui o maior consumo absoluto: {Maior} ") #exibe o maior
print(f"Média aritmética de consumo: {Media}") #exibe a média
if (Condicao == True): #exibe Operação Dentro dos Parâmetros de Eficiência se a condição for verdade 
    print("Operação Dentro dos Parâmetros de Eficiência")