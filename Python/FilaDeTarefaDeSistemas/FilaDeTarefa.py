# Crie um script em Python que simule uma fila de tarefas do sistema:
# ◆ Inicialize uma lista chamada fila_tarefas contendo: "Backup", "Envio de Logs",
# "Limpeza de Cache".
# ◆ Adicione uma nova tarefa "Atualização de Dependências" ao final da lista.
# ◆ Insira a tarefa de emergência "Correção de Bug Crítico" na primeira posição
# (índice 0).
# ◆ Remova a tarefa concluída "Limpeza de Cache" pelo seu nome/valor.
# ◆ Imprima o total de tarefas restantes e exiba qual tarefa está no primeiro e qual
# está no último índice da lista.
fila_tarefas = ["Backup", "Envio de Logs", "Limpeza De Cache"]
fila_tarefas.append("Atualização de Dependências")
fila_tarefas.insert (0, "Correção de Bug Crítico")
fila_tarefas.remove("Limpeza De Cache")
print("Total de tarefas restantes:", len(fila_tarefas))
print("Primeira tarefa:", fila_tarefas[0])
print("Última tarefa:", fila_tarefas[-1])
print("Fila de tarefas:", fila_tarefas)