import random
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

T = turtle.Turtle()
T.penup()
a = [100, 200]
b = [100, 200]
def rasgele_yer_değiştir():
    x = random.choice(a)
    y = random.choice(b)

    T.goto(x, y)

def tıklama(x, y):
    rasgele_yer_değiştir()

turtle.onscreenclick(tıklama)


turtle.mainloop()