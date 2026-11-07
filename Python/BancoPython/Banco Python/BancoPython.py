from tokenize import Double


nome = " "
conta = 0
saldo = 0.0
dep = 0.0
sair = "N"

nome = str (input("Informe seu nome:"))
conta = int (input("Bem vindo "+ nome +" informe sua conta:"))

while conta != 123:
    print("Conta inválida!")
    conta = int (input ("Informe sua conta:"))

print("1|Consultar")
print("2|Retirar")
print("3|Depositar")

while sair != "S":
    acao = int (input("Escolha uma opção:"))

    if acao == 1:
     print("Seu saldo é: ",saldo)

    elif acao == 2:
       ret = float (input("Valor a ser retirado:"))

       if ret > saldo:
         print("Saldo insuficiente!")

       else:
         saldo = saldo - ret
         print("Retirada concluida: ", saldo)

    elif acao == 3:
      dep = float (input("Valor a ser depositado:"))
      saldo = saldo + dep
      print("Deposito concluido: ", saldo)

    else:
      print("Opção inválida!")
    sair = str (input("Deseja sair? S|N "))
