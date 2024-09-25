# crie um programa que divida a turma em dois grupos
import random
lista = ["Renan", "Ytalo", "Nataly", "Renato", "Luydi", "Murilo", "Uriel", "Alexandre", "Gilmar", "Thiago",
         "Gelson", "Gabriela", "Breno", "Yago", "Paulo", "Thallys"]
random.shuffle(lista)
sla = len(lista) // 2
parte1 = lista[sla:]
parte2 = lista[:sla]
print(f"Grupo 1: {parte1}")
print(f"Grupo 2: {parte2}")