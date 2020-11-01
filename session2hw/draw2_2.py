from turtle import *
speed(-1)
for edge in range (3,7):
    for i in range(edge):
        if edge % 2==0:
            color("red")
            forward(100)
            left(360/edge)
        else:
            color("blue")
            forward(100)
            left(360/edge)
mainloop()