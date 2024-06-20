from tkinter import *
import random
import os
import time

mainwin = Tk(className=" TRON")

mainwin.geometry("800x680")

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
    
class AIPlayer(Player):
    def findclear(self):
        self.dx = 0
        self.dy = 0
        godirections = []
        if grid[self.x+1][self.y] == 0:
           godirections.append("right")
        if grid[self.x-1][self.y] == 0:
           godirections.append("left")
        if grid[self.x][self.y+1] == 0:
           godirections.append("down")
        if grid[self.x][self.y-1] == 0:
           godirections.append("up")
        if godirections == []:
           if self.alive:
             explosion(self.x,self.y)
             self.alive = False
        else:
          go = random.choice(godirections)
          if go == "right": self.dx = 1
          elif go == "left": self.dx = -1
          elif go == "up":  self.dy = -1
          elif go == "down": self.dy = 1
    def findmove(self):
        if grid[self.x+self.dx][self.y+self.dy] == 1:
           if random.randint(1,100) > 10 : # turn to avoid wall
              self.findclear()
        elif random.randint(1,100) > 92: # make a random turn
           self.findclear()
        
    

player1 = Player(75,50,0,1,True,0,"#A0A0FF")
player2 = Player(160,50,0,1,True,0,"#FFA0A0")

aistartlist=[(10,10),(40,40),(80,80),(100,100),(120,120),(140,140),\
             (160,140),(180,140),(180,100),(180,80),(180,40),(180,20),\
             (160,40),(120,40),(80,40),(40,40),(40,80),(40,120),\
             (20,120),(40,20),(80,20),(100,20)]

ailist = []
for i in range(len(aistartlist)):
    ailist.append(AIPlayer(aistartlist[i][0],aistartlist[i][1],0,1,True,0,"#999999"))

def printscores():
    printscr("Player 1 keyboard controls: w, a, s, d",10,24,player1.colour)
    printscr("Score: "+str(player1.score),160,49,player1.colour)
    printscr("Player 2 keyboard controls: i, j, k, l",420,24,player2.colour)
    printscr("Score: "+str(player2.score),560,49,player2.colour)

printscores()

def startagain():
    if player1.alive:
        player1.score = player1.score + 1
        printBIG("Player 1 wins!!!",100,200,"yellow")
    elif player2.alive:
        player2.score = player2.score + 1
        printBIG("Player 2 wins!!!",100,200,"yellow")
    else:
        printBIG("AI wins!!!",200,200,"yellow")
    canvastext.delete("all")
    printscores()
    canvastext.update()
    canvas1.update()
    time.sleep(2)
    player1.__init__(75,50,0,1,True,player1.score,"#A0A0FF")
    player2.__init__(160,50,0,1,True,player2.score,"#FFA0A0")
    ailist.clear()
    for i in range(10):
      ailist.append(AIPlayer(100+i*10,30,0,1,True,0,"#999999"))
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
    player1.move()
    player2.move()
    for ai in ailist:
      ai.findmove()
      ai.move()
    alivelist = [player1.alive, player2.alive]
    for ai in ailist:
        alivelist.append(ai.alive)
    alivecount = sum(alivelist)
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
