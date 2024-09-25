import random

print("---------------JANKENPO---------------")
print("Escolhas: ")
print("(1) Pedra")
print("(2) Papel")
print("(3) Tesoura")
choice = int(input("Faça sua escolha:"))
robo = int(random.randint(1, 3))
if choice == robo == 1:
    print("Pedra! Empate!!")
if choice == robo == 2:
    print("Papel!! empate")
if choice == robo == 3:
    print("Tesoura!! Empate")
if choice == 3 and robo == 1:
    print("Pedra!! Você perdeu")
if choice == 1 and robo == 2:
    print("Papel!! Você perdeu!")
if choice == 2 and robo == 3:
    print("Tesoura! Você perdeu!")
if choice == 1 and robo == 3:
    print("Tesoura! Você ganhou!")
if choice == 2 and robo == 1:
    print("Pedra!! Você ganhou!")
if choice == 3 and robo == 2:
    print("Papel!! Você ganhou!!")