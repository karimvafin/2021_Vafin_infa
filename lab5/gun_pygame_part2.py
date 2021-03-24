from classes import *

pygame.init()

FPS = 60

EXIT = False


def print_text(txt, color, position, size):
    f1 = pygame.font.Font('/Users/karimvafin/opt/anaconda3/pkgs/matplotlib-base-3.3.2-py38h181983e_0/lib/python3.8/'
                          'site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf', size)
    text1 = f1.render(txt, True,
                      color, WHITE)

    screen.blit(text1, position)


def new_game():
    global g1, targets, screen, balls, bullet, hit, count, text, EXIT, points

    t1.new_target()
    t2.new_target()
    screen.fill(WHITE)
    bullet = 0
    finished = False
    t1.live = 1
    t2.live = 1
    text = ''
    count = 0

    while not finished:
        clock.tick(FPS)
        if not balls and not t1.live and not t2.live:
            finished = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                EXIT = True
            if event.type == pygame.MOUSEBUTTONUP:
                g1.fire2_end(event)
                bullet += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                g1.fire2_start()

        for t in targets:
            t.draw_target()
            t.move()
        g1.targetting()
        g1.power_up()
        g1.draw_gun()
        print_text(text, BLACK, (200, 200), 20)
        print_text(str(points), BLACK, (20, 20), 30)

        for b in balls:
            b.move()
            for t in targets:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    points += 1

            if b.check_alive():
                b.delete_ball()
                balls.pop(0)

        if not t1.live and not t2.live:
            text = 'Вы уничтожили цели за ' + str(bullet) + ' выстрелов'
            print_text(text, BLACK, (200, 200), 20)
            count += 1
        if count == 150:
            count = 0
            hit = False
            break

        pygame.display.update()
        screen.fill(WHITE)


pygame.display.update()
clock = pygame.time.Clock()

t1 = Target('circle')
t2 = Target('triangle')
targets = [t1, t2]
g1 = Gun()
hit = False
count = 0
text = ''
points = 0
screen = pygame.display.set_mode((800, 600))

while not EXIT:
    new_game()
    screen.fill(WHITE)

pygame.quit()
