from unicodedata import name
import pygame as pg,sys
from pygame.locals import *
import time
def mini():
    XO='x'
    winner=None
    draw=False
    width=400
    height=400
    white=(255,255,255)
    line_color=(10,10,10)

    TTT=[[None]*3,[None]*3,[None]*3]

    pg.init()
    fps=30
    CLOCK=pg.time.Clock()
    screen=pg.display.set_mode((width,height+100),0,32)
    pg.display.set_caption("Tic Tac Toe")

    #opening=pg.image.load('tic tac opening.png')
    x_img=pg.image.load('images/X.png')
    o_img=pg.image.load('images/O.png')

    x_img=pg.transform.scale(x_img,(80,80))
    o_img=pg.transform.scale(o_img,(80,80))
    #opening=pg.transform.scale(opening,(width,height+100))

    def game_opening():
        #screen.blit(opening,(0,0))
        pg.display.update()
        time.sleep(1)
        screen.fill(white)

        pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
        pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)

        pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
        pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)
        draw_status()

    def draw_status():
        global draw

        if winner is None:
            message=XO.upper()+"'s Turn"
        else:
            message=winner.upper()+"won!"
        #if draw:
            #message="game draw!"

        font=pg.font.Font(None,30)
        text=font.render(message,1,(255,255,255))
        screen.fill((0,0,0),(0,400,500,100))
        text_rect=text.get_rect(center=(width/2,500-50))
        screen.blit(text,text_rect)
        pg.display.update()


    def check_win():
        global TTT,winner,draw

        for row in range(0,3):
            if((TTT[row][0]==TTT[row][1]==TTT[row][2])and(TTT[row][0] is not None)):
                winner=TTT[row][0]
                break
        for col in range(0,3):
            if((TTT[0][col]==TTT[1][col]==TTT[2][col])and (TTT[0][col] is not None)):
                winner=TTT[0][col]
                break
        if(TTT[0][0]==TTT[1][1]==TTT[2][2]) and (TTT[0][0] is not None):
            winner=TTT[0][0]
        if(TTT[0][2]==TTT[1][1]==TTT[2][0]) and (TTT[0][2] is not None):
            winner=TTT[0][2]
        if(all([all(row) for row in TTT])and winner is None):
            draw=True
        draw_status()

    def drawxo(row,col):
        global TTT,XO
        if row==1:
            posx=30
        if row==2:
            posx=width/3 +30
        if row==3:
            posx=width/3*2 +30
        if col==1:
            posy=30
        if col==2:
            posy=height/3 +30
        if col==3:
            posy=height/3*2 +30
        TTT[row-1][col-1]=XO
        if (XO=='x'):
            screen.blit(x_img,(posy,posx))
            XO='o'
        else:
            screen.blit(o_img,(posy,posx))
            XO='x'
        pg.display.update()


    def userclick():
        x,y=pg.mouse.get_pos()

        if (x<width/3):
            col=1
        elif(x<width/3*2):
            col=2
        elif(x<width):
            col=3
        else:
            col=None
        if(y<height/3):
            row=1
        elif(y<height/3*2):
            row=2
        elif(y<height):
            row=3
        else:
            row=None
        
        if(row and col and TTT[row-1][col-1] is None):
            global XO
            drawxo(row,col)
            check_win()

    def reset_game():
        global TTT,winner,XO,draw
        time.sleep(3)
        XO='x'
        draw=False
        game_opening()
        winner=None
        TTT=[[None]*3,[None]*3,[None]*3]

    game_opening()

    while(True):
        for event in pg.event.get():
            if event.type==QUIT:
                pg.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                userclick()
                if(winner or draw):
                    reset_game()
        pg.display.update()
        CLOCK.tick(fps)


xo='x'
mini_winner=None
mini_draw=False
g=[[None]*9 for i in range(9)]

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

def game_opening():
    pg.display.update()
    time.sleep(1)
    sn.fill(white)
    pg.draw.line(sn,black,(sn_width/3,0),(sn_width/3,sn_height),7)
    pg.draw.line(sn,black,(sn_width/9,20),(sn_width/9,sn_height-20),2)
    pg.draw.line(sn,black,(sn_width/3*2,0),(sn_width/3*2,sn_height),7)
    pg.draw.line(sn,black,(sn_width/9*4,20),(sn_width/9*4,sn_height-20),2)
    pg.draw.line(sn,black,(sn_width/9*7,20),(sn_width/9*7,sn_height-20),2)
    pg.draw.line(sn,black,(sn_width/9*2,20),(sn_width/9*2,sn_height-20),2)
    pg.draw.line(sn,black,(sn_width/9*5,20),(sn_width/9*5,sn_height-20),2)
    pg.draw.line(sn,black,(sn_width/9*8,20),(sn_width/9*8,sn_height-20),2)

    pg.draw.line(sn,black,(0,sn_height/3),(sn_width,sn_height/3),7)
    pg.draw.line(sn,black,(20,sn_height/9),(sn_width-20,sn_height/9),2)
    pg.draw.line(sn,black,(0,sn_height/3*2),(sn_width,sn_height/3*2),7)
    pg.draw.line(sn,black,(20,sn_height/9*2),(sn_width-20,sn_height/9*2),2)
    pg.draw.line(sn,black,(20,sn_height/9*4),(sn_width-20,sn_height/9*4),2)
    pg.draw.line(sn,black,(20,sn_height/9*5),(sn_width-20,sn_height/9*5),2)
    pg.draw.line(sn,black,(20,sn_height/9*7),(sn_width-20,sn_height/9*7),2)
    pg.draw.line(sn,black,(20,sn_height/9*8),(sn_width-20,sn_height/9*8),2)

def status(x):
    global mini_draw

    if mini_winner is None:
        message=xo.upper()+"'s turn"
    else:
        message=mini_winner.upper()+"won"
    if mini_draw:
        message=" mini draw"
    if(x==1):
        message=message+",   next grid= "+ng

    font=pg.font.Font(None,30)
    text=font.render(message,1,(255,0,0))
    sn.fill((0,0,0),(0,600,600,100))
    text_rect=text.get_rect(center=(sn_width/2,650))
    sn.blit(text,text_rect)
    pg.display.update()

def mini_win(grid,x,y):
    global g,mini_winner,mini_draw

    g1=[grid[0][0:3],grid[1][0:3],grid[2][0:3]]
    g2=[grid[0][3:6],grid[1][3:6],grid[2][3:6]]
    g3=[grid[0][6:9],grid[1][6:9],grid[2][6:9]]
    g4=[grid[3][0:3],grid[4][0:3],grid[5][0:3]]
    g5=[grid[3][3:6],grid[4][3:6],grid[5][3:6]]
    g6=[grid[3][6:9],grid[4][6:9],grid[5][6:9]]
    g7=[grid[6][0:3],grid[7][0:3],grid[8][0:3]]
    g8=[grid[6][3:6],grid[7][3:6],grid[8][3:6]]
    g9=[grid[6][6:9],grid[7][6:9],grid[8][6:9]]

    print(x,y)
    def find_grid(x,y):
        global grd,ng
        if(x<4) and(y<4):
            grd=g1
            ng="one"
        elif((x<4 and y<7)and(y>3)):
            grd=g2 
            ng="two"
        elif((x<4)and (y>6)):
            grd=g3
            ng="three"
        elif((x<7 and y<4)and(x>3 and y>0)):
            grd=g4
            ng="four"
        elif((x<7 and y<7)and(x>3 and y>3)):
            grd=g5
            ng="five"
        elif((x<7)and (x>3 and y>6)):
            grd=g6
            ng="six"
        elif((x>6 and y<4)):
            grd=g7
            ng="seven"
        elif((x<10 and y<7)and(x>6 and y>3)):
            grd=g8 
            ng="eight"
        else:
            grd=g9
            ng="nine"
    
    find_grid(x,y)

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
    

    for row in range(0,3):
        if((grd[row][0]==grd[row][1]==grd[row][2])and(grd[row][0] is not None)):
                mini_winner=grd[row][0]               
                break
    for col in range(0,3):
        if((grd[0][col]==grd[1][col]==grd[2][col])and (grd[0][col] is not None)):
            mini_winner=grd[0][col]
            break
    if(grd[0][0]==grd[1][1]==grd[2][2]) and (grd[0][0] is not None):
        mini_winner=grd[0][0]
        
    if(grd[0][2]==grd[1][1]==grd[2][0]) and (grd[0][2] is not None):
        mini_winner=grd[0][2]
        
    if(all([all(row) for row in grd])and mini_winner is None):
        mini_draw=True

    status(0)
    find_grid(nx,ny)
    status(1)

def draw_large(x,y):
    ximage=pg.transform.scale(ximg,(180,180))
    sn.blit(ximage,(x,y))

def drawxo(row,col):
    global g,xo
    sn_width=600
    sn_height=600
    if row==1:
        x=10
    if row==2:
        x=sn_width/9
    if row==3:
        x=sn_width/9*2
    if row==4:
        x=sn_width/9*3
    if row==5:
        x=sn_width/9*4
    if row==6:
        x=sn_width/9*5
    if row==7:
        x=sn_width/9*6
    if row==8:
        x=sn_width/9*7
    if row==9:
        x=sn_width/9*8
    if col==1:
        y=5
    if col==2:
        y=sn_height/9
    if col==3:
        y=sn_height/9*2 
    if col==4:
        y=sn_height/9*3
    if col==5:
        y=sn_height/9*4 
    if col==6:
        y=sn_height/9*5
    if col==7:
        y=sn_height/9*6 
    if col==8:
        y=sn_height/9*7 
    if col==9:
        y=sn_height/9*8
    
    g[row-1][col-1]=xo
    if (xo=='x'):
        sn.blit(ximg,(y,x))
        xo='o'
    else:
        sn.blit(oimg,(y,x))
        xo='x'
    pg.display.update()

def click():
    x,y=pg.mouse.get_pos()

    if (x<sn_width/9):
        col=1
    elif(x<sn_width/9*2):
        col=2
    elif(x<sn_width/9*3):
        col=3
    elif(x<sn_width/9*4):
        col=4
    elif(x<sn_width/9*5):
        col=5
    elif(x<sn_width/9*6):
        col=6
    elif(x<sn_width/9*7):
        col=7
    elif(x<sn_width/9*8):
        col=8
    elif(x<sn_width):
        col=9
    else:
        col=None
    
    if(y<sn_height/9):
        row=1
    elif(y<sn_height/9*2):
        row=2
    elif(y<sn_height/9*3):
        row=3
    elif(y<sn_height/9*4):
        row=4
    elif(y<sn_height/9*5):
        row=5
    elif(y<sn_height/9*6):
        row=6
    elif(y<sn_height/9*7):
        row=7
    elif(y<sn_height/9*8):
        row=8
    elif(y<sn_height):
        row=9
    else:
        row=None
    
    if(row and col and g[row-1][col-1] is None):
        global xo 
        drawxo(row,col)
        mini_win(g,row,col)

def reset_game():
    global g,mini_winner,xo,mini_draw
    time.sleep(0)
    x='x'
    mini_draw=False
    game_opening()
    mini_winner=None
    g=[[None]*9 for i in range(9)]


game_opening()

state=True
while state:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            state=False
        elif event.type==MOUSEBUTTONDOWN:
            click()
            if(mini_winner or mini_draw):
               reset_game()


    pg.display.update()
    CLOCK.tick(30)


pg.quit()
quit()





















































