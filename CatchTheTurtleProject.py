import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT= ("Verdana", 15, "normal")

#score turtle
score_turtle = turtle.Turtle()

#turtle_list
turtle_list = []

score = 0

#countdown turtle
countdown_turtle = turtle.Turtle()

#gameover
gameover = False

#make_turtle properties
x_cordinates = [-20, -10, 0, 10, 20]
y_cordinates = [-10, 0, 10, 20]
grid_size = 10
def setup_score_turtle():
    score_turtle.hideturtle()       ##TURTLE'I SAKLAMAK(HİDE)

    score_turtle.color("dark blue")
    score_turtle.penup()
    #score_turtle.goto(0,230)  ##METNİ YUKARI TAŞIMAK#goto yerine setpos yazabilirdim.
    ##metni taşımak için ikinci yöntem
    toplam_yükseklik = screen.window_height() / 2
    y = toplam_yükseklik * 0.9
    score_turtle.setposition(0,y)
    ###YAZI YAZMAK
    score_turtle.write(arg="Score: 0", move=False, align="center",font=FONT)  #metni yazdım


def make_turtle(x, y):
    t = turtle.Turtle()    #yeni turtle oluşturdum
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

        #print(x, y)  kordinat almak için.şuan gerek yok bil diye yazdık

    t.onclick(handle_click)


    t.penup()
    t.shape("turtle")     #turtleın tipini değiştirdim
    t.shapesize(3, 3)     #boyutunu büyüttüm
    t.color("red")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)   #turtlerı bir dizide sakladım


def setup_turtles():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursice function:yani devamlı kendini çalıştıran fonksiyon.sonsuz çalışır.
def show_turtles_randomly():
    if not gameover:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

#recursive functinu durdurmak için bir if fonksiyonu gerkiyor.
def countdown(time):
    global gameover
    countdown_turtle.hideturtle()
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()
    toplam_yükseklik = screen.window_height() / 2
    y = toplam_yükseklik * 0.9
    countdown_turtle.setposition(0, y - 30)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 500)
    else:
        gameover = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)



def start_game_up():
    turtle.tracer(0)  # animasyonları sıfırlar
    setup_score_turtle()  # fonksiyonu çalıştır.
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)

start_game_up()
turtle.mainloop()










