import turtle

t = turtle.Turtle()

def paral(colors = []):
    a= 145
    b = 55
    alpha = 60
    for item in colors:
        t.color(item)
        t.begin_fill()
        for i in range(2):
            t.forward(a)
            t.left(alpha)
            t.forward(b)
            t.left(180 - alpha)
        t.end_fill()
        t.forward(145)
        t.left(60)
        t.forward(55)
        t.left(60)

colors = ["blue", "yellow", "green"]
paral(colors)
input("")


'''
import turtle

t = turtle.Turtle()
t.speed(10)
colors = ["red", "violet", "blue", "green", "yellow", "orange"]

for i in range(6):
    t.left(90)
    t.down()
    t.pencolor(colors[i])
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(120,180)
    t.left(150)
    t.circle(-140,120)
    t.end_fill()

print("")'''