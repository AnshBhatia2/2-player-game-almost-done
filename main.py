import pygame
import os
pygame.font.init()
pygame.mixer.init

WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2-player game")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

border = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

#bullet_hit_sound = pygame.mixer.Sound('Assets/Grenade+1.mp3)
#bullet_fire_sound = pygame.mixer.Sound('Assets/Gun+Silencer.mp3)

health_font = pygame.font.SysFont('comicsans',40)
winner_font = pygame.font.SysFont('comicsans'100)

FPS = 60
vel = 5
bullet_vel = 7
max_bullets = 3
spaceship_width, spaceship_height = 55,40

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

yellow_spaceship_image = pygame.image.load(
    os.path.join('Assets','spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(
    yellow_spaceship_image, (spaceship_width, spaceship_height)), 90)

red_spaceship_image = pygame.image.load(
    os.path.join('Assets','spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(
    red_spaceship_image, (spaceship_width, spaceship_height)), 90)

space = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(space, (0,0))
    pygame.draw.rect(WIN, black, border)

    red_health_text = health_font.render(
        "Health: " + str(red_health),1,white)
    yellow_health_text = health_font.render(
        "Health: " + str(yellow_health),1,white)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width()-10,10))
    WIN.blit(yellow_health_text, (10,10))

    WIN.blit(yellow_spaceship, yellow.x, yellow.y)
    WIN.blit(red_spaceship, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, red, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, yellow, bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - vel > 0: # left
        yellow.x -= vel
    if keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < border.x: #right
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0: # up
        yellow.x -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < HEIGHT - 15: #down
        yellow.x += vel

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - vel > border.x + border.width: #left
        red.x -= vel
    if keys_pressed[pygame.K_d] and red.x + vel + red.width < WIDTH: #right
        red.x += vel
    if keys_pressed[pygame.K_w] and red.y - vel > 0: #up
        red.x -= vel
    if keys_pressed[pygame.K_s] and red.y + vel + red.height < HEIGHT - 15: #down
        red.x += vel

def handle_bullets(yellow_bullets, red_bullets, yellow, red)
    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x += bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            run = False
            pygame.quit()

