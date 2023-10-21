import pygame as pg,sys
from pygame.locals import *
import time

xo='x'
big_win=False
big_draw=False


b0= [[None]*3,[None]*3,[None]*3]
b1= [[None]*3,[None]*3,[None]*3]
b2= [[None]*3,[None]*3,[None]*3]
b3= [[None]*3,[None]*3,[None]*3]
b4= [[None]*3,[None]*3,[None]*3]
b5= [[None]*3,[None]*3,[None]*3]
b6= [[None]*3,[None]*3,[None]*3]
b7= [[None]*3,[None]*3,[None]*3]
b8= [[None]*3,[None]*3,[None]*3]
b9= [[None]*3,[None]*3,[None]*3]

boxes={1:b1,2:b2,3:b3,4:b4,5:b5,6:b6,7:b7,8:b8,9:b9}
draws={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}


pg.init()
CLOCK=pg.time.Clock()
white=(255,255,255)
black=(0,0,0)

sn_height=600
sn_width=600
sn=pg.display.set_mode((sn_width,sn_height+100),0,32)
pg.display.set_caption("ultimate tic tac toe!")

ximg=pg.image.load('images/X.png')
oimg=pg.image.load('images/O.png')
ximg=pg.transform.scale(ximg,(60,60))
oimg=pg.transform.scale(oimg,(60,60))
ximage=pg.transform.scale(ximg,(180,180))
oimage=pg.transform.scale(oimg,(180,180))

def game_opening():
    pg.display.update()
    time.sleep(1)
    sn.fill(white)
    for i in range(9):
        if i%3!=0:
            pg.draw.line(sn,black,(sn_width/9*i,20),(sn_width/9*i,sn_height-20),2)
            pg.draw.line(sn,black,(20,sn_height/9*i),(sn_width-20,sn_height/9*i),2)
    pg.draw.line(sn,black,(sn_width/3,0),(sn_width/3,sn_height),7)
    pg.draw.line(sn,black,(sn_width/3*2,0),(sn_width/3*2,sn_height),7)
    pg.draw.line(sn,black,(0,sn_height/3),(sn_width,sn_height/3),7)
    pg.draw.line(sn,black,(0,sn_height/3*2),(sn_width,sn_height/3*2),7)
    status_bar("X starts, location: Anywhere!")

def status_bar(message):
    font=pg.font.Font(None,30)
    text=font.render(message,1,(255,0,0))
    sn.fill((0,0,0),(0,600,600,100))
    text_rect=text.get_rect(center=(sn_width/2,650))
    sn.blit(text,text_rect)
    pg.display.update()

def click():
    x,y= pg.mouse.get_pos()

    if y<sn_height:

        col,row=None,None
        for i in range(1,10):
            if x<sn_width/9*i:
                col=i
                break
        for i in range(1,10):
            if y<sn_height/9*i:
                row=i
                break
        bnum=whichbox(row,col)
        b=boxes[bnum]
        if (row and col and b[row%3-1][col%3-1] is None):
            drawxo(row,col)
            check_win(b,bnum)
            r,c=find_next(row,col)
            status(whichbox(r,c))

def find_next(x,y):
    if(x in [1,4,7]):
        nx=1
    elif(x in [2,5,8]):
       nx=4 
    elif(x in [3,6,9]):
       nx=7 
    if(y in [1,4,7]):
        ny=1
    elif(y in [2,5,8]):
       ny=4 
    elif(y in [3,6,9]):
       ny=7 
    return nx,ny

def check_win(b,bnum):
    
    global small_win,big_win,small_draw
    small_win=None

    for i in range(3):
        if((b[i][0]==b[i][1]==b[i][2])and b[i][0] is not None):
            small_win=b[i][0]
            break
    for i in range(3):    
        if((b[0][i]==b[1][i]==b[2][i])and b[0][i] is not None):
            small_win=b[0][i]
            break
    if(b[0][0]==b[1][1]==b[2][2] and b[0][0] is not None):
        small_win=b[0][0]
    if(b[0][2]==b[1][1]==b[2][0] and b[2][0] is not None):
        small_win=b[0][2]
    
    if(all([all(row) for row in b])and small_win is None):
            small_draw=True
            draws[bnum]=True
            check_draw()

    if bnum in [1,4,7]:
        m=0
    elif bnum in [2,5,8]:
        m=1
    else:
        m=2
    
    if bnum in [1,2,3]:
        n=0
    elif bnum in [4,5,6]:
        n=1
    else:
        n=2
    
    if small_win and bnum==0:
        big_win=True
    elif small_win and bnum!=0:
        draw_large_xo(n,m,small_win)
        draws[bnum]=True
        check_win(b0,0)
        check_draw()



def check_draw():
    for i in range(1,10):
        if not draws[i]:
            return
    global big_draw 
    big_draw=True

def status(nb):
    
    if big_win:
        message=small_win.upper()+" wins BIG!"
    elif big_draw:
        message="DRAW GAME!"
    elif draws[nb]:
        message="play for "+xo.upper()+" in any box!"
    else:
        message="play for "+xo.upper()+" in box: "+str(nb)

    status_bar(message)

def draw_large_xo(n,m,small_winner):

    
    b0[n][m]=small_winner

    x=sn_height/3*m
    y=sn_width/3*n

    image= ximage if small_winner=='x' else oimage

    sn.blit(image,(x,y))

    

def whichbox(x,y):
    
    if(x<4) and(y<4):
        box=1
    elif((x<4 and y<7)and(y>3)):
        box=2
    elif((x<4)and (y>6)):
        box=3
    elif((x<7 and y<4)and(x>3 and y>0)):
        box=4
    elif((x<7 and y<7)and(x>3 and y>3)):
        box=5
    elif((x<7)and (x>3 and y>6)):
        box=6
    elif((x>6 and y<4)):
        box=7
    elif((x<10 and y<7)and(x>6 and y>3)):
        box=8
    else:
        box=9
    
    return box

def drawxo(row,col):
    global xo, b0,b1,b2,b3,b4,b5,b6,b7,b8,b9, sn_height, sn_width

    x,y=10,5

    for i in range(1,9):
        if row==i+1:
            x=sn_width/9*i
            break
    for i in range(1,9):
        if col==i+1:
            y=sn_height/9*i
            break
    
    b=boxes[whichbox(row,col)]
    b[row%3-1][col%3-1]=xo

    if (xo=='x'):
        sn.blit(ximg,(y,x))
        xo='o'
    else:
        sn.blit(oimg,(y,x))
        xo='x'
    pg.display.update()


game_opening()
state=True
while state:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            state=False
        elif event.type==MOUSEBUTTONDOWN:
            click()

    pg.display.update()
    CLOCK.tick(30)    

pg.quit()
quit()