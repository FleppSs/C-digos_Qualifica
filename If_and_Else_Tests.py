user = input("Insira seu nome de usuario: ")
print("---------------------------------------------------------------")
if user == "Link":
    print("Usuário encontrado")
    print(user)
    # a seguir estou verificando se a senha do usuario está correta.
    key = input("Insira sua senha: ")
    if key == "Zelda":
        print("Senha correta.")
        print("Efetuando seu login, aguarde...")
        print("Usuario conectado: " + user)
        senha = input("Deseja mudar sua senha?(N/S) ").upper()
        if senha == "N":
            print("")
            print("---------------------------------------------------------------")
        elif senha == "S":
            key = input("Insira sua nova senha: ")
            print("SENHA ALTERADA!")
            print("---------------------------------------------------------------")
    else:
        print("Senha incorreta")
        print("---------------------------------------------------------------")

else:
    print("Usuário não encontrado.")
    print("---------------------------------------------------------------")
