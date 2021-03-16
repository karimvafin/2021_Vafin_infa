import pygame
import math
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_figure():
    """
    Returns characteristics of a random figure
    :return:
    """
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(30, 100)
    color = COLORS[randint(0, 5)]
    coord = [x, y, r, color]
    return coord


def draw_triangle(ch):
    """
    Draws a triangle with center in (x, y), with the side = s and with set color
    :param ch: includes x, y, s, color
    :return:
    """
    polygon(screen, ch[3], ((ch[0], ch[1] - ch[2] * math.sqrt(3) / 3),
                            (ch[0] - ch[2] / 2, ch[1] + math.sqrt(3) * ch[2] / 6),
                            (ch[0] + ch[2] / 2, ch[1] + math.sqrt(3) * ch[2] / 6)))


def draw_ball(characteristics):
    """
    Draws a ball in (x, y) with the radius = r and with set color
    :param characteristics: includes x, y, r, color
    :return:
    """
    circle(screen, characteristics[3], (characteristics[0], characteristics[1]), characteristics[2])


def is_got(coordinates, mouse_pos):
    if math.sqrt((mouse_pos[0] - coordinates[0]) ** 2 + (mouse_pos[1] - coordinates[1]) ** 2) < coordinates[2]:
        return True
    else:
        return False


def is_accelerate(coordinates, mouse_pos):
    if math.sqrt((mouse_pos[0] - coordinates[0]) ** 2 + (mouse_pos[1] - coordinates[1]) ** 2) < coordinates[2] * 1.3:
        return True
    else:
        return False


def print_text(text, color, position, size):
    f1 = pygame.font.Font(None, size)
    text1 = f1.render(text, True,
                      color, BLACK)

    screen.blit(text1, position)


def game(score, name):
    finished = False
    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(3):
                    if is_got(figures[i], event.pos):
                        score += 1
                        bool1[i] = True
                    if is_got(figures[i + 3], event.pos):
                        score += 2
                        bool1[i + 3] = True
            if event.type == pygame.MOUSEMOTION:
                for i in range(6):
                    if is_accelerate(figures[i], event.pos):
                        bool2[i] = True
                    else:
                        bool2[i] = False

        # move figures
        for i in range(6):
            figures[i][0] += round(v[i] * math.cos(angles[i]) / 30)
            figures[i][1] += round(v[i] * math.sin(angles[i]) / 30)

        # changing directions of triangles
        for i in range(3):
            angles[i + 3] += randint(-4, 4) / 10

        # checking for collision
        for i in range(6):

            if figures[i][0] >= (1200 - figures[i][2]) or figures[i][0] <= figures[i][2]:
                angles[i] = 3.14 - angles[i]
                figures[i][0] += round(v[i] * math.cos(angles[i]) / 30)
                figures[i][1] += round(v[i] * math.sin(angles[i]) / 30)

            if figures[i][1] >= (800 - figures[i][2]) or figures[i][1] <= figures[i][2]:
                angles[i] = - angles[i]
                figures[i][0] += round(v[i] * math.cos(angles[i]) / 30)
                figures[i][1] += round(v[i] * math.sin(angles[i]) / 30)

        # updating positions
        for i in range(6):
            if bool1[i]:
                figures[i] = new_figure()
                angles[i] = randint(0, 314 * 2) / 100
                bool1[i] = False

        # acceleration
        for i in range(6):
            if bool2[i]:
                v[i] = 300
            else:
                v[i] = 200

        # print username and score
        print_text('Your score: ' + str(score), GREEN, (10, 40), 36)
        print_text('Username: ' + name, GREEN, (10, 10), 36)

        # draw figures
        for i in range(3):
            draw_ball(figures[i])
            draw_triangle(figures[i+3])

        pygame.display.update()
        screen.fill(BLACK)
    return score


def menu():
    finished = False
    is_game = False
    name = ""
    while not finished:
        clock.tick(FPS)
        print_text("Enter your name: " + name, GREEN, (100, 300), 70)
        print_text("Press RightMouseButton to start", GREEN, (150, 400), 70)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                is_game = False

            elif event.type == pygame.KEYDOWN:
                if event.key == 13:
                    finished = True
                    is_game = True
                else:
                    name += event.unicode

        pygame.display.update()
        screen.fill(BLACK)

    user = [is_game, name]
    return user


def write_to_file(data):
    f = open('scores.txt', 'a')
    f.write(data)
    f.close()


def read_from_file():
    f = open('scores.txt', 'r')
    data = f.read()
    return data

sc = 0
pygame.display.update()
clock = pygame.time.Clock()

angles = [0., 0., 0., 0., 0., 0.]
figures = [0, 0, 0, 0, 0, 0]
bool1 = [0, 0, 0, 0, 0, 0]  # for catching
bool2 = [0, 0, 0, 0, 0, 0]  # for acceleration
v = [0, 0, 0, 0, 0, 0]

for k in range(6):
    angles[k] = randint(0, 314 * 2)/100
    figures[k] = new_figure()
    bool1[k] = False
    bool2[k] = False
    v[k] = 200.0

usr = menu()
if usr[0]:
    scr = game(sc, usr[1])
    print("Your score is", scr)
    write_to_file(str(usr[1]) + "  " + str(scr) + '\n')
    print(read_from_file()[0])

pygame.quit()
