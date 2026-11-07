# Crie um dicionário chamado produto contendo as chaves: "sku", "nome",
# "preco", "quantidade" e "ativo".
# ◆ Preencha com valores fictícios de um item de informática (ex.: SKU "MEM-16GB",
# preço 280.00, quantidade 15, ativo True).
# ◆ Aplique uma atualização no dicionário: altere a chave "preco" para sofrer um
# reajuste de 10% e atualize a "quantidade" para 12.
# ◆ Imprima no console o nome do produto e o novo preço acessando diretamente as
# chaves correspondentes.
produto = {"sku":"MEM-16GB","nome":"Memória RAM 16GB","preco":280.00,"quantidade":15,"ativo":True}
produto ["preco"] = produto["preco"]* 1.10
produto ["quantidade"] = 12
print("Nome do produto:", produto["nome"])
print("Novo preço: R$", round(produto["preco"], 2))

