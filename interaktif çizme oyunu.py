import random
import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

colors = ["red", "blue", "green", "yellow", "black"]

def turtle_forward():
    turtle_instance.color(random.choice(colors))

    turtle_instance.forward(100)

def rotata_angle_right():
    turtle_instance.right(90)

def rotata_angle_left():
    turtle_instance.left(90)

def clear():
    turtle_instance.clear()      #silme fonksiyonu

def evedön():
    turtle_instance.penup()    #kalemi kaldır
    turtle_instance.home()      #eve dön
    turtle_instance.pendown()    #kalemi indir

def kalemiKaldir():                 #kalemi kaldırdı.çizmeyi bıraktı
    turtle_instance.penup()

def kalemiİndir():                   #kalemi kaldırdı.çizmeye başladı
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotata_angle_right, key="Down")
drawing_board.onkey(fun=rotata_angle_left, key="Up")
drawing_board.onkey(fun=clear, key="c")
drawing_board.onkey(fun=evedön, key="h")
drawing_board.onkey(fun=kalemiKaldir, key="w")
drawing_board.onkey(fun=kalemiİndir, key="e")

turtle.mainloop()