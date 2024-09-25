# Crie um programa que leia a idade das pessoas em uma fila de recepção. O programa não sabe quantas pessoas estão na
# fila, entõa ele continuará solicitando a idade de cada pessoa. enquanto houver mais pessoas a serem atendidas, quando
# o usuário informar que não há mais pessoas na fila, o programa será finalizado.
pessoas = 0
while True:
    idade = int(input("Digite a idade da pessoa: "))
    pessoas += 1
    print("Idade registrada.")
    sair = str(input("Deseja continuar?(S/N): ").upper())
    if sair == "N":
        break

print(f"No total {pessoas} pessoas foram registradas.")
print("Programa finalizado")

