import turtle
import time
import math
from datetime import datetime
from Watch import Watch

class Digit:
    def __init__(self, value, position, size=20, color="black"):
        self.value = value
        self.position = position
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color(color)

    def draw(self):
        # малює цифру на циферблаті
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(self.position)
        self.pen.write(str(self.value), align="center", font=("Arial", 20, "bold"))

    def update_color(self, color):
        self.pen.color(color)

    def erase(self):
        self.pen.clear()

class DigitFace:
    def __init__(self, radius=200, color="black"):
        self.digits = []
        # цифри по колу
        for i in range(1, 13):
            angle = math.radians(90 - i * 30)  # 12 година вгорі
            x = radius * 0.85 * math.cos(angle)
            y = radius * 0.85 * math.sin(angle)
            self.digits.append(Digit(i, (x, y), color=color))

    def draw(self):
        for digit in self.digits:
            digit.draw()

    def update_color(self, color):
        for digit in self.digits:
            digit.update_color(color)

    def erase(self):
        for digit in self.digits:
            digit.erase()


class Hand:
    def __init__(self, length, width, color):
        self.length = length
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.pensize(width)
        self.pen.color(color)

    def draw(self, angle):
        # малюєм стрілку з заданим кутом
        self.pen.clear()
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.setheading(90 - angle)  # 90 - це 12 година
        self.pen.pendown()
        self.pen.forward(self.length)

    def update_color(self, color):
        self.pen.color(color)

    def erase(self):
        self.pen.clear()


class Button:
    def __init__(self, position, width, height, text, color="purple", text_color="black"):
        self.position = position
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color

        # обчислює границі кнопки для перевірки кліків
        self.x_min = position[0] - width / 2
        self.x_max = position[0] + width / 2
        self.y_min = position[1] - height / 2
        self.y_max = position[1] + height / 2


        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.penup()

    def draw(self):
        # кнопачку ам-ам
        self.pen.clear()
        self.pen.penup()

        # її фон
        self.pen.goto(self.x_min, self.y_min)
        self.pen.color("black", self.color)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(2):
            self.pen.forward(self.width)
            self.pen.left(90)
            self.pen.forward(self.height)
            self.pen.left(90)
        self.pen.end_fill()

        # текст кнопки
        self.pen.penup()
        self.pen.goto(self.position[0], self.position[1] - 7)  # невеликий зсув для вирівнювання
        self.pen.color(self.text_color)
        self.pen.write(self.text, align="center", font=("Arial", 12, "bold"))

    def is_pressed(self, x, y):
        # перевірка кліку на кнопкє
        return (self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max)

    def update_colors(self, background_color, text_color, shown = 1):
        self.color = background_color
        self.text_color = text_color
        if shown:
            self.draw()


    def erase(self):
        self.pen.clear()


class AnalogClock(Watch):
    def __init__(self, radius=220):
        self.radius = radius
        self.theme = "light"

        self.face_pen = turtle.Turtle()
        self.face_pen.hideturtle()
        self.face_pen.speed(0)
        self.face_pen.pensize(3)

        # циферблат і стрілки
        self.digit_face = DigitFace(radius=radius)
        self.hour_hand = Hand(length=radius * 0.5, width=6, color="black")
        self.minute_hand = Hand(length=radius * 0.7, width=3, color="blue")
        self.second_hand = Hand(length=radius * 0.8, width=1, color="red")
        
        # центральна точка
        self.center_dot = turtle.Turtle()
        self.center_dot.hideturtle()
        self.center_dot.shape("circle")
        self.center_dot.color("black")
        self.center_dot.shapesize(0.5, 0.5)


        self.delay = 500
        self.running = 0

    def draw_clock_face(self):
        self.center_dot.penup()
        self.center_dot.goto(0, 0)
        self.center_dot.showturtle()
        

        self.face_pen.clear()
        self.face_pen.penup()
        self.face_pen.goto(0, -self.radius)
        self.face_pen.pendown()
        self.face_pen.circle(self.radius)

        self.digit_face.draw()

    def update_time(self):
        # поточний час
        now = datetime.now()

        hour = now.hour % 12
        minute = now.minute
        second = now.second

        hour_angle = (hour + minute / 60) * 30  # 30 на годину
        minute_angle = (minute + second / 60) * 6  # 6 на хвилину
        second_angle = second * 6  # 6 на секунду

        # стрілки
        self.hour_hand.draw(hour_angle)
        self.minute_hand.draw(minute_angle)
        self.second_hand.draw(second_angle)


    def set_theme(self, theme):
        self.theme = theme

        # зміна теми
        if theme == "dark":
            fg_color = "white"
            minute_color = "lightblue"
            btn_bg = "darkblue"
            btn_fg = "white"
        else:
            fg_color = "black"
            minute_color = "blue"
            btn_bg = "lightblue"
            btn_fg = "black"

        self.face_pen.color(fg_color)
        self.hour_hand.update_color(fg_color)
        self.minute_hand.update_color(minute_color)
        self.center_dot.color(fg_color)
        self.digit_face.update_color(fg_color)
        
        # перемальовуємо його
        if self.running:
            self.draw_clock_face()
            self.update_time()

    def draw(self):
        self.draw_clock_face()

    def erase(self):
        self.face_pen.clear()
        self.center_dot.hideturtle()
        self.digit_face.erase()
        self.minute_hand.erase()
        self.hour_hand.erase()
        self.second_hand.erase()

if __name__ == "__main__":
    clock = AnalogClock()
    clock.run()
    turtle.mainloop()
