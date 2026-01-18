from modules import sim
import pygame as pg
import random
import math

pg.init()

WIDTH, HEIGHT = 800, 600
BOUNDS = 200, 150

WR, HR = WIDTH / BOUNDS[0], HEIGHT / BOUNDS[1]

AGENTAMOUNT = 1500
CITYAMOUNT = 20

ctx = pg.display.set_mode((WIDTH, HEIGHT));
clock = pg.time.Clock()
run = True;

def pos(x, y):
    p = sim.pos()
    p.x = x
    p.y = y
    return p

s = sim.sim()


def polarToCartesian(r, theta):
    return pos(r * math.cos(theta), r * math.sin(theta))


def generateAgents():
    populationcenters = []
    for _ in range(CITYAMOUNT):
        populationcenters.append(pos(random.randint(0, BOUNDS[0]), random.randint(0, BOUNDS[1])))

    for _ in range(AGENTAMOUNT):
        if random.randint(0, 1) == 1:
            s.addIndividual(pos(random.randint(0, BOUNDS[0]), random.randint(0, BOUNDS[1])))
        else:
            r, theta = abs(random.gauss(0, 7)), random.uniform(0, 2 * math.pi)

            city = random.randrange(0, CITYAMOUNT)

            position = polarToCartesian(r, theta);
            position.x += populationcenters[city].x
            position.y += populationcenters[city].y

            s.addIndividual(position)

generateAgents()

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    
    ctx.fill((0, 0, 0));
    for i in s.individuals:
        pg.draw.aacircle(ctx, (255, 255, 255), (i.x * WR, i.y * HR), 2)

    pg.display.flip()

    clock.tick(60)
