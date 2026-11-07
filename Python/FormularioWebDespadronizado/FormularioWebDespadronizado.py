# 3. Um formulário web despadronizado gerou um arquivo de texto bruto
# chamado emails_brutos.txt com e-mails digitados pelos usuários.
# i. Esse arquivo contém espaçamentos indesejados nas pontas, caracteres
# maiúsculos misturados e linhas vazias acidentais.
# ii. Escreva um script em Python que leia esse arquivo linha por linha, descarte linhas
# em branco, converta todos os e-mails válidos para letras minúsculas (lowercase),
# remova espaços extras nas pontas e salve a lista limpa e padronizada em um
# novo arquivo chamado emails_padronizados.txt.
with open("emails_brutos.txt", "r", encoding="utf-8") as arquivo_entrada:
    emails_limpos = []
    for linha in arquivo_entrada:
        email = linha.strip().lower()
        if email:
            emails_limpos.append(email)
with open("emails_padronizados.txt", "w", encoding="utf-8") as arquivo_saida:
    for email in emails_limpos:
        arquivo_saida.write(email + "\n")
print("Arquivo emails_padronizados.txt gerado com sucesso!")
