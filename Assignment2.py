import turtle
import time
import random

window = turtle.Screen()

alex = turtle.Turtle()
john = turtle.Turtle()

#Mainmenu

def Mainmenu():
    window.resetscreen()
    alex.speed(0)
    alex.hideturtle()
    john.speed(0)
    john.hideturtle()

    john.penup()
    alex.penup()
    john.setposition(-280, 250)
    alex.setposition(-280, 200)
    alex.pendown()
    john.pendown()
    john.write("\U0001F4DE", font=('Arial', 60))
    alex.write("Call App\nType 'P' to open", font=('Arial', 10, 'bold'))


    john.penup()
    alex.penup()
    john.setposition(-80, 250)
    alex.setposition(-80, 200)
    alex.pendown()
    john.pendown()
    john.write("\U0001F506", font=('Arial', 60))
    alex.write("Weather App\nType 'W' to open", font=('Arial', 10, 'bold'))

    john.penup()
    alex.penup()
    john.setposition(-280, 100)
    alex.setposition(-280, 60)
    alex.pendown()
    john.pendown()
    john.write("\U0001F4D2", font=('Arial' , 60))
    alex.write("Contacts App\nType 'C' to open", font=('Arial', 10, 'bold'))

    alex.penup()
    john.penup()
    alex.setposition(80, 200)
    john.setposition(100,250)
    alex.pendown()
    john.pendown()
    john.write("\U0001F4C5", font=('Arial', 60))
    alex.write("UFV Class Schesule App\nType 'U' to open", font=('Arial', 10, 'bold'))

    john.penup()
    alex.penup()
    alex.setposition(-80, 60)
    john.setposition(-80,100)
    alex.pendown()
    john.pendown()
    john.write("\U0001F68F", font=('Arial', 60))
    alex.write("Bus Schedule App\nType 'B' to open", font=('Arial', 10, 'bold'))

    john.penup()
    alex.penup()
    alex.setposition(80, 60)
    john.setposition(100, 100)
    alex.pendown()
    john.pendown()
    john.write("\U0001F500", font=('Arial', 60))
    alex.write("Word Randomizer App\nType 'R' to open", font=('Arial', 10, 'bold'))

    john.penup()
    alex.penup()
    alex.setposition(-280, -100)
    john.setposition(-280,-60)
    alex.pendown()
    john.pendown()
    john.write("\U0001F527", font=('Arial', 60))
    alex.write("Settings App\nType 'S' to open", font=('Arial', 10, 'bold'))

    john.penup()
    alex.penup()
    john.setposition(-70,-60)
    alex.setposition(-80,-110)
    alex.pendown()
    john.pendown()
    john.write("\U0001FAB7", font=('Arial', 60))
    alex.write("Geometric Pattern\nGenerator\nType 'G' to open", font=('Arial', 10, 'bold'))

    john.penup()
    alex.penup()
    john.setposition(100,-60)
    alex.setposition(100,-100)
    alex.pendown()
    john.pendown()
    john.write("\U0001F4DD", font=('Arial', 60))
    alex.write("Drawing App\nType 'D' to open", font=('Arial', 10, 'bold'))


    alex.penup()
    alex.setposition(-150, -300)
    alex.pendown()
    alex.write("Press 'right arow' key to go to the next page", font=('Arial', 10, 'bold'))

#NEXT PAGE

def next_page():
    window.resetscreen()
    alex.speed(0)
    alex.hideturtle()
    john.speed(0)
    john.hideturtle()
    
    john.penup()
    alex.penup()
    john.setposition(-300, 230)
    alex.setposition(-320, 200)
    alex.pendown()
    john.pendown()
    john.write("\U0001F577", font=('Arial', 60))
    alex.write("Spirograph Simulator\nType 'A' to open", font=('Arial', 10, 'bold'))

    alex.penup()
    alex.setposition(-150, -300)
    alex.pendown()
    alex.write("Press 'left arow' key to go to the previous page", font=('Arial', 10, 'bold'))

#Call App

def call_app():
    window.resetscreen()
    phone_call = window.textinput("Phone Call", "Please enter the 7-digit phone number:")
    alex.speed(0)
    alex.hideturtle()
    alex.penup()
    alex.setposition(-200,50)
    alex.pendown()
    
    if phone_call == "E":
        alex.write("END CALL", font=("Arial", 24, "normal"))
        time.sleep(2)
        window.bye()

    elif phone_call.isdigit() and len(phone_call) == 7:
        alex.write("CALLING..."+ phone_call, font=("Arial", 24, "normal"))
    
    else:
        alex.write("INVALID NUMBER", font=("Arial", 24, "normal"))

#Weather app

def Weather_app():
    window.resetscreen()
    file_reference = open("Weather_info.txt", "r")
    content_of_file = file_reference.read()
    file_reference.close()
    alex.speed(0)
    alex.hideturtle()
    alex.penup()
    alex.setposition(-200,50)
    alex.pendown()
    alex.write(content_of_file, font=("Arial", 24, "normal"))

#Contacts App


def Contacts_app():
    window.resetscreen()
    file_reference = open("Contacts_info.txt", "r")
    content_of_file = file_reference.read()
    file_reference.close()
    alex.speed(0)
    alex.hideturtle()
    alex.penup()
    alex.setposition(-200,50)
    alex.pendown()
    alex.write(content_of_file, font=("Arial", 24, "normal"))

    file_reference = open("Contacts_info.txt", "a")
    message = window.textinput("Save New Contacts","Please enter the name and the phone number:")
    file_reference.write("\n" + message)
    file_reference.close()

#UFV Schedule App

def UFV_Schedule_app():
    window.resetscreen()
    file_reference = open("UFV_Schedule.txt", "r")
    content_of_file = file_reference.read()
    file_reference.close()
    alex.speed(0)
    alex.hideturtle()
    alex.penup()
    alex.setposition(-200,50)
    alex.pendown()
    alex.write(content_of_file, font=("Arial", 24, "normal"))

#Bus schedule App

def Bus_schedule_app():
    window.resetscreen()
    file_reference = open("bus_schedule.txt", "r")
    content_of_file = file_reference.read()
    file_reference.close()
    alex.speed(0)
    alex.hideturtle()
    alex.penup()
    alex.setposition(-200,50)
    alex.pendown()
    alex.write(content_of_file, font=("Arial", 24, "normal"))

#Word Randomizer App

def Word_randomizer_app():
    window.resetscreen()
    file_reference = open("random_words.txt", "r")
    content_of_file = file_reference.read()
    file_reference.close()
    words = content_of_file.splitlines()
    random_word = random.choice(words)
    alex.speed(0)
    alex.hideturtle()
    alex.penup()
    alex.setposition(-200,50)
    alex.pendown()
    alex.write(random_word, font=("Arial", 24, "normal"))

#Settings App

def Settings_app():
    window.resetscreen()
    background = window.textinput("Settings", "Please enter the background colour:")
    window.bgcolor(background)
    Mainmenu()


#Geometric pattern app

def Geometric_pattern_app():
    window.resetscreen()
    window.bgcolor("Black")
    alex.speed(0)

    sides = window.textinput("Geometric Pattern", "Please enter the number of sides")
    new_sides = int(sides)

    size = window.textinput("Geometric Pattern", "Please enter the size")
    new_size = int(size)
   
    def draw_pattern(alex, sides, size):
        # Choose a random color
        r = random.random()
        g = random.random()
        b = random.random()
        alex.pencolor(r, g, b)
        
        for _ in range(new_sides):
            alex.forward(new_size)
            alex.right(360/new_sides)


    for size in range(new_size):
        draw_pattern(alex, sides, size)
        alex.right(5)
        
#Drawing app

def Drawing_app():
    window.resetscreen()
    window.bgcolor("white")

    alex.penup()
    alex.goto(-300, -300)
    alex.pendown()
    alex.speed(0)
    alex.hideturtle()
    alex.write("'E' for forward\n'T' for backward\n'F' for turn left\n'V' for right", font=('Arial', 15, 'bold') )
    
    def move_forward():
        john.forward(100)

    def move_backward():
        john.backward(100)

    def turn_left():
        john.left(90)

    def turn_right():
        john.right(90)

    window.onkey(move_forward, "E")
    window.onkey(move_backward, "T")
    window.onkey(turn_left, "F")
    window.onkey(turn_right, "V")

#Spirograph Simulator

def Spirograph_Simulator():
    window.resetscreen()
    window.bgcolor("black")
    alex.speed(0)
    alex.hideturtle()
    alex.pencolor("white")

    radius = window.textinput("Spirograph Simulator", "Please enter the radius")
    new_radius = int(radius)

    loops = window.textinput("Spirograph Simulator", "Please enter the number of loops")
    new_loops = int(loops)

    def draw_spirograph(alex,radius,loops):
        for _ in range(loops):
            alex.circle(radius)
            alex.right(360/loops)
    
    draw_spirograph(alex, new_radius, new_loops)


window.onkeypress(Mainmenu, "Left")
window.onkeypress(call_app, "P")
window.onkeypress(Weather_app, "W")
window.onkeypress(Contacts_app, "C")
window.onkeypress(UFV_Schedule_app, "U")
window.onkeypress(Bus_schedule_app, "B")
window.onkeypress(Word_randomizer_app, "R")
window.onkeypress(Settings_app, "S")
window.onkeypress(Geometric_pattern_app, "G")
window.onkeypress(Drawing_app, "D")
window.onkeypress(next_page, "Right")
window.onkeypress(Spirograph_Simulator, "A")
window.listen()

Mainmenu()
window.mainloop()