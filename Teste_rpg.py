from PIL import Image

# Abrir uma imagem
imagem = Image.open('C:/Users/Noite.AL014/Downloads/bau.png')

# Exibir a imagem
imagem.show()

import pygame

# Inicializar o mixer
pygame.mixer.init()

# Carregar um arquivo de áudio
pygame.mixer.music.load('C:/Users/Noite.AL014/Downloads/baur.mp3')

# Tocar o áudio
pygame.mixer.music.play()

# Esperar a reprodução terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
