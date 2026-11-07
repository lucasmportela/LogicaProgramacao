# Criar um script em Python que leia o arquivo vendas_bruto.csv, aplique cálculos e
# regras de negócio para cada pedido e gere um novo arquivo chamado
# faturamento_consolidado.csv.
# a. Para cada linha do arquivo, realize as seguintes operações:
# i. Valor Bruto: quantidade * preco_unitario
# ii. Desconto: 10% do valor bruto se a quantidade >= 5; caso contrário, 0.00
# iii. Valor Líquido: valor_bruto - desconto
# iv. Status: "PREMIUM" se valor_liquido >= 1000.00; caso contrário, "PADRAO"

import csv
with open("vendas_bruto.csv", "r", encoding="utf-8-sig") as arquivo_entrada:
    leitor = csv.DictReader(arquivo_entrada, delimiter=";")
    campos = leitor.fieldnames + [
        "valor_bruto",
        "desconto",
        "valor_liquido",
        "status"
    ]
    with open(
        "faturamento_consolidado.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as arquivo_saida:
        escritor = csv.DictWriter(
            arquivo_saida,
            fieldnames=campos,
            delimiter=";"
        )
        escritor.writeheader()
        for linha in leitor:
            quantidade = int(linha["quantidade"])
            preco_unitario = float(linha["preco_unitario"])
            valor_bruto = quantidade * preco_unitario
            if quantidade >= 5:
                desconto = valor_bruto * 0.10
            else:
                desconto = 0.00
            valor_liquido = valor_bruto - desconto
            if valor_liquido >= 1000.00:
                status = "PREMIUM"
            else:
                status = "PADRAO"
            linha["valor_bruto"] = f"{valor_bruto:.2f}"
            linha["desconto"] = f"{desconto:.2f}"
            linha["valor_liquido"] = f"{valor_liquido:.2f}"
            linha["status"] = status
            escritor.writerow(linha)
print("Arquivo faturamento_consolidado.csv gerado com sucesso!")