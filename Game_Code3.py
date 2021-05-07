import pygame
pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Boundaries")

icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

play1=pygame.image.load('spaceship.png')
x,y=350,650
vel=0
def player(x,y):
    screen.blit(play1,(x,y))

run=True
while run:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                vel+=0.5
            if event.key==pygame.K_LEFT:
                vel-=0.5
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
                vel=0
    x+=vel
    if x<0:
        x=0
    if x>736:
        x=736
    player(x,y)
    pygame.display.update()

pygame.quit()

