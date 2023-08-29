from turtle import *
sizes = 400
orders = 5
speed(50)
penup()
goto(-200,-200)
pendown()

def sierpinski(size,order,count):
    if order == count:
        return
    if count%2 == 0:
        left(60)
        forward(size)
        sierpinski(size/2,order,count+1)
        forward(size)
        left(120)
        forward(size)
        sierpinski(size/2,order,count+1)
        forward(size)
        left(120)
        forward(size)
        sierpinski(size/2,order,count+1)
        forward(size)
        left(60)
    else:
        right(60)
        forward(size)
        sierpinski(size/2,order,count+1)
        forward(size)
        right(120)
        forward(size)
        sierpinski(size/2,order,count+1)
        forward(size)
        right(120)
        forward(size)
        sierpinski(size/2,order,count+1)
        forward(size)
        right(60)
    return

forward(sizes)
left(120)
forward(sizes)
left(120)
forward(sizes)
left(120)
forward(sizes/2)
sierpinski(sizes/4,orders,0)

Screen().mainloop()