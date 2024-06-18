from tkinter import *
import random
import os
import time

mainwin = Tk(className=" TRON")

mainwin.geometry("800x680")
player1colour = "#A0A0FF"
player2colour = "#FFA0A0"
AIcolour = "#0000FF"

# playground
canvas1= Canvas(mainwin,width=800,height=600, bg = "black")
canvas1.place(x=0,y=0)

# status text box frame
canvas2= Canvas(mainwin,width=798,height=78, bg = "grey")
canvas2.place(x=0,y=600)

# Print text (labels) on screen
canvastext= Canvas(mainwin,width=784,height=64, bg = "black")
canvastext.place(x=6,y=607)
font1 = ("Arial",16,"bold")
fontBIG = ("Arial",64,"bold") 
def printscr(mytext,x,y,mycolour):
    canvastext.create_text(x,y,text=mytext, fill=mycolour,font=font1, anchor="sw") 

def printBIG(mytext,x,y,mycolour):
    canvas1.create_text(x,y,text=mytext, fill=mycolour,font=fontBIG, anchor="sw") 


class Player:
    def __init__(self,x=100,y=100,dx=0,dy=0,alive=True,score=0):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.alive = alive
        self.score = score
    def move(self):
        if self.alive:
           self.x = self.x + self.dx
           self.y = self.y + self.dy
           drawdot(self.x,self.y,"red")
           if grid[self.x][self.y] == 1:
            explosion(self.x,self.y)
            self.alive = False
    


player1 = Player(75,50,0,1,True,0)
player2 = Player(150,50,0,1,True,0)

playerai = Player(100,50,0,1,True,0)

player1alive = True
x1 = 50 # player 1 x-location
y1 = 50 # player 1 y-location 
dx1 = 0 # player 1 x-speed
dy1 = 1 # player 1 y-speed
score1 = 0 # player 1 score

player2alive = True
x2 = 150 # player 2 x-location
y2 = 50  # player 2 y-location
dx2 = 0  # player 2 x-speed
dy2 = 1  # player 2 y-speed
score2 = 0 # player 2 score

AIalive = True
xai = 100  # AI x-location
yai = 50   # AI y-location
dxai = 0   # AI x speed
dyai = 1   # AI y speed

def printscores():
    printscr("Player 1 keyboard controls: w, a, s, d",10,24,player1colour)
    printscr("Score: "+str(score1),160,49,player1colour)
    printscr("Player 2 keyboard controls: i, j, k, l",420,24,player2colour)
    printscr("Score: "+str(score2),560,49,player2colour)

printscores()

def startagain():
    global x1,y1,dx1,dy1,x2,y2,dx2,dy2,xai,yai,dxai,dyai
    global player1alive, player2alive, AIalive
    global score1, score2
    if AIalive:
            printBIG("AI wins!!!",200,200,"yellow")
    if player1alive:
        score1 = score1 + 1
        printBIG("Player 1 wins!!!",100,200,"yellow")
    if player2alive:
        score2 = score2 + 1
        printBIG("Player 2 wins!!!",100,200,"yellow")
    canvastext.delete("all")
    printscores()
    canvastext.update()
    canvas1.update()
    time.sleep(2)
    player1alive = True
    x1 = 50 
    y1 = 50 
    dx1 = 0 
    dy1 = 1
    player2alive = True
    x2 = 150 # player 2 x-location
    y2 = 50  # player 2 y-location
    dx2 = 0  # player 2 x-speed
    dy2 = 1  # player 2 y-speed
    AIalive = True
    xai = 100  # AI x-location
    yai = 50   # AI y-location
    dxai = 0   # AI x speed
    dyai = 1   # AI y speed
    canvas1.delete("all")
    cleargrid()
    drawwalls()

grid = []  # playfield, 500 by 500
for i in range(500):
    L=[]
    for j in range(500):
        L.append(0)
    grid.append(L)

def cleargrid():
    global grid
    for i in range(500):
      for j in range(500):
          grid[i][j] = 0


def mykey(event):
    global dx1, dy1, dx2, dy2
    if event.char == "w":
        dy1 = -1
        dx1 = 0
    if event.char == "d":
        dy1 = 0
        dx1 = 1
    if event.char == "a":
        dy1 = 0
        dx1 = -1
    if event.char == "s":
        dy1 = 1
        dx1 = 0
    if event.char == "i":
        dy2 = -1
        dx2 = 0
    if event.char == "l":
        dy2 = 0
        dx2 = 1
    if event.char == "j":
        dy2 = 0
        dx2 = -1
    if event.char == "k":
        dy2 = 1
        dx2 = 0

def explosion(x,y):
    drawdot(x,y, "black")
    for i in range(100):
        ex = random.randint(-4,4)
        ey = random.randint(-4,4)
        drawdot(x+ex,y+ey, "black")
    for i in range(3):
        ex = random.randint(-3,3)
        ey = random.randint(-3,3)
        drawdot(x+ex,y+ey, "white")
    canvas1.update()

def goclearAI():
    global dxai, dyai, AIalive
    dxai = 0
    dyai = 0
    godirections = []
    if grid[xai+1][yai] == 0:
        godirections.append("right")
    if grid[xai-1][yai] == 0:
        godirections.append("left")
    if grid[xai][yai+1] == 0:
        godirections.append("down")
    if grid[xai][yai-1] == 0:
        godirections.append("up")
    if godirections == []:
       if AIalive:
            explosion(xai,yai)
       AIalive = False
    else:
      go = random.choice(godirections)
      if go == "right": dxai = 1
      elif go == "left": dxai = -1
      elif go == "up": dyai = -1
      elif go == "down": dyai = 1
    

def controlAI():
    if grid[xai+dxai][yai+dyai] == 1:
        if random.randint(1,100) > 40 : # turn to avoid wall
           goclearAI()
    elif random.randint(1,100) > 92: # make a random turn
        goclearAI()
        


def drawdot(x,y,colour):
    global grid
    if colour == "black":
      grid[x][y] = 0
    else:
      grid[x][y] = 1
    canvas1.create_line(x*4,y*4,x*4+4,y*4,width=4,fill=colour)


def drawline(x,y,dx,dy,n,colour):
    for i in range(n):
        drawdot(x+dx*i,y+dy*i,colour)
    

mainwin.bind("<Key>", mykey)

def timerupdate():
    global x1,x2,y1,y2,xai,yai, player1alive, player2alive, AIalive
    controlAI()
    player1.move()
    if player1alive:
      x1 = x1 + dx1
      y1 = y1 + dy1
    if player2alive:
      x2 = x2 + dx2
      y2 = y2 + dy2
    if AIalive:
      xai = xai + dxai
      yai = yai + dyai
    if grid[x1][y1] == 1:
       if player1alive:
            explosion(x1,y1) 
       player1alive = False  
    if grid[x2][y2] == 1:
       if player2alive:
            explosion(x2,y2) 
       player2alive = False
    if grid[xai][yai] == 1:
       if AIalive:
            explosion(xai,yai)
       AIalive = False
    if player1alive:
       drawdot(x1,y1,player1colour)
    if player2alive: 
       drawdot(x2,y2,player2colour)
    if AIalive:  
       drawdot(xai,yai,AIcolour)
    alivecount = sum([player1alive, player2alive, AIalive])
    if alivecount <= 1:
        startagain()
    mainwin.after(100,timerupdate)


def drawwalls():
   drawline(0,1,1,0,200,"grey")
   drawline(199,1,0,1,150,"grey")
   drawline(199,150,-1,0,200,"grey")
   drawline(0,150,0,-1,150,"grey")

drawwalls()
    
mainwin.after(100,timerupdate)
mainwin.mainloop()
