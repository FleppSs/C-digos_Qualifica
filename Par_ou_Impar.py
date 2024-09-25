import random
list = ["Par", "Impar"]
choice = str(input("Impar ou par? ").capitalize())
result = random.choice(list)
if choice == result:
    print(f"Você ganhou!!! O número foi {result}")
if not choice == result:
    print(f"Você perdeu, o número foi {result}")
