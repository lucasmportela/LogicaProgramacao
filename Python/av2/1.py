
import csv
from decimal import Decimal

try:
    # Abre o arquivo CSV
    with open("pedidos.csv", "r", encoding="utf-8", newline="") as arquivo:

        # Lê o CSV utilizando ponto e vírgula
        leitor = csv.DictReader(arquivo, delimiter=";")

        # Inicializa os acumuladores
        total_bruto = Decimal("0.00")
        total_descontos = Decimal("0.00")
        total_liquido = Decimal("0.00")

        # Variáveis para identificar o maior pedido
        maior_valor_liquido = None
        maior_id = ""
        maior_cliente = ""
        maior_produto = ""
        maior_status = ""

        # Cabeçalho do relatório
        print("\n========== RELATÓRIO DE FATURAMENTO ==========")

        print(
            f"{'ID':<8} {'Cliente':<22} "
            f"{'Bruto':>12} {'Desconto':>12} "
            f"{'Líquido':>12} {'Status':<8}"
        )

        print("-" * 85)

        # Percorre cada pedido do arquivo
        for linha in leitor:

            # Extrai os dados do CSV
            id_pedido = linha["id_pedido"]
            cliente = linha["cliente"]
            produto = linha["produto"]
            quantidade = int(linha["quantidade"])
            preco_unitario = Decimal(linha["preco_unitario"])

            # Calcula o valor bruto
            valor_bruto = quantidade * preco_unitario

            # Aplica o desconto progressivo
            if quantidade >= 10:
                desconto = valor_bruto * Decimal("0.10")

            elif quantidade >= 6:
                desconto = valor_bruto * Decimal("0.05")

            else:
                desconto = Decimal("0.00")

            # Calcula o valor líquido
            valor_liquido = valor_bruto - desconto

            # Classifica o pedido
            if valor_liquido >= Decimal("1000.00"):
                status = "PREMIUM"
            else:
                status = "PADRÃO"

            # Acumula os valores
            total_bruto += valor_bruto
            total_descontos += desconto
            total_liquido += valor_liquido

            # Identifica o maior pedido líquido
            if maior_valor_liquido is None or valor_liquido > maior_valor_liquido:

                maior_valor_liquido = valor_liquido
                maior_id = id_pedido
                maior_cliente = cliente
                maior_produto = produto
                maior_status = status

            # Exibe os dados do pedido
            print(
                f"{id_pedido:<8} {cliente:<22} "
                f"{valor_bruto:>12.2f} "
                f"{desconto:>12.2f} "
                f"{valor_liquido:>12.2f} "
                f"{status:<8}"
            )

        # Exibe o resumo financeiro
        print("-" * 85)

        print("\n========== RESUMO FINANCEIRO ==========")

        print(f"Faturamento Bruto Total: R$ {total_bruto:.2f}")
        print(f"Total de Descontos: R$ {total_descontos:.2f}")
        print(f"Faturamento Líquido Total: R$ {total_liquido:.2f}")

        # Exibe os dados do maior pedido
        print("\n========== MAIOR PEDIDO LÍQUIDO ==========")

        if maior_valor_liquido is not None:

            print(f"ID: {maior_id}")
            print(f"Cliente: {maior_cliente}")
            print(f"Produto: {maior_produto}")
            print(f"Valor Líquido: R$ {maior_valor_liquido:.2f}")
            print(f"Status: {maior_status}")

        else:
            print("Nenhum pedido encontrado no arquivo.")

except FileNotFoundError:
    print("Erro: arquivo pedidos.csv não encontrado!")
    print("Verifique se o arquivo está na mesma pasta do programa.")
