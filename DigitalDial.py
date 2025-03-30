from SegmentDigit import SegmentDigit
import turtle
class DigitalDial():
    def __init__(self, watch_height = 100, watch_width = 400, watch_position = (0,0)):
        self.segment_length = min(watch_width//9, watch_height//3)
        self.position = watch_position
        available_width = self.segment_length
        available_height = self.segment_length * 2
        self.digits = [SegmentDigit(position = (self.position[0] - 3*self.segment_length,self.position[1]), available_width = available_width, available_height = available_height, segment_length = self.segment_length),
                       SegmentDigit(position = (self.position[0] - 1*self.segment_length,self.position[1]), available_width = available_width, available_height = available_height, segment_length = self.segment_length),
                       SegmentDigit(position = (self.position[0] + 1*self.segment_length,self.position[1]), available_width = available_width, available_height = available_height, segment_length = self.segment_length),
                       SegmentDigit(position = (self.position[0] + 3*self.segment_length,self.position[1]),available_width = available_width, available_height = available_height, segment_length = self.segment_length)]
        self.color = 'lightblue'
        self.theme = 'light'
        self.t = turtle.Turtle()
        self.t.hideturtle()

    def draw_colon(self):
        t = self.t
        t.clear()
        t.up()
        t.goto(self.position[0],self.position[1] + self.segment_length * 0.333)
        t.dot(self.segment_length * 0.2, self.color)
        t.goto(self.position[0], self.position[1] - self.segment_length * 0.333)
        t.dot(self.segment_length * 0.2, self.color)

    def update(self, hours, minutes):
        self.digits[0].draw(hours//10)
        self.digits[1].draw(hours%10)
        self.digits[2].draw(minutes//10)
        self.digits[3].draw(minutes%10)
        
    
    def update_theme(self,theme, running = 1):
        if self.theme == theme:
            return
        self.theme = theme
        if theme == 'dark':
            self.color = 'red'
        else:
            self.color = 'lightblue'
        for digit in self.digits:
            digit.update_theme(theme)
        if not running:
            return
        self.draw_colon()
           
    def draw(self, hours = 0, minutes = 0):
        self.digits[0].draw(hours//10)
        self.digits[1].draw(hours%10)
        self.digits[2].draw(minutes//10)
        self.digits[3].draw(minutes%10)
        self.draw_colon()
        
    def erase(self):
        self.t.clear()
        for digit in self.digits:
            digit.erase()
if __name__ == '__main__':
    d1 = DigitalDial()
    d1.draw(0,0)
    d1.update_theme('dark')
    import time
    time.sleep(2)
    d1.update(4,12)
    time.sleep(2)

    d1.erase()
    time.sleep(2)
    d1.update_theme('light', 0)
    time.sleep(2)
    d1.draw(23,59)
    time.sleep(2)
    d1.update(0,1)
    d1.erase()
    turtle.mainloop()
                       
