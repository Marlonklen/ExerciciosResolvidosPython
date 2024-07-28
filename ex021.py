# Faça um programa em Python que reproduza audio de um arquivo mp3.
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
para = input('aperta enter bixinha: ')
