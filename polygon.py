import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("darkblue")
drawing_board.title("Python Turtle")


turtle_instance = turtle.Turtle()
num_sides = 6              #kaç kenarlı
angle = 360.0 / num_sides   #açı. kaç derecede bir değiştiricez
side_length = 100    #ne kadar ilerlesin
for i in range(num_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)


turtle.done()