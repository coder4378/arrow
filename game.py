#my first game   from python
#favouravle for biggeners
#using
#Turtle graphics game
import turtle
import math
import random
#set up screen
screen = turtle.Screen()
screen.bgcolor("light green")


#draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300 , -300)
mypen.pendown()
mypen.pensize(5)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
    mypen.hideturtle()



#create player
player = turtle.Turtle()
player.color("black")
player.shape("triangle")
player.penup()
player.speed(0)



                       

#set speed
speed = 1

def turnleft():
    player.left(30)


def turnright():
    player.right(30)

def dash():
    global speed
    speed += 1



#set keyboard bindings
turtle.listen()
turtle.onkey(turnleft , "Left")
turtle.onkey(turnright , "Right")
turtle.onkey(dash , "space")



while True:
    player.forward(speed)

    #boundry collison
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)


    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
    


