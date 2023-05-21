import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("darkblue")  #arka plan rengi darkblue yerine #collor hex code yazabiliriz.
drawing_board.title("Python Turtle") #ekranda ne yazsın


turtle_instance = turtle.Turtle()
turtle_instance.forward(200)      #200 piksel ileri git
#tutle intance daha fazla olabilir.turtle instance dediğimiz çizimi yapan kaplumbağa
turtle_instance_2 = turtle.Turtle() #2.ci turtle oluşturdum
turtle_instance_2.left(45)   # bu turtle 45 derece sola döndükten sonra
turtle_instance_2.forward(200) #200 piksel gidecek


turtle.done()              #bitirdim

