from tkinter import *

mainwin = Tk(className=" TRON")

mainwin.geometry("800x680")
player1colour = "#A0A0FF"
player2colour = "#FFA0A0"

# playground
canvas1= Canvas(mainwin,width=800,height=600, bg = "black")
canvas1.place(x=0,y=0)

# status text box
canvas2= Canvas(mainwin,width=798,height=78, bg = "grey")
canvas2.place(x=0,y=600)

# Print text (labels) on screen
canvastext= Canvas(mainwin,width=784,height=64, bg = "black")
canvastext.place(x=6,y=607)
font1 = ("Arial",16,"bold")
def printscr(mytext,x,y,mycolour):
    canvastext.create_text(x,y,text=mytext, fill=mycolour,font=font1, anchor="sw") 


printscr("Player 1 keyboard controls: w, a, s, d",10,24,player1colour)
printscr("Score: 0",160,49,player1colour)
printscr("Player 2 keyboard controls: i, j, k, l",420,24,player2colour)
printscr("Score: 0",560,49,player2colour)



player1alive = True
x1 = 50 # player 1 x-location
y1 = 50 # player 1 y-location 
dx1 = 0 # x1 speed
dy1 = 1 # y1 speed

player2alive = True
x2 = 150 # player 2 x-location
y2 = 50 # player 2 y-location
dx2 = 0 # x2 speed
dy2 = 1 # y2 speed



grid = []  # playfield, 500 by 500
for i in range(500):
    L=[]
    for j in range(500):
        L.append(0)
    grid.append(L)


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


def drawdot(x,y,colour):
    global grid
    grid[x][y] = 1
    canvas1.create_line(x*4,y*4,x*4+4,y*4,width=4,fill=colour)


def drawline(x,y,dx,dy,n,colour):
    for i in range(n):
        drawdot(x+dx*i,y+dy*i,colour)
    

mainwin.bind("<Key>", mykey)

def timerupdate():
    global x1,x2,y1,y2, player1alive, player2alive
    if player1alive:
      x1 = x1 + dx1
      y1 = y1 + dy1
    if player2alive:
      x2 = x2 + dx2
      y2 = y2 + dy2
    if grid[x1][y1] == 1:
       player1alive = False
    if grid[x2][y2] == 1:
       player2alive = False
    drawdot(x1,y1,player1colour)
    drawdot(x2,y2,player2colour)
    mainwin.after(100,timerupdate)


# drawwalls
drawline(0,1,1,0,200,"grey")
drawline(199,1,0,1,150,"grey")
drawline(199,150,-1,0,200,"grey")
drawline(0,150,0,-1,150,"grey")


mainwin.after(100,timerupdate)
mainwin.mainloop()
