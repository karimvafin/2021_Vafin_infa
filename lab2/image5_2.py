import pygame
import pygame.draw as draw


def bird(x, y, k):
    """
    рисует птичек
    :param x:
    :param y:
    :param k:
    :return:
    """
    draw.polygon(screen, (0, 0, 0),
                 [(x, y), (x + 2 * k, y), (x + 4 * k, y + 0.5 * k), (x + 8 * k, y + 2.5 * k), (x + 10 * k, y + 1.5 * k),
                  (x + 13 * k, y + 0.5 * k), (x + 16 * k, y + 0.5 * k), (x + 8 * k, y + 4 * k), (x, y)])


def brown_mount():
    """
    рисует коричневые горы
    :return:
    """
    draw.polygon(screen, (131, 38, 26),
                 [(0, 400), (10, 400), (70, 420), (80, 600), (0, 600)])  # левый кусок коричневой горы
    draw.polygon(screen, (131, 38, 26),
                 [(100, 600), (300, 380), (420, 420), (440, 370), (600, 390), (650, 450), (700, 420), (900, 440),
                  (980, 420),
                  (1030, 450), (1070, 420), (1180, 440), (1300, 350), (1300, 600)])  # коричневая гора
    draw.ellipse(screen, (131, 38, 26), (730, 360, 200, 250))  # эллиптические куски коричневой горы
    draw.ellipse(screen, (131, 38, 26), (50, 300, 175, 300))  # эллиптические куски коричневой горы


def yellow_mount():
    """
    рисует жёлтые горы
    :return:
    """
    draw.polygon(screen, (249, 166, 2),
                 [(0, 350), (70, 310), (80, 309), (90, 308), (100, 307), (110, 305), (120, 302), (130, 299), (140, 295),
                  (150, 291), (160, 286), (170, 281), (300, 180), (350, 200), (430, 290), (600, 260), (700, 280),
                  (800, 250),
                  (850, 280), (900, 250), (1300, 0), (1300, 250)])  # желтая гора


def purple_mount():
    """
    рисует фиолетовые горы
    :return:
    """
    draw.polygon(screen, (35, 0, 70), [(0, 450), (180, 480), (400, 630), (450, 690), (480, 720), (650, 710), (800, 650),
                                       (950, 690), (1050, 650), (1070, 620), (1170, 580), (1200, 550), (1300, 500),
                                       (1300, 750), (0, 750)])


def ship():
    """
    рисует кораблик
    :return:
    """
    draw.polygon(screen, (210, 105, 30), [[350, 550], [490, 550], [470, 600], [370, 600]])
    draw.polygon(screen, (0, 0, 0), [[350, 550], [490, 550], [470, 600], [370, 600]], 1)
    draw.polygon(screen, (0, 0, 255), [[430, 550], [430, 470], [480, 550]])
    draw.polygon(screen, (0, 0, 0), [[430, 550], [430, 470], [480, 550]], 1)


def clouds(x, y, rrr):
    """
    рисует облака по заданным кооринатам и радиусу
    :param x:
    :param y:
    :param rrr:
    :return:
    """
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 2 * rrr / 3)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 2 * rrr / 3, 1)
    for j in range(6):
        if j == 1 or j == 3 or j == 5:
            x = x + 2 * rrr / 3
        if j == 2:
            y = y - 2 * rrr / 3
        if j == 4:
            y = y + 2 * rrr / 3
        pygame.draw.circle(screen, (255, 255, 255), (x, y), 2 * rrr / 3)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 2 * rrr / 3, 1)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1300, 750))
draw.polygon(screen, (252, 244, 163), [(0, 375), (0, 500), (1300, 500), (1300, 375)])  # второй фон снизу
draw.polygon(screen, (255, 253, 208), [(0, 375), (0, 200), (1300, 200), (1300, 375)])  # третий фон снизу
draw.polygon(screen, (255, 229, 180), [(0, 0), (1300, 0), (1300, 200), (0, 200)])  # четвертый фон снизу

yellow_mount()
brown_mount()
draw.polygon(screen, (216, 191, 216), [(1400, 750), (0, 750), (0, 550), (1400, 500)])  # первый фон снизу
draw.circle(screen, (255, 211, 0), (650, 170), 65)  # солнце

# выполнение функций
bird(450, 300, 6)
bird(500, 280, 6)
bird(430, 340, 6)
bird(530, 340, 5)
bird(700, 550, 10)
bird(1000, 550, 7)
bird(880, 650, 5)
bird(970, 600, 7)
purple_mount()
ship()
clouds(100, 120, 60)
clouds(500, 100, 50)
clouds(600, 150, 60)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
