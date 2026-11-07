# Crie um script que avalie a concessão de empréstimo com base em três
# variáveis: renda_mensal (float), score (inteiro de 0 a 1000) e possui_restricao
# (booleano).
# ◆ Aprovado: score maior ou igual a 700, renda_mensal a partir de 4000.00
# e sem restrições cadastrais.
# ◆ Análise Manual: Se não for aprovado diretamente, mas a renda_mensal
# for de pelo menos 2500.00, sem restrições, e (score maior ou igual a 500
# ou renda_mensal superior a 6000.00).
# ◆ Recusado: Qualquer outro caso.
RendaMensal = float (input("Informe sua renda mensal: "))
score = int (input("Informe seu score: "))
RestricoesEntrada = str (input("Possui restrições (Verdadeiro/Falso): ")).lower() 
if RestricoesEntrada == "verdadeiro":
    Restricoes = True
else:
    Restricoes = False
if (score >= 700 and RendaMensal >= 4000 and Restricoes == False):
    print("APROVADO")
elif (RendaMensal >= 2500 and Restricoes == False and score >= 500) or (RendaMensal >6000):
    print("APROVADO")
else:
    print("REPROVADO")
