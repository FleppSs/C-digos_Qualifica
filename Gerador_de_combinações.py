# crie um programa que gere combinações entre 5 elementos a partir de uma lista
import itertools
elementos = [1, 2, 3, 4, 5]
combinacoes = list(itertools.combinations(elementos, 2))
print("As combinações são {}".format(combinacoes))
