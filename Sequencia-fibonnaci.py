import time
a, b = 0, 1
while True:
    print(f"fibonacci: {b} | Soma acumulada: {a + b}")
    a, b = b, a + b
    time.sleep(2)
