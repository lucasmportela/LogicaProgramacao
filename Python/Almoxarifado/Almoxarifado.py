# 2. O almoxarifado de uma assistência técnica controla suas peças por meio de
# um arquivo chamado estoque_geral.csv (contendo colunas id, produto,
# saldo_atual e estoque_minimo).
# a. Desenvolva um script que leia esse arquivo e filtre apenas os itens cujo
# saldo_atual esteja estritamente abaixo do estoque_minimo.
# b. O resultado filtrado deve ser gravado em um novo arquivo chamado
# pedidos_reposicao.csv, incluindo uma nova coluna calculada chamada
# qtd_comprar, que representa a quantidade necessária para atingir a meta mínima.
import csv
with open("estoque_geral.csv", "r", newline="", encoding="utf-8-sig") as arquivo_entrada:
    leitor = csv.DictReader(arquivo_entrada, delimiter=";")
    leitor.fieldnames = [campo.strip() for campo in leitor.fieldnames]
    campos = ["id", "produto", "saldo_atual", "estoque_minimo", "qtd_comprar"]
    with open("pedidos_reposicao.csv", "w", newline="", encoding="utf-8") as arquivo_saida:
        escritor = csv.DictWriter(
            arquivo_saida,
            fieldnames=campos,
            delimiter=";"
        )
        escritor.writeheader()
        for item in leitor:
            saldo_atual = int(item["saldo_atual"].strip())
            estoque_minimo = int(item["estoque_minimo"].strip())
            if saldo_atual < estoque_minimo:
                qtd_comprar = estoque_minimo - saldo_atual
                item["qtd_comprar"] = qtd_comprar
                escritor.writerow(item)
print("Arquivo pedidos_reposicao.csv gerado com sucesso!")
