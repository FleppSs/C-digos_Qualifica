# crie um programa de adivinhção onde o computador vai pensar em um número entre 0 e 10 só que agora o jogador vai
# adivinhar até acertar mostrando no final o n de tentativas.
import random
num = int(random.randint(0, 10))
tentativas = 0
while True:
    print("Adivinhe o número gerado pelo computador.")
    escolha = int(input("Faça sua escolha: "))
    if escolha == num:
        print("Parabéns! Você acertou!")
        tentativas += 1
        break

    else:
        print("Tente novamente.")
        tentativas += 1
print(f"Quantidade de tentativas até acertar {tentativas}")
