# Crie um programa que verifica a nova senha que o usuário vai criar.
# peça para ele mudar a senha e enquanto ele não colocar um caractere especial e um número o programa não aceita
# a nova senha.
senha_valida = 0
while senha_valida == 0:
    nova_senha = input("Crie a nova senha:")
    tem_especial = 0
    tem_num = 0
    for caractere in nova_senha:
        if caractere in "!@#$%¨&*()_+{}^<>:?|-=´[~],.;/":
            tem_especial = 1
        elif caractere in "0987654321":
            tem_num = 1

    if tem_especial == 1 and tem_num == 1:
        print("Senha aceita!")
        senha_valida = 1
    else:
        print("Tente novamente.")