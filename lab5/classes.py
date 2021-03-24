import pygame
from random import randrange as rnd, choice
import math

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
screen = pygame.display.set_mode((800, 600))
bullet = 0


class Ball:
    def __init__(self, x=50, y=420):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = [self.x, self.y, self.r]
        self.live = 150

    def draw_ball(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy -= 0.7
        if self.x > 790 - self.r or self.x < self.r + 10:
            self.vx = - 0.9 * self.vx
            self.x += self.vx
        if self.y > 570 - self.r:
            self.vy = - 0.7 * self.vy
            self.y = 570 - self.r
            self.vx *= 0.9
            if math.fabs(self.vx) < 0.05:
                self.vx = 0

        self.x += self.vx
        self.y -= self.vy - 0.7
        self.live -= 1
        self.draw_ball()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2) < (self.r + obj.r)**2:
            return True
        else:
            return False

    def delete_ball(self):
        self.x = -10
        self.y = -10
        self.r = 0
        self.draw_ball()

    def decrement(self):
        self.live -= 1

    def check_alive(self):
        if self.live == 0:
            return True
        else:
            return False


class Gun:

    def __init__(self):
        self.position = [0, 0]
        self.f2_power = 1
        self.f2_on = 0
        self.an = 1
        self.color = BLACK
        self.x = 50
        self.y = 420
        self.A = (self.x - 10 * math.sin(self.an), self.y - 10 * math.cos(self.an))
        self.B = (self.x + 10 * math.sin(self.an), self.y + 10 * math.cos(self.an))
        self.C = (self.x + self.f2_power * 100 * math.cos(self.an) + 10 * math.sin(self.an), self.y - self.f2_power
                  * 100 * math.sin(self.an) + 10 * math.cos(self.an))
        self.D = (self.x + self.f2_power * 100 * math.cos(self.an) - 10 * math.sin(self.an), self.y - self.f2_power
                  * 100 * math.sin(self.an) - 10 * math.cos(self.an))

    def draw_gun(self):
        pygame.draw.polygon(screen, self.color, (self.C, self.D, self.A, self.B))

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.pos[1]-new_ball.y) / (event.pos[0]-new_ball.x))
        new_ball.vx = 8 * self.f2_power * math.cos(self.an)
        new_ball.vy = - 8 * self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 1

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        self.position = pygame.mouse.get_pos()
        if self.position[0] - 20 != 0:
            self.an = - math.atan((self.position[1] - 450) / (self.position[0] - 20))
        else:
            self.an = 1.57
        if self.f2_on:
            self.color = RED
        else:
            self.color = BLACK
        self.C = (self.x + self.f2_power * 25 * math.cos(self.an) + 5 * math.sin(self.an), self.y - self.f2_power
                  * 25 * math.sin(self.an) + 5 * math.cos(self.an))
        self.D = (self.x + self.f2_power * 25 * math.cos(self.an) - 5 * math.sin(self.an), self.y - self.f2_power
                  * 25 * math.sin(self.an) - 5 * math.cos(self.an))
        self.A = (self.x - 5 * math.sin(self.an), self.y - 5 * math.cos(self.an))
        self.B = (self.x + 5 * math.sin(self.an), self.y + 5 * math.cos(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 3:
                self.f2_power += 0.1
            self.color = RED
        else:
            self.color = BLACK


class Target:

    def __init__(self, type):
        self.angle = 1
        self.v = 3
        self.live = 1
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = choice(COLORS)
        self.type = type

    def draw_target(self):
        if self.type == 'circle':
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        if self.type == 'triangle':
            pygame.draw.polygon(screen, self.color, ((self.x, self.y - self.r * math.sqrt(3) / 3),
                                    (self.x - self.r / 2, self.y + math.sqrt(3) * self.r / 6),
                                    (self.x + self.r / 2, self.y + math.sqrt(3) * self.r / 6)))

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 750)
        self.y = rnd(300, 520)
        self.r = rnd(5, 50)
        self.draw_target()

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x > 790 - self.r or self.x < 400 + self.r + 10:
            self.v = - self.v
        if self.y > 570 - self.r or self.y < 200:
            self.v = - self.v

        self.angle += rnd(-15, 15) / 100
        self.x += self.v * math.cos(self.angle)
        self.y += self.v * math.sin(self.angle)
        self.draw_target()

    def hit(self):
        """Попадание шарика в цель."""
        self.x = self.y = self.r = 0
        self.live = 0
        self.draw_target()


balls = []
