# 1. O setor de segurança da informação de uma empresa precisa rastrear as
# ações dos funcionários no sistema corporativo.
# i. Crie uma função em Python chamada registrar_evento(usuario, acao, status) que
# receba o nome do usuário, a ação executada (ex: LOGIN, SAQUE, EXCLUSAO)
# e o status da operação (SUCESSO ou FALHA).
# ii. O programa deve anexar cada registro em uma nova linha no arquivo
# auditoria_sistema.log, contendo a data e a hora do momento exato em que a ação
# ocorreu, sem sobrescrever os registros anteriores.
from datetime import datetime
def registrar_evento(usuario, acao, status):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("auditoria_sistema.log", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{data_hora}] Usuário: {usuario} | Ação: {acao} | Status: {status}\n")
registrar_evento("Lucas", "LOGIN", "SUCESSO")
registrar_evento("Maria", "EXCLUSAO", "FALHA")
registrar_evento("João", "SAQUE", "SUCESSO")
print("Eventos registrados com sucesso!")
    