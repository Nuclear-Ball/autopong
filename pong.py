import pygame
from settings import *

pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)
lose = font.render('Игрок 2 ВЫИГРАЛ!', True, WHITE)
win = font.render('Игрок 1 ВЫИГРАЛ!', True, WHITE)
screen = pygame.display.set_mode((320, 224))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load('layers/pong.png'))
x = int(0)
y = int(0)
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
    global enemy_paddle_y, enemy_paddle_up, enemy_paddle_down, paddle_down, paddle_up
    if x < W // 2:
        if y > enemy_paddle_y + paddle_width // 2:
            enemy_paddle_down = 1
            enemy_paddle_up = 0
        elif y < enemy_paddle_y + paddle_width // 2:
            enemy_paddle_down = 0
            enemy_paddle_up = 1
    if x > W // 2:
        if y > paddle_y + paddle_width // 2:
            paddle_down = 1
            paddle_up = 0
        elif y < paddle_y + paddle_width // 2:
            paddle_down = 0
            paddle_up = 1


def main():
    global x, y, up, down, left, right, paddle_down, paddle_up, paddle_y, enemy_paddle_y, enemy_paddle_up, enemy_paddle_down, lose_state, win_state, score_p1, score_p2
    score1 = font.render(f'Счет (Игрок 1): {score_p1}', True, WHITE)
    score2 = font.render(f'Счет (Игрок 2): {score_p2 - 5}', True, WHITE)
    key = pygame.key.get_pressed()
    y += down * speed - up * speed
    x += right * speed - left * speed
    paddle_ai()
    if enemy_paddle_y < 0:
        enemy_paddle_y = 0
    if (enemy_paddle_y + paddle_width) > H:
        enemy_paddle_y = H - paddle_width
    if paddle_y < 0:
        paddle_y = 0
    if (paddle_y + paddle_width) > H:
        paddle_y = H - paddle_width
    if x >= W - paddle_height and paddle_y < y < paddle_y + paddle_width:
        right = 0
        left = 1
        score_p1 += 1
    if x <= paddle_height and enemy_paddle_y < y < enemy_paddle_y + paddle_width:
        right = 1
        left = 0
        score_p2 += 1
    pygame.draw.circle(screen, WHITE, (x, y), 5)
    paddle_y += paddle_down * speed - paddle_up * speed
    enemy_paddle_y += enemy_paddle_down * (speed - 0) - enemy_paddle_up * (speed - 0)
    pygame.draw.rect(screen, WHITE, (310, paddle_y, paddle_height, paddle_width))
    pygame.draw.rect(screen, WHITE, (0, enemy_paddle_y, paddle_height, paddle_width))
    paddle_up = 0
    paddle_down = 0
    enemy_paddle_up = 0
    enemy_paddle_down = 0
    if y >= H - paddle_height:
        up = 1
        down = 0
    if y <= 0:
        up = 0
        down = 1
    if x <= -10:
        win_state = True
    if x >= W:
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

    pygame.time.delay(10)

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
