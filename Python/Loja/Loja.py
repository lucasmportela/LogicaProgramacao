# Desenvolva um programa para registrar as vendas de uma loja ao longo
# do dia. O programa deve processar múltiplos clientes até que o
# operador digite 0 no total de compras para encerrar o expediente.
# ○ Regras de Negócio:
# ■ Para cada cliente, utilize um loop while que leia o valor de cada
# produto comprado, somando-os até que seja digitado -1 (fim da
# compra daquele cliente).
# ■ Se o valor total da compra for superior a R$ 200, aplique 10%
# de desconto; se for superior a R$ 100, aplique 5%; caso
# contrário, sem desconto (utilize if/elif/else).
# ■ Pergunte a quantidade de parcelas (de 1 a 6). Utilize um loop
# for para exibir o cronograma de pagamento, mostrando o valor
# exato de cada parcela mensal.
# ■ Ao final do expediente (quando for digitado 0 para novo cliente),
# exiba o faturamento total acumulado do dia e a quantidade de
# clientes atendidos.

# ○ Restrição: Utilize apenas variáveis numéricas acumuladoras (float e
# int). Não utilize listas.
faturamentototal = 0.0
cliente = 1
produto = 0.0
parcelas = 0
while (cliente != 0):
    total = 0.0
    while (produto != -1):
        total = total + produto
        produto = float (input("Informe o valor do produto: "))
    produto = 0.0
    if (total > 200):
         total = total * 0.9
    elif (total > 100):
        total = total * 0.95
    faturamentototal = total + faturamentototal
    parcelas = int (input("Quantas parcelas serão? (1 a 6) "))
    while (parcelas < 1 or parcelas > 6):
        print("Quantidade de parcelas invalidas")
        parcelas = int (input("Quantas parcelas serão? (1 a 6) "))
    total = total / parcelas
    for i in range(parcelas, 0, -1):
        print(f"{i}º parcela de {total:.2f}")
    cliente = float (input("Novo cliente? "))
print(f"Faturamento total de: {faturamentototal:.2f}") 