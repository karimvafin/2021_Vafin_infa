import pygame
from random import randrange as rnd, choice
import math

# constants
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
BROWN = (158, 116, 39)
ORANGE = (253, 106, 2)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, ORANGE, BROWN]
screen = pygame.display.set_mode((800, 600))


class Ball:
    def __init__(self, x, y, live_time=150, type='bullet'):
        """

        :param x: start x
        :param y: start y
        :param live_time: when it will disappear
        :param type: 'bullet' or 'bomb'
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.live = live_time
        self.type = type

    def draw_ball(self):
        """
        Draws the ball
        :return:
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """
        Moves the ball in dependence of walls, type of class and physical laws
        """
        self.vy -= 0.7
        if self.x > 790 - self.r or self.x < self.r + 10:
            if self.type == 'bomb':
                self.live = 0
            self.vx = - 0.9 * self.vx
            self.x += self.vx

        if self.y > 455 - self.r:
            self.vy = - 0.7 * self.vy
            self.y = 455 - self.r
            self.vx *= 0.9
            if math.fabs(self.vx) < 0.05:
                self.vx = 0

        self.x += self.vx
        self.y -= self.vy
        self.live -= 1
        self.draw_ball()

    def hittest(self, obj):
        """
        Checks if collision with ball and object
        Args:
            obj: object
        Returns:
            If collision returns True, else returns False
        """
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2) < (self.r + obj.r)**2:
            return True
        else:
            return False

    def delete_ball(self):
        """
        Deletes ball from the screen
        :return:
        """
        global bombs, balls
        self.x = -10
        self.y = -10
        self.r = 0
        if self.type == 'bomb':
            bombs.pop(0)
        else:
            balls.pop(0)

    def check_alive(self):
        """
        Checks if ball's field "live"
        :return: True if live == 0, else False
        """
        if self.live == 0:
            return True
        else:
            return False


class Gun:

    def __init__(self, is_tank):
        self.position = [0, 0]  # position of mouse
        self.f2_power = 1
        self.f2_on = 0
        self.an = 1
        self.color = BLACK
        self.hit = False
        self.r = 40
        self.x = 50
        self.y = 420
        self.A = (self.x - 10 * math.sin(self.an), self.y - 10 * math.cos(self.an))
        self.B = (self.x + 10 * math.sin(self.an), self.y + 10 * math.cos(self.an))
        self.C = (self.x + self.f2_power * 100 * math.cos(self.an) + 10 * math.sin(self.an), self.y - self.f2_power
                  * 100 * math.sin(self.an) + 10 * math.cos(self.an))
        self.D = (self.x + self.f2_power * 100 * math.cos(self.an) - 10 * math.sin(self.an), self.y - self.f2_power
                  * 100 * math.sin(self.an) - 10 * math.cos(self.an))
        self.type = is_tank
        self.hp = 100

    def move_gun(self):
        """
        Moves the gun in dependence of keys
        :return:
        """
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.x -= 3
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.x += 3
        self.draw_gun()

    def draw_gun(self):
        """
        Draws the gun and tank if is_tank == True
        :return:
        """
        pygame.draw.polygon(screen, self.color, (self.C, self.D, self.A, self.B))
        if self.type:
            pygame.draw.polygon(screen, self.color, ((self.x + 10, self.y - 10), (self.x + 15, self.y + 10),
                                                     (self.x - 50, self.y + 10), (self.x - 45, self.y - 10)))
            pygame.draw.polygon(screen, self.color, ((self.x - 60, self.y + 10), (self.x + 40, self.y + 10),
                                                     (self.x + 50, self.y + 20),
                                                     (self.x + 45, self.y + 35), (self.x - 55, self.y + 35)))

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Produces the shot
        """
        global balls
        new_ball = Ball(self.x, self.y)
        new_ball.r += 5
        new_ball.vx = 8 * self.f2_power * math.cos(self.an)
        new_ball.vy = 8 * self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 1

    def targetting(self):
        """
        Rotates the gun
        :return:
        """
        self.position = pygame.mouse.get_pos()
        if not self.type and self.position[0] - self.x != 0 and self.position[0] < self.x:
            self.an = 3.14 - math.atan((self.position[1] - self.y) / (self.position[0] - self.x))
        if self.position[0] - self.x != 0 and self.position[0] > self.x:
            self.an = - math.atan((self.position[1] - self.y) / (self.position[0] - self.x))
        if self.position[0] - self.x == 0:
            if self.position[1] > self.y:
                self.an = -1.57
            if self.position[1] <= self.y:
                self.an = 1.57
        if self.f2_on:
            self.color = ORANGE
        else:
            if self.hit:
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
        """
        Enlarge the gun if f2_on == 1
        :return:
        """
        if self.f2_on:
            if self.f2_power < 3:
                self.f2_power += 0.1
            self.color = ORANGE
        else:
            if self.hit:
                self.color = RED
            else:
                self.color = BLACK


class Target:

    def __init__(self, type):
        """
        Randomly moves the ball in dependence of walls
        :param type: 'circle' or 'triangle'
        """
        self.angle = 1
        self.v = 3
        self.live = 1
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = choice(COLORS)
        self.type = type
        self.active = 130  # bombs will be created each self.active iterations

    def draw_target(self):
        """
        Draws the target in dependence of type
        Creating bombs
        :return:
        """
        if self.type == 'circle':
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        if self.type == 'triangle':
            pygame.draw.polygon(screen, self.color, ((self.x, self.y - self.r * math.sqrt(3) / 3),
                                    (self.x - self.r / 2, self.y + math.sqrt(3) * self.r / 6),
                                    (self.x + self.r / 2, self.y + math.sqrt(3) * self.r / 6)))
        if self.active > 0:
            self.active -= 1
        else:
            if self.live == 1:
                self.new_bomb()
                self.active = 130

    def new_bomb(self):
        """
        Created class Ball with type 'bomb'
        :return:
        """
        global bombs
        new_bomb = Ball(self.x, self.y, 30, 'bomb')
        new_bomb.color = BLACK
        bombs += [new_bomb]
        new_bomb.r = 10

    def new_target(self):
        """ Initial new target """
        self.x = rnd(100, 750)
        self.y = rnd(100, 280)
        self.r = rnd(5, 50)

    def move(self):
        """
        Randomly moves the ball in dependence of walls
        """
        if self.x > 790 - self.r or self.x < self.r + 10:
            self.v = - self.v
        if self.y > 300 - self.r or self.y < self.r + 10:
            self.v = - self.v

        self.angle += rnd(-15, 15) / 100
        self.x += self.v * math.cos(self.angle)
        self.y += self.v * math.sin(self.angle)

    def hit(self):
        """ This function is called when hit to remove the target """
        self.x = self.y = self.r = 0
        self.live = 0


# global lists of objects
balls = []
bombs = []
