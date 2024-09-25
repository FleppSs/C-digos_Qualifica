# Escreva um programa que faça o cmoputador pensar em um número inteiro entre 0 e 5
# e peça para o usuário descobrir o número escolhido pelo computador
import random
num = int(random.randint(0, 5))
choice = int(input("Digite o número e teste sua sorte! "))
if choice == num:
    print("Você acertou o número!!!")
if not choice == num:
    print(f"Não foi dessa vez. Tente de novo! O  número escolhido foi {num}")
