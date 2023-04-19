import turtle

adi=turtle.Turtle()#variable can be any name

turtle.bgcolor("black")

adi.pencolor("red")

a=0
b=0
adi.speed(0)
adi.penup()
adi.goto(0,200)
adi.pendown()
while True:
    adi.forward(a)
    adi.right(b)
    a+=3
    b+=1

    if b ==200:
        break

    turtle.hideturtle()

#basic understanding of how to make squares and turtle movement back and forward.at angles

# adi.color('black','red')
# adi.begin_fill()
# adi.forward(100)
# adi.left(45)
# adi.forward(100)
# adi.right(90)
# adi.forward(100)
# adi.right(90)
# adi.forward(100)
# adi.right(90)
# adi.forward(100)
# adi.end_fill()
#











turtle.done()