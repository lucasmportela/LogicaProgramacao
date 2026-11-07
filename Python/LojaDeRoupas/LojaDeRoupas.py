# ➔ Uma loja de roupas quer fechar o balanço do fim de semana. Eles anotaram as vendas
# de 3 produtos ao longo de 3 dias (sexta, sábado e domingo) em uma matriz.
# ➔ O que o programa deve fazer:
# ◆ Somar as vendas de cada produto ao longo dos três dias (soma de cada linha).
# ◆ Descobrir qual produto teve o maior total de vendas no fim de semana.
Produtos = []
Total = []
for i in range (3):
    Linha = []
    for j in range (3):
        num = int(input(f"Digite a quantidade vendida do produto {i+1} no dia {j+1}: "))
        Linha.append(num)
    Produtos.append(Linha)
for i in range (3):
    Soma = 0
    for j in range(3):
        Soma += Produtos[i][j]
    Total.append(Soma)
for i in range(3):
    print(f"O produto {i+1} vendeu no total: {Total[i]}")
Maior = max(Total)
ProdutoMaior = Total.index(Maior) + 1
print(f"O produto {ProdutoMaior} teve o maior total de vendas, com {Maior} unidades.")