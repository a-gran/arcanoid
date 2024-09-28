from turtle import *
def light(s_col, x, y, fill):
    color(s_col)
    penup()
    goto(x, y)
    pendown()
    if fill == 'on':
        begin_fill()
        circle(35)
        end_fill()
    elif fill == 'off':
        circle(35)

answer = input('Какой горит цвет: красный/желтый/зеленый?')
if answer == 'красный':
    light('red', 0, 100, 'on')
    light('yellow', 0, 0, 'off')
    light('green', 0, -100, 'off')
if answer == 'желтый':
    light('red', 0, 100, 'off')
    light('yellow', 0, 0, 'on')
    light('green', 0, -100, 'off')
if answer == 'зеленый':
    light('red', 0, 100, 'off')
    light('yellow', 0, 0, 'off')
    light('green', 0, -100, 'on')

hideturtle()
exitonclick()
