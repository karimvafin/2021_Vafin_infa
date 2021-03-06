import pygame
from pygame.draw import *


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1300, 750))
polygon(screen, (252, 244, 163), [(0, 375), (0, 500), (1300, 500), (1300, 375)])  # второй фон снизу
polygon(screen, (255, 253, 208), [(0, 375), (0, 200), (1300, 200), (1300, 375)])  # третий фон снизу
polygon(screen, (255, 229, 180), [(0, 0), (1300, 0), (1300, 200), (0, 200)])  # четвертый фон снизу


polygon(screen, (131, 38, 26), [(0, 400), (10, 400), (70, 420), (80, 600), (0, 600)])  # левый кусок коричневой горы
polygon(screen, (249, 166, 2), [(0, 350), (70, 310), (80, 309), (90, 308), (100, 307), (110, 305), (120, 302), (130, 299), (140, 295), (150, 291), (160, 286), (170, 281), (300, 180), (350, 200), (430, 290), (600, 260), (700, 280), (800, 250), (850, 280), (900, 250), (1300, 0), (1300, 250)])  # желтая гора
polygon(screen, (131, 38, 26), [(100, 600), (300, 380), (420, 420), (440, 370), (600, 390), (650, 450), (700, 420), (900, 440), (980, 420), (1030, 450), (1070, 420), (1180, 440), (1300, 350), (1300, 600)])  # коричневая гора
ellipse(screen, (131, 38, 26), (730, 360, 200, 250))  # эллиптические куски коричневой горы
ellipse(screen, (131, 38, 26), (50, 300, 175, 300))  # эллиптические куски коричневой горы
polygon(screen, (216, 191, 216), [(1400, 750), (0, 750), (0, 550), (1400, 500)])  # первый фон снизу
circle(screen, (255, 211, 0), (650, 170), 65)  # солнце

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

