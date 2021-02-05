import pygame
from settings import *

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)
lose = font.render('Игрок 2 ВЫИГРАЛ!', True, WHITE)
win = font.render('Игрок 1 ВЫИГРАЛ!', True, WHITE)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load('layers/pong.png'))
x = int(farness + paddle_height * 2 + ball_size)
y = int(0)
screen_size_x, screen_size_y = pygame.display.get_window_size()
print(screen_size_y)
paddle_y = int(0)
enemy_paddle_y = int(0)
down = bool(1)
up = bool(0)
left = bool(0)
right = bool(1)
paddle_down = bool(0)
paddle_up = bool(0)
enemy_paddle_down = bool(0)
enemy_paddle_up = bool(0)
win_state = bool(False)
lose_state = bool(False)
score_p1 = 0
score_p2 = 0


def paddle_ai():
    global enemy_paddle_up, enemy_paddle_down, paddle_up, paddle_down
    if x < screen_size_x // 2:
        if y > enemy_paddle_y + paddle_width // 2:
            enemy_paddle_down = 1
            enemy_paddle_up = 0
        elif y < enemy_paddle_y + paddle_width // 2:
            enemy_paddle_down = 0
            enemy_paddle_up = 1
    if x > screen_size_x // 2:
        if y > paddle_y + paddle_width // 2:
            paddle_down = 1
            paddle_up = 0
        elif y < paddle_y + paddle_width // 2:
            paddle_down = 0
            paddle_up = 1


def main():
    global x, y, up, down, left, right, paddle_y, paddle_up, paddle_down, enemy_paddle_y, enemy_paddle_up, enemy_paddle_down, lose_state, win_state, score_p1, score_p2
    score1 = font.render(f'Счет (Игрок 1): {score_p1}', True, WHITE)
    score2 = font.render(f'Счет (Игрок 2): {score_p2}', True, WHITE)
    key = pygame.key.get_pressed()
    paddle_ai()
    '''Paddle collision'''
    if enemy_paddle_y < 0:
        enemy_paddle_y = 0
    if (enemy_paddle_y + paddle_width) > screen_size_y:
        enemy_paddle_y = screen_size_y - paddle_width
    if paddle_y < 0:
        paddle_y = 0
    if (paddle_y + paddle_width) > screen_size_y:
        paddle_y = screen_size_y - paddle_width
    '''Detect collision'''
    if screen_size_x - farness - paddle_height <= x + ball_size <= screen_size_x - farness and paddle_y < y + ball_size // 2 < paddle_y + paddle_width:
        right = 0
        left = 1
        score_p1 += 1
    if farness + paddle_height >= x - ball_size >= farness and enemy_paddle_y < y + ball_size // 2 < enemy_paddle_y + paddle_width:
        right = 1
        left = 0
        score_p2 += 1
    '''Move objects'''
    y += down * speed - up * speed
    x += right * speed - left * speed
    paddle_y += paddle_down * speed - paddle_up * speed
    enemy_paddle_y += enemy_paddle_down * (speed - 0) - enemy_paddle_up * (speed - 0)
    '''Drawing'''
    pygame.draw.circle(screen, WHITE, (x, y), ball_size)
    pygame.draw.rect(screen, WHITE, ((screen_size_x - farness) - paddle_height, paddle_y, paddle_height, paddle_width))
    pygame.draw.rect(screen, WHITE, (farness, enemy_paddle_y, paddle_height, paddle_width))
    '''Stop moving'''
    paddle_up = 0
    paddle_down = 0
    enemy_paddle_up = 0
    enemy_paddle_down = 0
    if y >= screen_size_y - ball_size:
        up = 1
        down = 0
    if y <= 0 + ball_size:
        up = 0
        down = 1
    if x <= -10:
        win_state = True
    if x >= screen_size_x:
        lose_state = True

    if key[pygame.K_w]:
        paddle_up = 1
        paddle_down = 0
    if key[pygame.K_s]:
        paddle_up = 0
        paddle_down = 1

    if key[pygame.K_UP]:
        enemy_paddle_up = 1
        enemy_paddle_down = 0
    if key[pygame.K_DOWN]:
        enemy_paddle_up = 0
        enemy_paddle_down = 1
    pygame.time.delay(0)

    if win_state:
        screen.blit(win, (20, 0))
        pygame.display.update()
        pygame.time.delay(5000)
        exit()
    if lose_state:
        screen.blit(lose, (20, 0))
        pygame.display.update()
        pygame.time.delay(5000)
        exit()
    screen.blit(score1, (20, 0))
    screen.blit(score2, (20, 30))
    pygame.display.update()


if __name__ == "__main__":
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
        main()
        screen.fill(BLACK)
