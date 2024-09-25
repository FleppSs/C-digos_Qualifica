import pygame
import cv2
import time

# Caminho do vídeo
video_path = 'C:/Users/Noite.AL014/Downloads/baurr.mp4'



# Abrir o arquivo de vídeo
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Exibir o frame
    cv2.imshow('Video', frame)

    # Parar o vídeo se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar o vídeo e fechar as janelas
cap.release()
cv2.destroyAllWindows()

