# 2. Declare uma tupla chamada config_banco contendo os seguintes dados na
# ordem: endereço do host ("192.168.1.100"), porta (5432), nome do banco
# ("producao_db") e flag SSL (True).
# ◆ Exiba o endereço do host e a porta acessando-os pelos seus respectivos índices
# numéricos.
# ◆ No código, tente alterar a porta para 5433.
config_banco = ("192.168.1.100", "5432", "producao_db", "flag SSL")
print(f"Endereço de Host: {config_banco[0]} | Porta: {config_banco[1]}")
# config_banco(1,"5433")