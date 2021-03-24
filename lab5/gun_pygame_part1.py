from classes import *

pygame.init()

FPS = 60

EXIT = False


def print_text(txt, color, position, size):
    """
    This function prints colored text with certain size on the screen in position
    :param txt: text you want to print
    :param color: color of the text
    :param position: (x, y)
    :param size: size of the text
    :return:
    """
    f1 = pygame.font.Font('/Users/karimvafin/opt/anaconda3/pkgs/matplotlib-base-3.3.2-py38h181983e_0/lib/python3.8/'
                          'site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSansMono-Oblique.ttf', size)
    text1 = f1.render(txt, True,
                      color, WHITE)

    screen.blit(text1, position)


def new_game():
    """
    This function launches the game
    :return:
    """
    # this variables are to change in this function
    global g1, targets, screen, balls, bullet, hit, count, text, EXIT, points

    # initializing new targets, counters(bullet, count) and text
    t1.new_target()
    t2.new_target()
    bullet = 0
    finished = False
    t1.live = 1
    t2.live = 1
    text = ''
    count = 0  # counter that is used for stop the game loop

    screen.fill(WHITE)

    while not finished:
        clock.tick(FPS)

        # checking for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True  # start next game
                EXIT = True  # exit from the program
            if event.type == pygame.MOUSEBUTTONUP:
                g1.fire2_end(event)
                if t1.live or t2.live:
                    bullet += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                g1.fire2_start()

        # drawing objects and text
        for t in targets:
            t.draw_target()
            t.move()
        g1.targetting()
        g1.power_up()
        g1.draw_gun()
        print_text(text, BLACK, (200, 200), 20)
        print_text(str(points), BLACK, (20, 20), 30)

        # processing bullets
        for b in balls:
            b.move()  # moving them
            for t in targets:  # checking for collision
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    points += 1

            if b.check_alive():  # deleting bullets if time is up
                b.delete_ball()

        if not t1.live and not t2.live:  # if targets disappeared
            text = 'Вы уничтожили цели за ' + str(bullet) + ' выстрелов'
            print_text(text, BLACK, (200, 200), 20)
            count += 1

        if count == 150:  # timer in order not to allow the game end instantly
            count = 0
            finished = True

        # updating the screen
        pygame.display.update()
        screen.fill(WHITE)


clock = pygame.time.Clock()

# initializing class objects and other variables
t1 = Target('circle')
t2 = Target('triangle')
targets = [t1, t2]
g1 = Gun(False)
text = ''
points = 0  # counts your hits
screen = pygame.display.set_mode((800, 600))

# the main loop
while not EXIT:
    new_game()
    screen.fill(WHITE)

pygame.quit()
