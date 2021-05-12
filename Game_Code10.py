import pygame,random,math
pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Space Invader")

icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

play1=pygame.image.load('spaceship.png')
enemy1=pygame.image.load('enemy.png')
bullet1=pygame.image.load('bullet.png')
bullX=0
bullY=650
bull_vel=1
bull_state="ready"
x1=random.randint(0,735)
y1=random.randint(50,150)
x,y=350,650
vel,vel1=0,0.9
score_val=0
font=pygame.font.Font('freesansbold.ttf',32)
over_font=pygame.font.Font('freesansbold.ttf',64)
def over_game(x,y):
    over = over_font.render("GAME OVER ",True, (255,225,255))
    screen.blit(over, (x, y))
def show_score(x,y):
    score=font.render("Score: "+str(score_val),True,(125,220,155))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(play1,(x,y))
def enemyplayer(x1,y1):
    screen.blit(enemy1, (x1, y1))
def bullet_shot(x,y):
    global bull_state
    bull_state="fire"
    screen.blit(bullet1,(x+14,y+10))
def isCollision(x,y,x1,y1):
    if bull_state=="ready":
        return 0
    m = math.sqrt(math.pow((x - x1), 2) + math.pow((y - y1), 2))
    if m < 27:
        return True
    else:
        return False
run=True
while run:
    screen.fill((0,0,0))
    pygame.draw.line(screen,(0,0,255),(0,645),(800,645))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                vel+=0.5
            if event.key==pygame.K_LEFT:
                vel-=0.5
            if event.key==pygame.K_SPACE:
                if bull_state=="ready":
                    bullX=x
                    bullet_shot(bullX,bullY)
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
                vel=0

    x+=vel
    x1+=vel1
    if x<0:
        x=0
    if x>736:
        x=736
    if x1<0:
        x1=0
        vel1=0.9
        y1+=40
    if x1>736:
        x1=736
        vel1=-0.9
        y1+=40
    if y1>=645-55:
        y=1000
        y1=2000
        over = over_font.render("GAME OVER ", True, (255, 225, 255))
        screen.blit(over, (200, 400))
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(200,380,400,90),2)
        #pygame.display.flip()

    if bullY<0:
        bullY=650
        bull_state="ready"
    if bull_state == "fire":
        bullet_shot(bullX,bullY)
        bullY-=bull_vel
    if isCollision(x1,y1,bullX,bullY):
        x1 = random.randint(0, 735)
        y1 = random.randint(50, 150)
        bull_state="ready"
        bullY = 650
        score_val+=1

    player(x,y)
    enemyplayer(x1,y1)
    show_score(10,20)
    pygame.display.update()

pygame.quit()