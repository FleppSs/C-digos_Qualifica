import random
def adivinhe_num(intervalo_min, intervalo_max):
    numero_sc = random.randint(intervalo_min, intervalo_max)
    tentativas = 0
    while True:
        palpite = int(input(f"Adivinhe o número entre {intervalo_min} e {intervalo_max}: "))
        tentativas += 1
        if palpite < numero_sc:
            print("O número secreto é maior.")
        elif palpite > numero_sc:
            print("O número secreto é menor.")
        elif palpite == numero_sc:
            print("PARABÉNS VOCÊ GANHOU!!!!")
            print(f"Tentativas {tentativas}")
            break


adivinhe_num(0, 10)
