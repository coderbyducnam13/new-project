import turtle
window = turtle.Screen()
turtle = turtle.Turtle()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.speed("fastest")
turtle.pensize(5)
color = ["#55ff00","#ff00ff","#00aaff","#ff8000","#ffff00"]
seth = 0
index = 0
while True:
    turtle.seth(seth)
    seth-=10
    turtle.color(color[index])
    if index==4:
        index=0
    else:
        index+=1
    for i in range(2):
        turtle.circle(100, 90)
        turtle.circle(100 // 2, 90)

window.exitonclick()