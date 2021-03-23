import pygame
from random import randrange as rnd, choice
import math
pygame.init()

FPS = 60
screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

EXIT = False


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
        self.live = 130

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
        global balls, bullet
        bullet += 1
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
        # self.x = 20 + max(self.f2_power, 20) * math.cos(self.an)
        # self.y = 450 + max(self.f2_power, 20) * math.sin(self.an)
        self.C = (self.x + self.f2_power * 25 * math.cos(self.an) + 5 * math.sin(self.an), self.y - self.f2_power
                  * 25 * math.sin(self.an) + 5 * math.cos(self.an))
        self.D = (self.x + self.f2_power * 25 * math.cos(self.an) - 5 * math.sin(self.an), self.y - self.f2_power
                  * 25 * math.sin(self.an) - 5 * math.cos(self.an))
        self.A = (self.x - 5 * math.sin(self.an), self.y - 5 * math.cos(self.an))
        self.B = (self.x + 5 * math.sin(self.an), self.y + 5 * math.cos(self.an))
        # self.draw_gun()

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 3:
                self.f2_power += 0.1
            self.color = RED
        else:
            self.color = BLACK


class Target:

    def __init__(self):
        self.live = 1
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = RED

    def draw_target(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 750)
        self.y = rnd(300, 520)
        self.r = rnd(5, 50)
        self.draw_target()

    def hit(self):
        """Попадание шарика в цель."""
        self.x = self.y = self.r = 0
        self.live = 0
        self.draw_target()


def print_text(txt, color, position, size):
    f1 = pygame.font.Font('/Users/karimvafin/opt/anaconda3/pkgs/matplotlib-base-3.3.2-py38h181983e_0/lib/python3.8/'
                          'site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf', size)
    text1 = f1.render(txt, True,
                      color, WHITE)

    screen.blit(text1, position)


t1 = Target()
g1 = Gun()
bullet = 0
balls = []
hit = False
count = 0
text = ''
points = 0

pygame.display.update()
clock = pygame.time.Clock()


def new_game():
    global g1, t1, screen, balls, bullet, hit, count, text, EXIT, points

    t1.new_target()
    bullet = 0
    balls = []
    screen.fill(WHITE)
    finished = False
    t1.live = 1
    text = ''
    count = 0

    while not finished:
        clock.tick(FPS)
        if not balls and not t1.live:
            finished = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                EXIT = True
            if event.type == pygame.MOUSEBUTTONUP:
                g1.fire2_end(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                g1.fire2_start()

        g1.targetting()
        g1.power_up()
        g1.draw_gun()
        t1.draw_target()
        print_text(text, BLACK, (200, 200), 20)
        print_text(str(points), BLACK, (20, 20), 30)

        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                points += 1
                text = 'Вы уничтожили цель за ' + str(bullet) + ' выстрелов'
                print_text(text, BLACK, (200, 200), 20)
                hit = True

            if b.check_alive():
                b.delete_ball()
                balls.pop(0)

        if hit:
            count += 1
        if count == 70:
            for i in range(len(balls)):
                balls[i].delete_ball()
            balls = []
            count = 0
            hit = False
            break

        pygame.display.update()
        screen.fill(WHITE)


while not EXIT:
    new_game()
    screen.fill(WHITE)

pygame.quit()
