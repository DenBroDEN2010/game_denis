
from object import Object
from Player import Player
from setting import *

pg.init()

screen = pg.display.set_mode((setting['w'], setting['h']))
pg.display.set_caption(setting['title'])

clock = pg.time.Clock()

all_sprite = pg.sprite.Group()
obstacle_group = pg.sprite.Group()

player = Player()
all_sprite.add(player)


def new_mobs():
    obstacle_bottom = Object(setting['w'], 100)
    obstacle_top = Object(setting['w'], 200)
    obstacle_group.add(obstacle_top, obstacle_bottom)
    all_sprite.add(obstacle_group)


SPAWN_SPRITE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_SPRITE, 1500)

run = True
while run:
    clock.tick(setting['fps'])
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == SPAWN_SPRITE:
            new_mobs()

    all_sprite.update()

    screen.fill('green')
    all_sprite.draw(screen)
    pg.display.flip()

pg.quit()



from setting import *

pg.init()

# настройки экрана
screen = pg.display.set_mode((setting['w'], setting['h']))
pg.display.set_caption(setting['title'])
clock = pg.time.Clock()

# игровой цикл
run = True
while run:
    clock.tick(setting['fps'])

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

            # рендер

            screen.fill('green')
            pg.display.flip()

pg.init()
