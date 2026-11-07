# Desenvolva um script que abra o arquivo alunos.txt gerado no exercício
# anterior. O programa deve exibir na tela os nomes dos alunos formatados em
# ordem numérica (ex: 1 - Aluno) e, ao final, imprimir o total de registros lidos.
total = 0
with open("alunos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        total += 1
        print(f"{total} - {linha.strip()}")
print(f"Total de registros lidos: {total}")