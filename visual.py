import pygame
import random
import time

from setting import Board
from square import Direction
from player import Player
from show import show

GAME_SIZE = 600
PANEL_WIDTH = 300
STICK_WIDTH = 20
SQUARE_SIZE = (GAME_SIZE - 5 * STICK_WIDTH) / 4

print("[INFO]")
print(f"\tGAME_SIZE   = {GAME_SIZE}")
print(f"\tPANEL_WIDTH = {PANEL_WIDTH}")
print(f"\tSTICK_WIDTH = {STICK_WIDTH}")
print(f"\tSQUARE_SIZE = {SQUARE_SIZE}")
print("[INFO]")

game_background_color = (245, 224, 122)
panel_background_color = (227, 227, 227)

square_color = (209, 193, 113)

player_color = (0, 0, 0)

first_player_color = (252, 3, 3)
second_player_color = (3, 3, 252)

human_player_color = (186, 186, 186)

human_x, human_y, human_direction = 2, 2, 0

def set_text(string, coordx, coordy, fontSize):
    font = pygame.font.Font('FreeSans/freesansbold.ttf', fontSize)
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)

def mark_square(surface, x, y, color):
    x1 = PANEL_WIDTH + STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (x - 1)
    y1 = STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (y - 1)
    pygame.draw.rect(surface, color, pygame.Rect(
        x1, y1, SQUARE_SIZE, SQUARE_SIZE
    ))

def show_tool_panel(surface, b):
    pygame.draw.rect(surface, panel_background_color, pygame.Rect(0, 0, PANEL_WIDTH, GAME_SIZE))

    totalText1 = set_text(f"1st Player: {b.FIRST_PLAYER}", 50, 20, 15)
    totalText2 = set_text(f"2st Player: {b.SECOND_PLAYER}", 50, 40, 15)
    totalText3 = set_text(f"Position: {human_x}, {human_y}, {human_direction}", 60, 60, 15)
    totalText4 = set_text(f"TURN: {b.TURN % 2}", 50, 80, 15)

    surface.blit(totalText1[0], totalText1[1])
    surface.blit(totalText2[0], totalText2[1])
    surface.blit(totalText3[0], totalText3[1])
    surface.blit(totalText4[0], totalText4[1])

def random_color():
    return (random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))

def draw_human_at_position(surface, x, y, direction):
    x1, y1 = 0, 0
    if direction == Direction.UP:
        x1 = PANEL_WIDTH + STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (x - 1)
        y1 = (STICK_WIDTH + SQUARE_SIZE) * y - SQUARE_SIZE - STICK_WIDTH
    elif direction == Direction.BOTTOM:
        x1 = PANEL_WIDTH + STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (x - 1)
        y1 = (STICK_WIDTH + SQUARE_SIZE) * y
    elif direction == Direction.LEFT:
        x1 = PANEL_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (x - 1)
        y1 = STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * y - SQUARE_SIZE - STICK_WIDTH
    elif direction == Direction.RIGHT:
        x1 = PANEL_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * x
        y1 = STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * y - SQUARE_SIZE - STICK_WIDTH

    if direction == Direction.UP or direction == Direction.BOTTOM:
        pygame.draw.rect(surface, human_player_color, pygame.Rect(
            x1, y1, SQUARE_SIZE, STICK_WIDTH
        ))
    else:
        pygame.draw.rect(surface, human_player_color, pygame.Rect(
            x1, y1, STICK_WIDTH, SQUARE_SIZE
        ))

def draw_at_position(surface, x, y, direction):
    x1, y1 = 0, 0
    if direction == Direction.UP:
        x1 = PANEL_WIDTH + STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (x - 1)
        y1 = (STICK_WIDTH + SQUARE_SIZE) * y - SQUARE_SIZE - STICK_WIDTH
    elif direction == Direction.BOTTOM:
        x1 = PANEL_WIDTH + STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (x - 1)
        y1 = (STICK_WIDTH + SQUARE_SIZE) * y
    elif direction == Direction.LEFT:
        x1 = PANEL_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (x - 1)
        y1 = STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * y - SQUARE_SIZE - STICK_WIDTH
    elif direction == Direction.RIGHT:
        x1 = PANEL_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * x
        y1 = STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * y - SQUARE_SIZE - STICK_WIDTH

    if direction == Direction.UP or direction == Direction.BOTTOM:
        pygame.draw.rect(surface, player_color, pygame.Rect(
            x1, y1, SQUARE_SIZE, STICK_WIDTH
        ))
    else:
        pygame.draw.rect(surface, player_color, pygame.Rect(
            x1, y1, STICK_WIDTH, SQUARE_SIZE
        ))

def show_board(srceen, b):
    for i in range(4):
        for j in range(4):
            if b.board[i][j].LEFT == True:
                # print(f"{i}, {j}, LEFT")
                draw_at_position(screen, j + 1, i + 1, Direction.LEFT)
            if b.board[i][j].RIGHT == True:
                # print(f"{i}, {j}, RIGHT")
                draw_at_position(screen, j + 1, i + 1, Direction.RIGHT)
            if b.board[i][j].UP == True:
                # print(f"{i}, {j}, UP")
                draw_at_position(screen, j + 1, i + 1, Direction.UP)
            if b.board[i][j].BOTTOM == True:
                # print(f"{i}, {j}, BOTTOM")
                draw_at_position(screen, j + 1, i + 1, Direction.BOTTOM)

            if b.marked_board[i][j] == 0:
                mark_square(screen, j + 1, i + 1, first_player_color)
            elif b.marked_board[i][j] == 1:
                mark_square(screen, j + 1, i + 1, second_player_color)

def show_board_squares(surface):
    for i in range(1, 5):
        for j in range(1, 5):
            x1 = PANEL_WIDTH + STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (i - 1)
            y1 = STICK_WIDTH + (STICK_WIDTH + SQUARE_SIZE) * (j - 1)
            pygame.draw.rect(surface, square_color, pygame.Rect(
                x1, y1, SQUARE_SIZE, SQUARE_SIZE
            ))
            # print(f"{x1} {y1} {x2} {y2}")

## GAME PLAYER

b = Board(n=4)
DEPTH = 2
player = Player()

def computer_move():
    x, y, dir = player.calc(b, depth=DEPTH)
    res = b.put(x, y, dir)
    print(f"{{ X = {x}, Y = {y}, DIR = {dir} }}")

    if res == True:
        print("ONE MORE PLEASE!")
        b.TURN -= 1
        computer_move()

## GAME PLAYER

pygame.init()

screen = pygame.display.set_mode((GAME_SIZE + PANEL_WIDTH, GAME_SIZE))
pygame.display.set_caption('Boxe Game')
screen.fill(game_background_color)
pygame.display.flip()
running = True

cnt = 0

while running:
    cnt += 1

    screen.fill(game_background_color)

    show_tool_panel(screen, b)
    show_board_squares(screen)

    if b.TURN % 2 == 0:
        computer_move()

    show_board(screen, b)

    draw_human_at_position(screen, human_x, human_y, human_direction)

    pygame.display.flip()

    if cnt % 1000 == 0:
        show(b)
        for i in range(4):
            for j in range(4):
                if b.board[j][i].LEFT == True:
                    print(f"{i}, {j}, LEFT")
                if b.board[j][i].RIGHT == True:
                    print(f"{i}, {j}, RIGHT")
                if b.board[j][i].UP == True:
                    print(f"{i}, {j}, UP")
                if b.board[j][i].BOTTOM == True:
                    print(f"{i}, {j}, BOTTOM")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                human_y -= 1
                if human_y < 0:
                    human_y = 0
            if event.key == pygame.K_s:
                human_y += 1
                if human_y > 4:
                    human_y = 4
            if event.key == pygame.K_a:
                human_x -= 1
                if human_x < 0:
                    human_x = 0
            if event.key == pygame.K_d:
                human_x += 1
                if human_x > 4:
                    human_x = 4
            if event.key == pygame.K_r:
                human_direction = (human_direction + 1) % 4
            if event.key == pygame.K_p:
                res = b.put(human_y - 1, human_x - 1, human_direction)
                if res == True:
                    b.TURN -= 1

