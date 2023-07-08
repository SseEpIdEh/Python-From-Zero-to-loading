import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    color=(r,g,b)
    return color
tim.speed("fastest")

def draw_spirogragh(size_of_gap):
     for _ in range(int(360 /size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        print(tim.heading())  # the answer is zero, so we need to change it,shift it!
        tim.setheading(tim.heading() + size_of_gap)

draw_spirogragh(5)
screen =t.Screen()
screen.exitonclick()
