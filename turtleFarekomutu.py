import random
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

T = turtle.Turtle()
T.penup()

def bas(x, y):
    T.goto(x, y)

turtle.onscreenclick(bas)



turtle.mainloop()         #bitmesin diye mainloop çağırdık