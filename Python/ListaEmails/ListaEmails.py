# Um formulário web recebeu múltiplos cadastros com e-mails repetidos:
# ◆ Converta a lista emails_brutos em um conjunto (set) chamado emails_unicos para
# eliminar as redundâncias.
# ◆ Adicione um novo e-mail "marcos@tech.com" ao conjunto.Verifique, por meio de
# um teste lógico (in), se o e-mail "carlos@provedor.com" consta no conjunto e
# exiba uma mensagem informativa no terminal.
# ◆ Exiba a quantidade total de e-mails válidos e únicos registrados.
emails_brutos = [
    "ana@empresa.com",
    "carlos@provedor.com",
    "ana@empresa.com",
    "beatriz@servico.com",
    "carlos@provedor.com",
    "daniel@tech.com"
]
emails_unicos = set(emails_brutos)
emails_unicos.add("marcos@tech.com")
if "carlos@provedor.com" in emails_unicos:
    print("Email encontrado")
print("Total de e-mails válidos e únicos registrados:", len(emails_unicos))
