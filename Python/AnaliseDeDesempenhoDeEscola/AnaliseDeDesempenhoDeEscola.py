# 8: Análise de Desempenho Escolar
# Crie um script para processar o fechamento de notas de uma turma. Os dados estão
# estruturados em um dicionário onde cada chave é a matrícula do estudante e o valor
# é uma lista com as notas obtidas nos 4 bimestres:
# Seu programa deve:
# 1. Iterar sobre o dicionário registro_notas.
# 2. Calcular a média aritmética das notas de cada estudante.
# 3. Gerar um novo dicionário de resultado chamado status_alunos, onde a chave
# é a matrícula e o valor é um dicionário secundário contendo: {"media":
# valor_calculado, "situacao": "Aprovado" se media >= 7.0 senao "Reprovado"}.
# 4. Imprimir o relatório final formatado com matrícula, média final (com duas
# casas decimais) e status.
status_alunos = {}
registro_notas = {"DS2026-01":[7.5,8.0,6.5,9.0], "DS2026-02":[4.0,5.5,3.5,6.0], "DS2026-03":[8.5,9.0,9.5,8.0]}
for matricula, notas in registro_notas.items():
    media = sum(notas) / 4
    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    status_alunos[matricula] = {"media": media, "situacao": situacao}   
for matricula, resultado in status_alunos.items():
    print(f"Matrícula: {matricula}")
    print(f"Média final: {resultado['media']:.2f}")
    print(f"Situação: {resultado['situacao']}")