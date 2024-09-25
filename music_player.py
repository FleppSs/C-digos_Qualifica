import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Caminho da pasta raiz específica
PASTA_RAIZ = 'C:/Users/Noite.AL014/Donwloads'  # Substitua este caminho pelo caminho da sua pasta

# Funções para controle de música
def abrir_pasta():
    global arquivo_musica
    arquivos = filedialog.askopenfilenames(initialdir=PASTA_RAIZ, filetypes=[("Arquivos de Música", "*.mp3 *.wav")])
    if arquivos:
        arquivo_musica = arquivos[0]  # Pegando o primeiro arquivo selecionado
        pygame.mixer.music.load(arquivo_musica)
        status_var.set(f"Música carregada: {arquivo_musica.split('/')[-1]}")

def tocar_musica():
    if arquivo_musica:
        pygame.mixer.music.play()
        status_var.set("Reproduzindo...")

def pausar_musica():
    pygame.mixer.music.pause()
    status_var.set("Pausado.")

def retomar_musica():
    pygame.mixer.music.unpause()
    status_var.set("Reproduzindo...")

def parar_musica():
    pygame.mixer.music.stop()
    status_var.set("Parado.")

# Inicializar pygame
pygame.init()
pygame.mixer.init()

# Configurar a interface gráfica
root = tk.Tk()
root.title("Reprodutor de Música")

# Variável para armazenar o status da música
status_var = tk.StringVar()
status_var.set("Nenhuma música carregada.")

# Botões
btn_abrir = tk.Button(root, text="Abrir Música", command=abrir_pasta)
btn_abrir.pack(pady=10)

btn_tocar = tk.Button(root, text="Tocar", command=tocar_musica)
btn_tocar.pack(pady=10)

btn_pausar = tk.Button(root, text="Pausar", command=pausar_musica)
btn_pausar.pack(pady=10)

btn_retomar = tk.Button(root, text="Retomar", command=retomar_musica)
btn_retomar.pack(pady=10)

btn_parar = tk.Button(root, text="Parar", command=parar_musica)
btn_parar.pack(pady=10)

# Status da música
status_label = tk.Label(root, textvariable=status_var)
status_label.pack(pady=20)

# Inicializar a aplicação
root.mainloop()

# Encerrar o pygame
pygame.quit()
