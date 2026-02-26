import turtle
import random
import math
# General Setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

screen = turtle.Screen()
screen.setup(1400, 700)
screen.bgcolor("skyblue")

# Screen Parameters
S_Width = 1400
S_LeftSide = -700

def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
# Layer Boundaries
Water_L = -350
Water_H = 130

Beach_L = -230
Beach_H = 250

Grass_L = 20
Grass_H = 220

Sky_L = 240
Sky_H = 280

# Water Layer
def draw_water():
    draw_rectangle(S_LeftSide, Water_L, S_Width, Water_H, "#1ca3ec")

    # waves

    t.color("#ffffff")
    for i in range(100):
        x = random.randint(-700, 700)
        y = random.randint(Water_L + 10, Water_L + Water_H - 20)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.circle(8, 60)
        t.setheading(0)



# Beach Layer
def draw_beach():
    draw_rectangle(S_LeftSide, Beach_L, S_Width, Beach_H, "#f0cb83")
    
    # Sand Texture
    t.color("#ece4d5")
    for i in range(600):
        t.pensize(3)
        x = random.randint(-680, 680)
        y = random.randint(Beach_L + 5, Beach_L + Beach_H - 5)
        t.penup()
        t.goto(x, y)
        t.dot(random.randint(1, 2))
    t.color("#bd9b5d")
    for i in range(500):
        t.pensize(3)
        x = random.randint(-680, 680)
        y = random.randint(Beach_L + 5, Beach_L + Beach_H - 5)
        t.penup()
        t.goto(x, y)
        t.dot(random.randint(1, 2))
        
    



    

    

    


# Grass Layer 
def draw_grass():
    draw_rectangle(S_LeftSide, Grass_L, S_Width, Grass_H, "#2ca540")

    # Grass Blade Texture
    t.color("#179737")
    for i in range(1500):
        x = random.randint(-700, 700)
        y = random.randint(Grass_L + 2, Grass_L + Grass_H - 2)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.left(90)
        t.forward(10)
        t.setheading(0)



def draw_house(x):

    depth = 28   
    y = 160

    # Front Wall
    t.penup()
    t.goto(x, -35 + y)  
    t.setheading(0)
    t.color("#d2b48c")
    t.begin_fill()
    for _ in range(2):
        t.forward(210)        
        t.left(90)
        t.forward(126)       
        t.left(90)
    t.end_fill()

    # Left Wall
    t.penup()
    t.goto(x, -35 + y)
    t.color("#c2a070")
    t.begin_fill()
    t.goto(x-depth, -35+depth + y)
    t.goto(x-depth, 91+depth + y)   # 130 → 91
    t.goto(x, 91 + y)
    t.goto(x, -35 + y)
    t.end_fill()

    # Front Roof
    t.penup()
    t.goto(x-14, 91 + y)
    t.color("#5c4033")
    t.begin_fill()
    t.goto(x+105, 161 + y)
    t.goto(x+224, 91 + y) 
    t.goto(x-14, 91 + y)
    t.end_fill()

    # Roof left side
    t.penup()
    t.color("#4a3228")
    t.begin_fill()
    t.goto(x - 14, 91 + y)
    t.goto(x + 105, 161 + y)
    t.goto(x + 105 - depth, 161 + depth + y)
    t.goto(x - 14 - depth, 91 + depth + y)
    t.goto(x - 14, 91 + y)
    t.end_fill()
    # Roof right side
    t.penup()
    t.color("#4a3228") 
    t.begin_fill()
    t.goto(x + 224, 91 + y)
    t.goto(x + 105, 161 + y)
    t.goto(x + 105 - depth, 161 + depth + y)
    t.goto(x + 224 - depth, 91 + depth + y)
    t.goto(x + 224, 91 + y)
    t.end_fill()
    # Door
    t.penup()
    t.goto(x + 91, -35 + y)
    t.color("#654321")
    t.begin_fill()
    for _ in range(2):
        t.forward(34)
        t.left(90)
        t.forward(63) 
        t.left(90)
    t.end_fill()

    # Windows
    def draw_window(wx, wy):
        t.penup()
        t.goto(wx, wy + y)
        t.color("white")
        t.begin_fill()
        for _ in range(4):
            t.forward(34)  
            t.left(90)
        t.end_fill()

    draw_window(x + 21, 14)
    draw_window(x + 154, 14)  


# Draw 3 Buildings
def draw_buildings():
    # Path
    for i in range(3):
        t.penup()
        t.goto(-700 + i * 215, 180)
        t.pendown()
        t.setheading(270)
        t.color("#534D46")
        t.begin_fill()
        for _ in range(2):
            t.forward(90)
            t.left(90)
            t.forward(1000)
            t.left(90)
        t.end_fill()
    # draw basic structure
    for i in range(3):
        t.penup()
        t.goto(-600 + i * 215, 120)
        t.setheading(0)
        t.fillcolor("#d2b48c")
        t.pendown()
        t.begin_fill()
        for _ in range(2):
            t.forward(200)
            t.left(90)
            t.forward(240)
            t.left(90)
        t.end_fill()

        t.setheading(0)
        t.begin_fill()
        t.fillcolor("#5c4033")
        t.right(215)
        t.forward(20)
        t.right(55)
        t.forward(240)
        t.right(135)
        t.forward(20)
        t.end_fill()
        t.begin_fill()
        t.backward(20)
        t.left(45)
        t.forward(203)
        t.right(45)
        t.forward(20)
        t.end_fill()
    # Windows
    for i in range(3):
        t.penup()
        t.goto(-580 + i * 215, 180)
        t.pendown()
        t.setheading(0)
        t.color("white")
        t.begin_fill()
        for _ in range(4):
            t.forward(40)
            t.left(90)
        t.end_fill()
        t.penup()
        t.goto(-580 + i * 215, 290)
        t.begin_fill()
        for _ in range(4):
            t.forward(40)
            t.left(90)
        t.end_fill()
        t.penup()
        t.goto((-530 + i * 215) + 60, 180)
        t.begin_fill()
        for _ in range(4):
            t.forward(40)
            t.left(90)
        t.end_fill()
        t.penup()
        t.goto((-530 + i * 215) + 60, 290)
        t.begin_fill()
        for _ in range(4):
            t.forward(40)
            t.left(90)
        t.end_fill()
    # doors
    for i in range(3):
        t.penup()
        t.goto(-525 + i * 215, 120)
        t.pendown()
        t.setheading(0)
        t.color("#654321")
        t.begin_fill()
        for _ in range(2):
            t.forward(43)
            t.left(90)
            t.forward(90)
            t.left(90)
        t.end_fill()
def draw_road():
    draw_rectangle(S_LeftSide, -70, S_Width, 160, "#808080")
    t.pensize(7)
    t.pencolor("white")
    for i in range(-700, 700, 40):
        t.penup()
        t.goto(i + 5, 10)
        t.pendown()
        t.forward(20)
    t.pensize(3)
    # sidewalks
    draw_rectangle(S_LeftSide, 90, S_Width, 20, "#696969")
    draw_rectangle(S_LeftSide, -100, S_Width, 30, "#696969")

# Beach Details
def draw_things():
    # SurfBoards
    for i in range(3):
        t.setheading(45)
        x = i * 230 - 600
        y = random.randint(Beach_L + 5, Beach_L + Beach_H - 130)
        t.penup()
        t.pencolor("red")
        t.goto(x, y)
        t.pendown()
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(90, 90)
        t.left(80)
        t.circle(90, 90)
        t.end_fill()

def draw_palmtree():

    def drawRectangle(t, width, height, color):
        t.fillcolor(color)
        t.begin_fill()
        for i in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()

    
   
    def drawTriangle(t, length, color):
        t.fillcolor(color)
        t.begin_fill()
        t.forward(length)
        t.left(135)
        t.forward(length / math.sqrt(2))
        t.left(90)
        t.forward(length / math.sqrt(2))
        t.left(135)
        t.end_fill()

    




   

    for i in range(10):
        x = random.randint(-680, 680)
        y = random.randint(Grass_L + 110, Grass_L + Grass_H)
        # Tree base
        t.setheading(0)
        t.color("brown")
        t.penup()
        t.goto(x, y)
        t.pendown()
        drawRectangle(t, 20, 40, "brown")


# Tree top
        t.setheading(0)
        t.color("lightgreen")
        for i in range(3):
            t.penup()
            t.goto((x - 42) + i * 7, y + 40 + i * 30)
            t.pendown()
            drawTriangle(t, 100 - i * 10, "lightgreen")
             








# Draw Scene

draw_water()
draw_beach()
draw_grass()
draw_palmtree()
draw_buildings()
draw_road()
draw_house(70)
draw_house(320)
draw_things()
turtle.exitonclick()

