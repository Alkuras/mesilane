from random import *
import pygame,sys


def drawflower(coords):
   
            pygame.draw.circle(screen,red,(coords[i][0],coords[i][1]),20)
     
   
            

def rightmove(spdx,posx):
    posx+= spdx
    return posx

def leftmove(spdx,posx):
     posx-= spdx
     return posx

def diagonalmove(spdx,spdy,posx,posy):

    posx-= spdx
    posy-= spdy
    return posx,posy

def startpos():
    p=randint(1,4)
    if p==1:
        posx=5
        posy=5
    elif p==2:
        posx=700
        posy=5
    elif p==3:
        posx=5
        posy=500
    elif p==4:
        posx=700
        posy=500
    return posx,posy

def startposW():
    p=randint(1,4)
    if p==1:
        posx=200
        posy=100
    elif p==2:
        posx=400
        posy=200
    elif p==3:
        posx=400
        posy=300
    elif p==4:
        posx=400
        posy=300
    return posx,posy

def drawbee(x,y):
    global bee
    bee=pygame.image.load("bee.png")
    bee=pygame.transform.scale(bee,(80,80))
    
    screen.blit(bee,(x,y))

    pygame.display
    return bee

def drawwasp(x,y,l):
    global wasp
    if l=="l":
        waspl=pygame.image.load("waspl.png")
        waspl=pygame.transform.scale(wasp,(100,100))
    
        screen.blit(waspl,(x,y))

        pygame.display
        return wasp
    elif d=="r":
        wasp=pygame.image.load("wasp.png")
        wasp=pygame.transform.scale(wasp,(100,100))
    
        screen.blit(wasp,(x,y))

        pygame.display
        return wasp
pygame.init()

yellow=[255,255,0]
red=[255,0,0]
green=[0,255,0]
grey=[128,128,128]
blue=[0,0,255]
purple=[255,0,255]

screenx=800
screeny=600

x=randint(100,600) 
y=randint(50,500)
coords=[]
flowers=[]

for i in range(10):
    posx=randint(5,screenx-50)
    posy=randint(5,screeny-50)
    coords.append([posx,posy])
for i in range(10):
    flowers.append(pygame.Rect(int(coords[i][0])-15,int(coords[i][1]-15),30,30))



flowercounter=0
totalflowers=5
score=0



r=randint(1,3)
screen=pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Animeerimine")
screen.fill(blue)
clock=pygame.time.Clock()
d="r"
posx,posy=startpos()
posxw,posyw=startposW()
speedx=2
speedy=2
speedxw=2
speedyw=2
gameover=False
while not gameover:
    beea=pygame.Rect(posx,posy,80,80)
    waspp=pygame.Rect(posxw,posyw,100,100)
    # pygame.draw.rect(screen,blue,beea)
    # pygame.draw.rect(screen,blue,waspp)
    clock.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT:

         sys.exit()
    for i in range(10):
        drawflower(coords)
    drawbee(posx,posy)
    drawwasp(posxw,posyw,d)
    posxw=rightmove(speedx,posxw)

    # flowercounter+=1
    # if flowercounter >=totalflowers:
    #     flowercounter=0
    #     flowers.append(pygame.Rect(int(coords[i][0]),int(coords[i][1]),-30,-30))

    for flower in flowers[:]:
        if beea.colliderect(flower):
            flowers.remove(flower)
            score+=1
    # for flower in flowers:
    #     pygame.draw.rect(screen,flower)

    if r==1:
        posx,posy=diagonalmove(speedx,speedy,posx,posy)
    elif r==2:
        posx=rightmove(speedx,posx)
    elif r==3:
        posx=leftmove(speedx,posx)
    if posx>screenx-bee.get_rect().width or posx <0:
        speedx= -speedx
        r=1
    if posy > screeny-bee.get_rect().height or posy <0:
        speedy= -speedy
        r=1
    if posxw>screenx-wasp.get_rect().width or posxw <0:
        speedxw= -speedxw
        d="l"
    if posyw > screeny-wasp.get_rect().height or posyw <0:
        speedyw= -speedyw
        
    pygame.display.flip()
    screen.fill(green)
    print(score)
    if score>9:
        gameover=True

pygame.quit()