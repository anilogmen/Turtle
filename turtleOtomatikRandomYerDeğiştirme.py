import random
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

T = turtle.Turtle()
T.speed(1)
T.shape("turtle")


a = [-100, 200]
b = [-100, 200]
def otomatik_yer_degistir():
    x = random.choice(a)
    y = random.choice(b)

    T.penup()
    T.goto(x, y)
    T.pendown()
while True:
    otomatik_yer_degistir()

turtle.mainloop()