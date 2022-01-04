import pygame
import random
from colors import *

snake_speed = 20
 
window_x = 800
window_y = 600


pygame.init()

file = 'sonic.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

pygame.display.set_caption('Snake Python')


game_window = pygame.display.set_mode((window_x, window_y))
image = pygame.image.load("logo.png")
pygame.display.set_icon(image)
start_time = pygame.time.get_ticks()
 
fps = pygame.time.Clock()
 
snake_position = [50, 50]
 
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
direction = 'RIGHT'
change_to = direction
 
score = 0