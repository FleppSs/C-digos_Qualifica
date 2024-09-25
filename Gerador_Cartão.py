import random
import faker
from datetime import datetime, timedelta

# Criação de um gerador de dados fictícios
fake = faker.Faker()

def gerar_numero_cartao():
    return f"{random.randint(4, 6)}{random.randint(1000000000000000, 9999999999999999)}"

def gerar_data_expiracao():
    hoje = datetime.now()
    expirar = hoje + timedelta(days=random.randint(30, 365*5))  # Entre 1 mês e 5 anos a partir de hoje
    return expirar.strftime("%m/%y")

def gerar_cvv():
    return f"{random.randint(100, 999)}"

def gerar_nome():
    return fake.name()

def gerar_cartao():
    return {
        "Número do Cartão": gerar_numero_cartao(),
        "Data de Expiração": gerar_data_expiracao(),
        "CVV": gerar_cvv(),
        "Nome": gerar_nome()
    }

if __name__ == "__main__":
    cartao = gerar_cartao()
    print(f"Número do Cartão: {cartao['Número do Cartão']}")
    print(f"Data de Expiração: {cartao['Data de Expiração']}")
    print(f"CVV: {cartao['CVV']}")
    print(f"Nome: {cartao['Nome']}")
