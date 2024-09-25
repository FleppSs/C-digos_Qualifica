idade_t = 0
M_velho_name = ""
M_velho = 0
F_nova = 0
for curriculo in range(4):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    genero = str(input("Digite o genero(M/F): ").upper())
    idade_t += idade
    if genero == "M" and idade > M_velho:
        M_velho = idade
        M_velho_name = nome
    if genero == "F" and idade < 20:
        F_nova += 1
media = idade_t / 4
print(f"O nome do homem mais velho é: {M_velho_name} com {M_velho} anos de idade.")
print(f"Ao todo temos {F_nova} mulher(es) com menos de 20 anos de idade.")
print(f"A média de idade é {media}")
