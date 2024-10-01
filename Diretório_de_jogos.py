import os
print("Bem vindo ao meu diretório de jogos!!")


while True:
    print("------------------OPÇÕES------------------")
    print("[1] Snake [2] Undertale [3] Pong [4]Rpg(não_finalizado) [5] Pong2 [6] Balls [7] Sair")
    choice = str(input(" "))
    if choice == "1":
        os.system('Snake.py')
    elif choice == "2":
        os.system('Undertale_in_python.py')
    elif choice == "3":
        os.system('Pong.py')
    elif choice == "4":
        os.system('PROJETO_DE_RPG.py')
    elif choice == "5":
        os.system('Pong2.py')
    elif choice == "6":
        os.system('Balls.py')
    elif choice == "7":
        break
    else:
        print("Comando inválido.")