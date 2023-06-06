import pygame

pygame.init()
pygame.mixer.music.load(
  '08ver.mp3')  #mp3 o aquivo mp3 tem que esta junto com o aquivo do .py
pygame.mixer.music.play()
input()
pygame.event.wait()
