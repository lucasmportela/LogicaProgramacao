# Construa um jogo de pedra, papel e tesoura.
import random
jogadas = ["pedra", "papel", "tesoura"]
jogador = input("Jogador Pedra, Papel ou Tesoura: ").lower()
pc = random.choice(jogadas)
print(pc)
if (jogador not in jogadas):
    print("Jogada invalida!")
elif(jogador == pc):
    print("Empate!")
elif((jogador == "papel" and pc == "pedra") 
    or (jogador == "pedra" and pc == "tesoura") 
    or (jogador == "tesoura" and pc == "papel")
):
     print(f"{jogador} ganhou de {pc}")
else:
    print(f"{pc} ganhou de {jogador}")
