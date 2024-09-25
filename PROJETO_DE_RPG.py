import random
from PIL import Image
import cv2
import time
# Status
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
        self.ataque = 25
        self.defesa = 15
        self.experiencia = 0
        self.nivel = 1
        self.inventario = []
        self.vida_maxima = 100

    def atacar(self, inimigo):
        dano = max(0, self.ataque - inimigo.defesa)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")

    def curar(self, quantidade):
        self.vida = min(self.vida_maxima, self.vida + quantidade)
        print(f"{self.nome} curou {quantidade} pontos de vida!")

# Itens
    def usar_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            if item == 'Poção de Vida':
                self.curar(40)
            elif item == 'Poção de Energia':
                self.ataque += 10
                print(f"{self.nome} usou Poção de Energia e agora tem {self.ataque} de ataque!")
        else:
            print("Item não encontrado no inventário.")

# Sistema de upagem
    def ganhar_experiencia(self, quantidade):
        self.experiencia += quantidade
        print(f"{self.nome} ganhou {quantidade} de experiência!")
        if self.experiencia >= 100 * self.nivel:
            self.experiencia -= 100 * self.nivel
            self.nivel += 1
            self.vida_maxima += 20
            self.ataque += 5
            self.defesa += 2
            self.vida = self.vida_maxima
            print(f"{self.nome} subiu para o nível {self.nivel}!")

    def mostrar_status(self):
        return f"{self.nome} - Vida: {self.vida}/{self.vida_maxima}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Experiência: {self.experiencia}"

# Base para criação de inimigos

class Inimigo:
    def __init__(self, nome, vida, ataque, defesa, experiencia):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.experiencia = experiencia

    def atacar(self, personagem):
        dano = max(0, self.ataque - personagem.defesa)
        personagem.vida -= dano
        print(f"{self.nome} atacou {personagem.nome} e causou {dano} de dano!")


class Item:
    def __init__(self, nome):
        self.nome = nome

# Base de missões
class Missao:
    def __init__(self, descricao, recompensa):
        self.descricao = descricao
        self.recompensa = recompensa
        self.completa = False

    def completar_missao(self, personagem):
        if not self.completa:
            self.completa = True
            personagem.inventario.append(self.recompensa)
            print(f"Missão completada! Você ganhou um {self.recompensa}.")

# Base do  sistema de batalhas
def batalha(personagem, inimigo):
    while personagem.vida > 0 and inimigo.vida > 0:
        print(f"\n{personagem.mostrar_status()}")
        print(f"{inimigo.nome} - Vida: {inimigo.vida}")
        acao = input("Escolha uma ação: [A] Atacar, [C] Curar, [I] Usar item: ").upper()

        if acao == 'A':
            personagem.atacar(inimigo)
            if inimigo.vida > 0:
                inimigo.atacar(personagem)
        elif acao == 'C':
            personagem.curar(20)
            inimigo.atacar(personagem)
        elif acao == 'I':
            print("Inventário: ", personagem.inventario)
            item = input("Qual item usar? ")
            personagem.usar_item(item)
            inimigo.atacar(personagem)
        else:
            print("Ação inválida!")

        if personagem.vida <= 0:
            print("Você foi derrotado!")
            return False
        elif inimigo.vida <= 0:
            print(f"Você derrotou {inimigo.nome}!")
            personagem.ganhar_experiencia(inimigo.experiencia)
            return True

# Posso adicionar novos mapas aqui em baixo
def explorar(personagem):
    locais = ["Caverna", "Floresta", "Ruínas", "Vilarejo", "Casa", "Igreja abandonada", "Cemitério"]
    print("Locais para explorar: ", locais)
    escolha = input("Para onde você deseja ir? ").capitalize()

# Após adicionar um local,aqui eu coloco o que vai acontecer
    if escolha in locais:
        print(f"Você explorou a {escolha}.")
        if escolha == "Caverna":
            print("""Você entra na caverna em busca de abrigo e um local seguro para descansar à noite...Porém 
            mal sabe você que essa caverna não é tão segura assim. A caverna é funda, então você decide dar um grito 
            para verificar se existe alguma criatura na caverna, e tudo que você ouve são seus própios ecos.
             Você monta seu saco de dormir e começa a preparar uma fogueira para cozinhar a carne de um coelho que você 
             caçou mais cedo. Após a refeição vocÊ vai começando a ficar mais relaxado à medida que a fogueira se 
             apaga. Você está prestes a pegar no sono quando por instinto você sente uma presença vindo em sua direção.
             então você rapidamente saca sua espada e corre em direção à saída. Parabéns! Você quase morreu na caverna 
             de um orc! E ele está furioso para te matar.""")
            inimigo = Inimigo("Orc", 80, 25, 10, 30)
            print(f"Um {inimigo.nome} apareceu!")
            batalha(personagem, inimigo)
        elif escolha == "Floresta":
            print("""Você decide entrar na floresta para caçar... É noite e você escuta um uivo distante. Minutos depois
            você ouve rosnados de cachorro bem atrás de você. Você decide olhar e vê um lobo correndo em sua direção""")
            inimigo = Inimigo("Lobo", 60, 20, 5, 20)
            print(f"Um {inimigo.nome} apareceu!")
            batalha(personagem, inimigo)
        elif escolha == "Ruínas":
            print("""Enquanto você entra nas ruínas você se depara com sons estranhos... Indo mais a fundo você decide
                  acender uma tocha e se surpreende com um esqueleto armado com uma espada vindo na sua direção!!!
                  e assim começa a luta!!!""")
            inimigo = Inimigo("Esqueleto", 70, 15, 15, 25)
            print(f"Um {inimigo.nome} apareceu!")
            batalha(personagem, inimigo)
        elif escolha == "Vilarejo":
            if "Poção de Vida" not in personagem.inventario:
                personagem.inventario.append('Poção de Vida')
                print("""Você encontrou com um sacerdote e ele te deu uma Poção de Vida no vilarejo para ajudar em suas"
                      batalhas.""")
            else:
                print("Você já tem a Poção de Vida.")
        elif escolha == "Casa":
            print("""Você volta para casa e tem uma boa noite de sono. Você precisava disso!(Porém, infelizmente dormir 
            não cura suas feridas)""")
        elif escolha == "Igreja abandonada":
            print("""Você por alum motivo decide entrar em uma igreja abandonada muito famosa por "Quem entrar nessa 
            igreja, nunca mais volta". Não sabemos porque você pensou que isso seria uma boa idéia, mas tudo bem. 
            Ao entrar na igreja sua espinha treme e todos os pelos de sua carne ficam arrepiados e você sente um pavor 
            imenso em seu coração. Você está com medo. Espectros surgem do chão e começam a agonizar por ajuda e 
            gritantes eles dizem coisas como "SOCORRO" "NOS LIBERTE" "ME AJUDE" e então uma luz surge no meio da igreja
             destruída e vazia, uma luz cinza e negra que começam a ter uma forma física de uma pessoa esquelética e 
             seca, seus olhos são negros e vermelhos. Ele carrega um cajada e usa uma capa branca rasgada junto de uma
              coroa de rei. Ele dá u  grito com tanto ódio, que faz sua cabeça doer. Esteja pronto para sofrer.""")
            inimigo = Inimigo("Padre amaldiçoado", 100, 30, 15, 80)
            print(f"Um {inimigo.nome} apareceu!")
            batalha(personagem, inimigo)
        elif escolha == "Cemitério":
            print("""Encontrou um ghoul!!!""")
            inimigo = Inimigo("Ghoul", 50, 40, 10, 150)
            print(f"Um {inimigo.nome} apareceu!")
            batalha(personagem, inimigo)
            print("Parabéns! Você encontrou um baú")
            video_path = 'C:/Users/Noite.AL014/Downloads/baurr.mp4'

            cap = cv2.VideoCapture(video_path)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()
    else:
        print("Local inválido!")

# Missões que eu posso adicionar e as recompensas após a conclusão
def mostrar_missoes():
    missao1 = Missao("Derrote um Orc", "Poção de Energia")
    missao2 = Missao("Encontre uma Poção de Vida", "Espada de Ferro")
    missao3 = Missao("Derrote um lobo", "Carne de Lobo")
    missao4 = Missao("Procure a espada lendária Excalibur", "Excalibur")
    missao5 = Missao("Entre na floresta negra e consiga um olho de aranha", "Veneno de aranha")
    missao6 = Missao("Encontre qualquer coisa", "Vou pensar ainda")
    return [missao1, missao2, missao3, missao4, missao5, missao6]

# Interface e comandos
def main():
    print("Bem-vindo ao RPG!!")
    nome = input("Escolha o nome do seu personagem: ")
    personagem = Personagem(nome)
    personagem.inventario.append('Poção de Vida')

    missoes = mostrar_missoes()

    while personagem.vida > 0:
        comando = input("\nEscolha uma ação: [E] Explorar, [B] Batalha, [S] Status, [M] Missões, [Q] Sair: ").upper()

        if comando == 'E':
            explorar(personagem)
        elif comando == 'B':
            inimigo = Inimigo("Goblin", 50, 15, 5, 15)
            print(f"Um {inimigo.nome} apareceu!")
            batalha(personagem, inimigo)
        elif comando == 'S':
            print(personagem.mostrar_status())
            print("Inventário:", personagem.inventario)
        elif comando == 'M':
            for i, missao in enumerate(missoes):
                status = "Completa" if missao.completa else "Pendente"
                print(f"Missão {i + 1}: {missao.descricao} - Status: {status}")
                if not missao.completa:
                    completar = input(f"Você deseja completar a missão '{missao.descricao}'? [S/N] ").upper()
                    if completar == 'S':
                        missao.completar_missao(personagem)
        elif comando == 'Q':
            print("Saindo do jogo...")
            break
        else:
            print("Comando inválido!")


if __name__ == "__main__":
    main()
