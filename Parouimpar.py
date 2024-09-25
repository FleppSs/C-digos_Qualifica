par = 0
impar = 0
numero = 1
while numero != 0:
    numero = int(input("(press 0 to close)\nInsert a number: "))
    if numero != 0:
        if numero % 2 == 0:
            print("Seu número é par.")
            par += 1

        else:
            print("Seu número é impar.")
            impar += 1
print(f"Quantidades de pares {par}\nQuantidade de impares {impar}")
