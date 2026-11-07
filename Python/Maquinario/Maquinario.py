# Um sistema de controle de maquinário pesado deve autorizar a operação
# com base em: cargo (string: "operador" ou "supervisor"), hora_atual (inteiro
# de 0 a 23) e chave_emergencia (booleano). O acesso deve ser concedido se:
# ◆ A chave_emergencia estiver ativa (True), independentemente de
# qualquer outra variável; OU
# ◆ O usuário for "supervisor"; OU
# ◆ O usuário for "operador" E a hora_atual estiver entre 8 e 17 (inclusive).
# ◆ Caso contrário, o sistema deve exibir "Acesso Bloqueado".
cargo = str (input("Informe o seu cargo: ")).lower()
horario = int (input("Informe o horário atual: "))
chave = input("Informe a chave de emergência: (1-Sim/0-Não): ") == "1"
if ((cargo == "supervisor" or cargo == "operador") and (horario >= 8 and horario <=17) or (chave)):
    print("Acesso Permitido")
else :
    print("Acesso Bloqueado")