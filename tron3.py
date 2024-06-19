from tkinter import *
import random
import os
import time

mainwin = Tk(className=" TRON")

mainwin.geometry("800x680")
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
    def __init__(self,x=100,y=100,dx=0,dy=0,alive=True,score=0, colour="white"):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.alive = alive
        self.score = score
        self.colour = colour
    def move(self):
        if self.alive:
           self.x = self.x + self.dx
           self.y = self.y + self.dy
           if grid[self.x][self.y] == 1:
               explosion(self.x,self.y)
               self.alive = False
           else:
               drawdot(self.x,self.y,self.colour)
    


player1 = Player(75,50,0,1,True,0,"#A0A0FF")
player2 = Player(160,50,0,1,True,0,"#FFA0A0")

playerai = Player(100,50,0,1,True,0)


AIalive = True
xai = 100  # AI x-location
yai = 50   # AI y-location
dxai = 0   # AI x speed
dyai = 1   # AI y speed

def printscores():
    printscr("Player 1 keyboard controls: w, a, s, d",10,24,player1.colour)
    printscr("Score: "+str(player1.score),160,49,player1.colour)
    printscr("Player 2 keyboard controls: i, j, k, l",420,24,player2.colour)
    printscr("Score: "+str(player2.score),560,49,player2.colour)

printscores()

def startagain():
    global x1,y1,dx1,dy1,x2,y2,dx2,dy2,xai,yai,dxai,dyai
    global player1alive, player2alive, AIalive
    global score1, score2
    if AIalive:
            printBIG("AI wins!!!",200,200,"yellow")
    if player1.alive:
        player1.score = player1.score + 1
        printBIG("Player 1 wins!!!",100,200,"yellow")
    if player2.alive:
        player2.score = player2.score + 1
        printBIG("Player 2 wins!!!",100,200,"yellow")
    canvastext.delete("all")
    printscores()
    canvastext.update()
    canvas1.update()
    time.sleep(2)
    player1.__init__(75,50,0,1,True,0,"#A0A0FF")
    player2.__init__(160,50,0,1,True,0,"#FFA0A0")
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
    if event.char == "w":
        player1.dx = 0
        player1.dy = -1
    if event.char == "d":
        player1.dx = 1
        player1.dy = 0
    if event.char == "a":
        player1.dx = -1
        player1.dy = 0
    if event.char == "s":
        player1.dx = 0
        player1.dy = 1
    if event.char == "i":
        player2.dx = 0
        player2.dy = -1
    if event.char == "l":
        player2.dx = 1
        player2.dy = 0
    if event.char == "j":
        player2.dx = -1
        player2.dy = 0
    if event.char == "k":
        player2.dx = 0
        player2.dy = 1

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
        if random.randint(1,100) > 10 : # turn to avoid wall
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
    player2.move()
    if AIalive:
      xai = xai + dxai
      yai = yai + dyai
    if grid[xai][yai] == 1:
       if AIalive:
            explosion(xai,yai)
       AIalive = False
    if AIalive:  
       drawdot(xai,yai,AIcolour)
    alivecount = sum([player1.alive, player2.alive, AIalive])
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
