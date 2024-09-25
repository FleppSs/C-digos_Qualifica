import random
def d20():
    while True:

        print("[1] Jogar dado [2] Sair")
        escolha = int(input(" "))
        if escolha == 1:
            uservalor = random.randint(0, 20)
            valor = random.randint(0, 20)
            print(f"Você jogou o dado e caiu {uservalor}")
            print(f"Adversário: {valor}")
            if uservalor > valor:
                print("Você ganhou!")
            elif uservalor == valor:
                print("Empate!")
            else:
                print("Você perdeu!")
        elif escolha == 2:
            break
        else:
            print("Opção inválida.")


d20()
