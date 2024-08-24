import turtle
turtle.setup(width=520,height=580)
turtle.bgcolor("WHITE")
def draw_board():
    x=-240
    y=270
    for i in range(10):
        turtle.penup()
        turtle.goto(x, y-i*60)
        turtle.pendown()
        turtle.goto(x+480, y-i*60)
    for i in range(9):
        turtle.penup()
        turtle.goto(x+i*60,y)
        turtle.pendown()
        turtle.goto(x+i*60,y-240)
    for i in range(9):
        turtle.penup()
        turtle.goto(x+i*60,y-300)
        turtle.pendown()
        turtle.goto(x+i*60,y-300-240)
    for i in [0,8]:
        turtle.penup()
        turtle.goto(x+i*60,y-240)
        turtle.pendown()
        turtle.goto(x+i*60,y-300)
    for i in [3,5]:
        for j in [5,3]:
            turtle.penup()
            turtle.goto(x+i*60,y)
            turtle.pendown()
            turtle.goto(x+j*60,y-2*60)
    x=-240
    y=-270
    for i in [3,5]:
        for j in [5,3]:
            turtle.penup()
            turtle.goto(x+i*60,y)
            turtle.pendown()
            turtle.goto(x+j*60,y+2*60)
    turtle.penup()
    turtle.goto(-160,-15)
    turtle.pendown()
    turtle.write("楚   河                汉   界", align="left", font=("Arial", 24, "normal"))
    # 隐藏海龟图标
    turtle.hideturtle()
draw_board()
turtle.done()