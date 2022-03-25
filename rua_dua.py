from turtle import Turtle,Screen
import random
import datetime
screen = Screen()



all_turtle = []
chon_rua = input("Vui lòng chọn rùa ").lower()
color = ["black","pink","red","yellow","green",]
y_position = [-60,-30,0,30,60]

for i in range(5):
    turtle = Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.color(color[i])
    turtle.shape("turtle")
    turtle.goto(-100,y_position[i])
    all_turtle.append(turtle)
def dichuyen(all_turtle):
    x = datetime.datetime.now()
    global end
    di_chuyen = random.choice(all_turtle)
    di_chuyen.fd(10)
    if di_chuyen.xcor() > 200:
        print("Rùa",di_chuyen.pencolor(),"là Rùa dành chiến thắng")
        y = datetime.datetime.now()
        if chon_rua ==di_chuyen.pencolor():
            print("Bạn đoán đúng")
            time = y-x
            print(time)
        else:
            print("Bạn đoán sai")
            time = y - x
            print(time)
        end=False

end = True
while end:
    turtle.speed(1)
    dichuyen(all_turtle)

screen.exitonclick()