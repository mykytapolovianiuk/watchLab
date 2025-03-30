import turtle

class Button:
    def __init__(self, position, width, height, text, color="lightblue", text_color="black"):
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



