import turtle
from DigitalDial import DigitalDial
from Watch import Watch
from datetime import datetime
class DigitalWatch(Watch):
    def __init__(self, height = 100, width = 400, mode = 12, position = (0,0)):
        
        self.screen = turtle.Screen()
        self.screen.title("Аналоговий годинник")
        self.screen.bgcolor("white")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)  # Вимикаємо автоматичне оновлення для кращої продуктивності

        self.position = position
        self.height = 100
        self.width = 400
        self.digital_dial = DigitalDial(self.height, self.width)
        self.__mode = 12
        self.theme = 'light'
        self.face_pen = turtle.Turtle()
        self.face_pen.hideturtle()
        self.face_pen.speed(0)
        self.face_pen.pensize(5)
        self.face_pen.width(5)
        self.face_pen.color('black')
        self.running = 0
        self.delay = 1000

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        if value == 12 or value == 24:
            self.__mode = value
            self.update_time()
        else:
            print("Немає такого формату")
    
    
    def draw_clock_face(self):
        t = self.face_pen
        t.clear()
        t.up()
        t.goto(self.position[0] - self.width/2, self.position[1] + self.height/2)
        t.down()
        t.seth(0)
        t.forward(self.width)
        t.seth(270)
        t.forward(self.height)
        t.seth(180)
        t.forward(self.width)
        t.seth(90)
        t.forward(self.height)
        t.up()

    def draw(self):
        self.draw_clock_face()
        self.digital_dial.draw()
    def set_theme(self, theme):
        if theme == self.theme:
            return
        self.theme = theme
        if theme == "dark":
            self.face_pen.color('lightblue')
        else:
            self.face_pen.color('black')

        self.digital_dial.update_theme(theme,self.running)
        if self.running:
            self.draw_clock_face()

    def update_time(self):
        now = datetime.now()
        hours = now.hour % self.mode
        minutes = now.minute
        self.digital_dial.update(hours, minutes)
        
    def erase(self):
        self.face_pen.clear()
        self.digital_dial.erase()

if __name__ == '__main__':
    import time
    w1 = DigitalWatch()
    w1.run()
    w1.set_theme('light')
    turtle.ontimer(lambda: w1.set_theme('light'), 2000)
    turtle.ontimer(lambda: w1.stop(), 4000)
    turtle.ontimer(lambda: w1.set_theme('dark'), 6000)
    turtle.ontimer(lambda: w1.run(), 8000)
    turtle.ontimer(lambda: w1.set_theme('light'), 10000)
    turtle.ontimer(lambda: w1.set_theme('dark'), 12000)
    print('here')
    turtle.ontimer(lambda: print(13), 13000)
    turtle.ontimer(lambda: w1.stop(), 14000)
    turtle.mainloop()

