# 4. A secretaria de uma escola técnica disponibilizou o arquivo notas_turma.csv
# com as colunas matricula, aluno, nota1 e nota2.
# i. Construa um programa em Python que leia esses registros e calcule a média
# aritmética de cada aluno.
# ii. Se a média final for maior ou igual a 7.0, o aluno recebe a situação
# "APROVADO"; caso contrário, recebe "REPROVADO".
# iii. O programa deve gerar o arquivo boletim_final.csv contendo as notas originais, a
# média final arredondada para uma casa decimal e a situação acadêmica
# calculada.
import csv
with open("notas_turma.csv", "r", newline="", encoding="utf-8-sig") as arquivo_entrada:
    leitor = csv.DictReader(arquivo_entrada, delimiter=";")
    leitor.fieldnames = [campo.strip() for campo in leitor.fieldnames]
    campos = ["matricula", "aluno", "nota1", "nota2", "media_final", "situacao"]
    with open("boletim_final.csv", "w", newline="", encoding="utf-8") as arquivo_saida:
        escritor = csv.DictWriter(
            arquivo_saida,
            fieldnames=campos,
            delimiter=";"
        )
        escritor.writeheader()
        for aluno in leitor:
            nota1 = float(aluno["nota1"])
            nota2 = float(aluno["nota2"])
            media = (nota1 + nota2) / 2
            if media >= 7.0:
                situacao = "APROVADO"
            else:
                situacao = "REPROVADO"
            aluno["media_final"] = f"{media:.1f}"
            aluno["situacao"] = situacao
            escritor.writerow(aluno)
print("Arquivo boletim_final.csv gerado com sucesso!")
