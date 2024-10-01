import os
print("Bem vindo ao meu diretório de jogos!!")


while True:
    print("------------------JOGOS------------------")
    print("[1] Snake\n[2] Undertale\n[3] Pong\n[4]Rpg(não_finalizado)\n[5] Pong2\n[6] Space Invaders\n[7] Balls\n[0] Sair")
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
        os.system('Space_Invaders.py')
    elif choice == "7":
        os.system('Balls.py')
    elif choice == "0":
        break
    else:
        print("Comando inválido.")