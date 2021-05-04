import pygame
pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Space Invaders")

icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

play1=pygame.image.load('spaceship.png')
x,y=370,650
def player(x,y):
    screen.blit(play1,(x,y))

run=True

while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    player(x,y)
    pygame.display.update()
pygame.quit()