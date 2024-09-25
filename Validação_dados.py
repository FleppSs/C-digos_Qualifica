# Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
# caso esteja eterrado, peça a digitação novamente.
#  até ter um valor correto.
while True:
    sex = str(input("Digite o seu gênero(M/F): ").upper())
    if sex != str:
        print("Digite novamente.")
    if sex == "M":
        print("Você é do gênero masculino")
        escolha = str(input("Deseja sair?(S/N):").upper())
        if escolha == "S":
            break
    elif sex == "F":
        print("Você é do genêro feminino.")
        escolha = str(input("Deseja sair?(S/N):").upper())
        if escolha == "S":
            break
print("Programa finalizado.")