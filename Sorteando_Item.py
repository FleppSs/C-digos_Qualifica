# O professor quer sortear um aluno para receber um aperto de mão.
# Crie um programa que ajude o professor
# lendo o nome dos alunos e escrevendo o nome escolhido
import random
al = str(input("Digite o nome de um aluno: "))
al2 = str(input("Digite o nome de um aluno: "))
al3 = str(input("Digite o nome de um aluno: "))
lista = [al, al2, al3] # Isso é uma lista que junta várias variaveis
ale = random.choice(lista) # Choice sorteia entre vaiaveis
print("O aluno escolhido é {}".format(ale))
