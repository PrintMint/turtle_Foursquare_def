from turtle import *
def draw(posx,posy,defx,defy,defcolor):
    penup()
    goto(posx,posy)
    pendown()
    color(defcolor)
    fillcolor(defcolor)
    begin_fill()
    for i in range(2):
        fd(defx)
        lt(90)
        fd(defy)
        lt(90)
    end_fill()
