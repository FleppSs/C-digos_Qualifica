# Crie um programa que calcule o tempo médio de atendimento aos clientes, considerando uma lista com todos esses tempos
# já atendidos [5, 10, 15, 20, 25, 30, 35]
tempo_atendimento = [5, 10, 15, 20, 25, 30, 35]
tempoto = 0
atendimentos = 0
for tempo in tempo_atendimento:
    tempoto += tempo
    atendimentos += 1
media = tempoto / atendimentos
print(media)