import pygame
import random
import math

#pygame initialize
pygame.init()

#create screen
screen=pygame.display.set_mode((800,600))

#icon and title
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#background
backgroundImg=pygame.image.load("background.png")

#BACKGROUND MUSIC
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

#player
playerImg=pygame.image.load("player.png")
playerX=370
playerY=500
playerX_change=0

#Score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
fontX=10
fontY=10

def show_score(x,y):
    score=font.render("Score: " + str(score_value) , True , (255,255,255))
    screen.blit(score,(x,y))

def show_game_over():
    font=pygame.font.Font("freesansbold.ttf",50)
    final_score=font.render("Final Score: "+str(score_value) , True , (255,255,255))
    game_over=font.render("GAME OVER",True,(255,255,255))
    screen.blit(game_over,(250,200))
    screen.blit(final_score,(235,280))

def player(x,y):   #to print player on screen
    screen.blit(playerImg,(x,y))

#bullet
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=500
bulletX_change=0
bulletY_change=4
bullet_state="ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+15,y+10))

#Enemy
enemyImg=pygame.image.load("enemy.png")
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemy=6
for i in range(num_of_enemy):
    enemyX.append(random.randint(20,700))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(2.5)
    enemyY_change.append(40)

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2))
    if distance<27:
        return True
    else:
        return False

#main screen
running=True
while running:

    screen.fill((56,2,63)) #screen colour

    screen.blit(backgroundImg,(0,0))

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-3
            if event.key==pygame.K_RIGHT:
                playerX_change=3
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    playerX+=playerX_change

    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    if bulletY<=0:
        bulletY=500
        bullet_state="ready"

    #bullet
    if bullet_state=="fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    for i in range(num_of_enemy):       #enemy for loop

        if enemyY[i]>430:
            for j in range(num_of_enemy):
                enemyY[j]=1000
            show_game_over()
        if enemyX[i]<=0:
            enemyX[i]=0
        elif enemyX[i]>=736:
            enemyX[i]=736

        if enemyX[i]==0:
            enemyX_change[i]=2.5
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]==736:
            enemyX_change[i]=-2.5
            enemyY[i]+=enemyY_change[i]

        enemyX[i]+=enemyX_change[i]

        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)

        if collision:
            bulletY=500
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(20,700)
            enemyY[i]=random.randint(0,150)

        enemy(enemyX[i],enemyY[i])

    show_score(fontX,fontY)

    player(playerX,playerY)

    pygame.display.update()
