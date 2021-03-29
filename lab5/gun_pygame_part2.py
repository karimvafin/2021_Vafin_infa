from classes import *

pygame.init()

FPS = 60

EXIT = False


def print_text(txt, color, position, size, background=WHITE):
    f1 = pygame.font.Font('/Users/karimvafin/opt/anaconda3/pkgs/matplotlib-base-3.3.2-py38h181983e_0/lib/python3.8/'
                          'site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf', size)
    text1 = f1.render(txt, True,
                      color, background)

    screen.blit(text1, position)


def new_game():
    # this variables are to change in this function
    global g1, targets, screen, balls, bullet, hit, count, text, EXIT, points, number_of_targets

    # initializing new targets, counters(bullet, count) and text

    number_of_targets += 1

    for i in range(number_of_targets):
        t1 = Target('circle', rnd(120))
        t2 = Target('triangle', rnd(120))
        targets += t1, t2

    for t in targets:
        t.new_target()
        t.live = 1

    is_targets_dead = False
    screen.fill(WHITE)
    bullet = 0
    finished = False
    text = ''
    count1 = 0
    count2 = 0
    for g in Guns:
        g.hp = 100

    while not finished:
        clock.tick(FPS)

        # checking for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True  # start next game
                EXIT = True  # exit from the program
            if event.type == pygame.MOUSEBUTTONUP:
                for g in Guns:
                    if g.active and g.hp > 0:
                        g.fire2_end(event)
                if not is_targets_dead:
                    bullet += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                for g in Guns:
                    if g.active:
                        g.fire2_start()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for g in Guns:
                        g.activation()

        print_text(text, BLACK, (200, 200), 20)
        print_text('Your points: ' + str(points), BLACK, (20, 20), 20)
        print_text('HP1: ' + str(g1.hp), BLACK, (20, 50), 20)
        print_text('HP2: ' + str(g2.hp), BLACK, (20, 80), 20)
        print_text('Level: ' + str(number_of_targets), BLACK, (20, 110), 20)

        # checking target lives matter
        is_targets_dead = True
        for t in targets:
            if t.live == 1:
                is_targets_dead = False

        # processing bullets
        for b in balls:
            b.move()  # moving them
            for t in targets:  # checking for collision
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    b.delete_ball()
                    points += 1

            if b.check_alive():  # deleting bullets if time is up
                b.delete_ball()

        if is_targets_dead:  # if targets disappeared
            text = 'Вы уничтожили цели за ' + str(bullet) + ' выстрелов'
            print_text(text, BLACK, (200, 200), 20)
            count1 += 1

        if count1 == 150:
            count1 = 0
            finished = True

        if g1.hp == 0 and g2.hp == 0:  # if you died
            count1 += 1
            text = 'YOU DIED'
            print_text(text, RED, (150, 200), 100)
            if count1 == 149:
                points = 0
                number_of_targets = 0

        # checking for collision of bombs
        for b in bombs:
            b.move()
            for g in Guns:
                if b.hittest(g):
                    g.hit = True
                    b.live = 0
                    if g.hp > 0:
                        g.hp -= 10
                    g.color = RED

            if b.check_alive():  # deleting bombs
                b.delete_ball()

        for g in Guns:
            if g.hit:  # timer for RED color of tank
                count2 += 1
                if count2 == 15:
                    g.hit = False
                    count2 = 0
            if g.hp != 0:
                if g.active:
                    g.targetting()
                    g.move_gun()
                g.draw_gun()
                g.power_up()

        # drawing objects and text
        for t in targets:
            if t.live == 1:
                t.draw_target()
                t.move()

        pygame.draw.polygon(screen, BROWN, ((0, 455), (800, 455), (800, 600), (0, 600)))
        print_text('Press SPACE to change the tank', BLACK, (270, 550), 15, BROWN)
        pygame.display.update()
        screen.fill(WHITE)
    targets = []


clock = pygame.time.Clock()

# initializing class objects and other variables
targets = []
number_of_targets = 0
g1 = Gun(80, True, 'Right')
g2 = Gun(700, True, 'Left')
Guns = [g1, g2]
g1.active = True
g2.active = False
count = 0
text = ''
points = 0
screen = pygame.display.set_mode((800, 600))

# the main loop
while not EXIT:
    new_game()
    screen.fill(WHITE)

pygame.quit()
