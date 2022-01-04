import pygame
import time
import random
from colors import *
from gamedisplay import *

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def pause():
    pause_font = pygame.font.SysFont("calibri", 40)
    loop = 1
    pause_surface = pause_font.render("PAUSE", 250, 100, white)
    pause_rect = pause_surface.get_rect()
    pause_rect.midtop = (window_x/2, window_y/3)
    game_window.blit(pause_surface, pause_rect)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                    pygame.mixer.music.pause()
                if event.key == pygame.K_SPACE:
                    game_window.fill((0,0,0))
                    loop = 0
        pygame.display.update()

def Timer():
    time_font = pygame.font.SysFont("calibri", 40)
    counting_time = pygame.time.get_ticks() - start_time
    counting_seconds = str(int(counting_time%60000)/1000 )
    counting_string = "Time : %s" % (counting_seconds)

    counting_text = time_font.render(str(counting_string), 1, (255,255,255))
    counting_rect = counting_text.get_rect()
    counting_rect.topleft = (window_x/3, window_y/100)
    game_window.blit(counting_text, counting_rect)

def game_over():
    my_font = pygame.font.SysFont('calibri', 50)
    game_over_surface = my_font.render(
        'PERDU ! Votre score est : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/3)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    baseTime = time.perf_counter()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_SPACE:
                    pygame.mixer.music.pause()
                    pause() 
                    pygame.mixer.music.unpause()              
 
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 5
        fruit_spawn = False
    else:
        snake_body.pop()
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, orange,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    show_score(white, 'calibri', 40)
    Timer()
    pygame.display.update()
    fps.tick(snake_speed)