while True:
    choice1 = input("Deseja calcular o preço dos produtos?(s/n)").upper()
    if choice1 == "N":
        print("Tenta de novo então engraçadinho.")
    elif choice1 == "S":
        print("Okay.. então vamos prosseguir.")
        break
    else:
        print("Qual é o seu problema animal?")
# Estoque

farinhakg = 1000
acucarkg = 1000
eggsqt = 12
leitel = 1000
manteigag = 200
fermentog = 100
baunilhaml = 50

# Uso para o bolo

farinha_uso = 500
acucar_uso = 300
ovos_uso = 4
leite_uso = 200
fermento_uso = 10
baunilha_uso = 10
manteiga_uso = 100


# Tabela de preços

farinha = 6.00
acucar = 4.00
eggs = 8.00
leite = 5.00
manteiga = 10.00
fermento = 8.00
baunilha = 10.00
gas = 7.00
eletricidade = 5.00

# Uso por bolo

farinha_custo_uso = (farinha_uso / 1000) * farinha
acucar_custo_uso = (acucar_uso / 1000) * acucar
eggs_custo_uso = (ovos_uso / 12) * eggs
leite_custo_uso = (leite_uso / 1000) * leite
manteiga_custo_uso = (manteiga_uso / 200) * manteiga
fermento_custo_uso = (fermento_uso / 100) * fermento
baunilha_custo_uso = (baunilha_uso / 50) * baunilha

custo_uso_total = (farinha_custo_uso + acucar_custo_uso + eggs_custo_uso + leite_custo_uso + manteiga_custo_uso
                   + fermento_custo_uso + baunilha_custo_uso + eletricidade + gas)
# Fatia preço
fatia_preco = (custo_uso_total / 12) * 1.50
custo_total = farinha + acucar + eggs + leite + manteiga + fermento + baunilha + gas + eletricidade
print("------------------ESTOQUE------------------")
print(f"""Farinha: {farinhakg}g\nAçúcar: {acucarkg}g\nOvos: {eggsqt}\nLeite: {leitel}ml\nManteiga: {manteigag}g
Baunilha: {baunilhaml}m\nFermento: {fermentog}g""")

while True:
    choice2 = input("Deseja fazer um bolo ou atualizar o estoque?(Atualizar/Fazer/sair)").upper()
    if choice2 == "ATUALIZAR":
        farinhakg += 1000
        acucarkg += 1000
        eggsqt += 12
        leitel += 1000
        manteigag += 200
        fermentog += 100
        baunilhaml += 50
        print("ESTOQUE ATUALIZADO!")
        print(f"PREÇO DA ATUALIZAÇÃO: {custo_total}")
        print("------------------ESTOQUE------------------")
        print(f"""Farinha: {farinhakg}g\nAçúcar: {acucarkg}g\nOvos: {eggsqt}\nLeite: {leitel}ml\nManteiga: {manteigag}g
        Baunilha: {baunilhaml}m\nFermento: {fermentog}g""")
        print("-------------------------------------------")
    elif choice2 == "SAIR":
        print("Programa finalizado.")
        break

    elif choice2 == "FAZER":
        if (farinhakg >= farinha_uso and acucarkg >= acucar_uso and eggsqt >= ovos_uso and leitel >= leite_uso
                and manteigag >= manteiga_uso and fermentog >= fermento_uso and baunilhaml >= baunilha_uso):

            farinhakg -= farinha_uso
            acucarkg -= acucar_uso
            eggsqt -= ovos_uso
            leitel -= leite_uso
            manteigag -= manteiga_uso
            fermentog -= fermento_uso
            baunilhaml -= baunilha_uso

        print("BOLO FEITO!!! ESTOQUE ATUALIZADO!")
        print("------------------ESTOQUE------------------")
        print(f"""Farinha: {farinhakg}g\nAçúcar: {acucarkg}g\nOvos: {eggsqt}\nLeite: {leitel}ml\nManteiga: {manteigag}g
        Baunilha: {baunilhaml}m\nFermento: {fermentog}g""")
        print(f"PREÇO POR FATIA: R${fatia_preco:.2f}")
        print("-------------------------------------------")
        if not (farinhakg >= farinha_uso and acucarkg >= acucar_uso and eggsqt >= ovos_uso and leitel >= leite_uso
                and manteigag >= manteiga_uso and fermentog >= fermento_uso and baunilhaml >= baunilha_uso):
            print("Você não tem material suficiente para fazer o bolo. Por favor verifique o estoque e tente "
                  "novamente""")
