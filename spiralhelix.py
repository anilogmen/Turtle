import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("black")
drawing_board.title("Python Turtle")


turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle_colors = ["red", "purple", "blue", "orange"]
turtle.speed(0)




for i in range(10):
    turtle_instance.color(turtle_colors[i % 4])

    turtle_instance.circle(10 * i)                #yarıçap
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)


turtle.done()