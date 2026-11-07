# Crie um sistema de autenticação de terminal que valida a segurança da
# senha cadastrada e gerencia o acesso do usuário.
# ○ Regras de Negócio:
# ■ Primeiro, o usuário define uma senha numérica de 4 dígitos.
# Use um loop while que continue solicitando até que o valor
# digitado esteja rigorosamente entre 1000 e 9999.
# ■ Em seguida, o sistema entra em modo de bloqueio e pede a
# confirmação da senha para liberar o sistema, permitindo até 3
# tentativas via loop while.
# ■ Dentro do processo de tentativa:
# ● Se a senha estiver correta: encerre imediatamente o loop
# de tentativas.
# ● Se estiver incorreta: informe quantas chances ainda
# restam usando if/elif/else.
# ■ Se o acesso for liberado com sucesso, use um loop for para
# simular uma contagem regressiva de inicialização do sistema
# (de 5 até 1).
# ■ Se as 3 tentativas falharem, exiba a mensagem de conta
# bloqueada.
# ○ Restrição: Todas as validações devem ser puramente lógicas e
# aritméticas, sem manipulação de listas ou estruturas compostas.
import time
senha = 0 
tentativa = 2
while (senha < 1000 or senha >= 10000):
    senha = int (input("Informe uma senha: "))
while (tentativa != -1):
    resposta = int (input("Digite a senha: "))
    if (resposta == senha):
        print("Acesso concedido")
        break   
    else:
        tentativa = tentativa - 1
        print(f"Acesso negado: {tentativa} restante")
        if (tentativa == 0):
            print("Conta bloqueada")
print("Sistema inicializando em:")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Sistema inicializado :D")
