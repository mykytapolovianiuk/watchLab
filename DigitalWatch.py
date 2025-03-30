import turtle
from DigitalDial import DigitalDial
from Watch import Watch
from datetime import datetime
class DigitalWatch(Watch):
    def __init__(self, mode_button, height = 100, width = 400, mode = 12, position = (0,0)):
        
        self.mode_button = mode_button
        self.position = position
        self.height = 100
        self.width = 400
        self.digital_dial = DigitalDial(self.height, self.width)
        self.__mode = mode
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
    
    def change_mode(self):
        self.mode = 36 - self.mode

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
        self.mode_button.draw()
    def set_theme(self, theme):
        if theme == self.theme:
            return
        self.theme = theme
        if theme == "dark":
            self.face_pen.color('lightblue')
            btn_bg = "darkblue"
            btn_fg = "white"
        else:
            self.face_pen.color('black')
            btn_bg = "lightblue"
            btn_fg = "black"
        self.digital_dial.update_theme(theme,self.running)
        self.mode_button.update_colors(btn_bg, btn_fg, shown = self.running)
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
        self.mode_button.erase()

if __name__ == '__main__':
    import time
    w1 = DigitalWatch()
    w1.run()
    w1.set_theme('light')
    turtle.ontimer(lambda: w1.set_theme('light'), 2000)
    turtle.ontimer(lambda: w1.set_theme('dark'), 6000)
    turtle.ontimer(lambda: w1.run(), 8000)
    turtle.ontimer(lambda: w1.set_theme('light'), 10000)
    turtle.ontimer(lambda: w1.set_theme('dark'), 12000)
    print('here')
    turtle.ontimer(lambda: print(13), 13000)
    turtle.Screen().update()
    turtle.ontimer(lambda: w1.change_mode(),2000)
    turtle.ontimer(lambda: w1.change_mode(),4000)
    turtle.ontimer(lambda: w1.change_mode(),6000)

    turtle.mainloop()

