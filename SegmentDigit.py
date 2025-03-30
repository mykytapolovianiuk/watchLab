import turtle

class SegmentDigit():
    #  0
    #5   1
    #  6
    #4   2
    #  3
    def __init__(self, position = (0,0), available_width = 20, available_height = 40, segment_length = None):
        if(segment_length == None):
            self.segment_length = min(available_height//2, available_width)
        else:
            self.segment_length = segment_length
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.pensize(4)
        self.start_position = (position[0] - self.segment_length/2, position[1]+self.segment_length)
        self.color = "lightblue"
        self.digits = [[1,1,1,1,1,1,0],
                       [0,1,1,0,0,0,0],
                       [1,1,0,1,1,0,1],
                       [1,1,1,1,0,0,1],
                       [0,1,1,0,0,1,1],
                       [1,0,1,1,0,1,1],
                       [1,0,1,1,1,1,1],
                       [1,1,1,0,0,0,0],
                       [1,1,1,1,1,1,1],
                       [1,1,1,1,0,1,1]]
        self.angles = [0,270,270,180,90,90,0]
        self.theme = 'light'
        self.curr_digit = None
    def draw(self,digit,theme_change = 0):
        print(f"{theme_change =}")
        if self.curr_digit == digit and theme_change == 0:
            return
        self.t.clear()
        self.curr_digit = digit
        self.t.up()
        self.t.pencolor(self.color)
        self.t.goto(self.start_position)
        segments = self.digits[digit]
        for i in range(7):
            if(i == 6):
                self.t.goto(self.start_position[0], self.start_position[1]-self.segment_length)
            self.t.seth(self.angles[i])
            self.t.up()
            
            self.t.forward(self.segment_length * 0.15)
            if segments[i]:
                self.t.down()
            else:
                self.t.up()
            self.t.forward(self.segment_length*0.7)
            self.t.up()
            self.t.forward(self.segment_length * 0.15)

    def update_theme(self, theme):
        if theme == self.theme:
            return
        self.theme = theme
        if theme == 'dark':
            self.color = 'red'
        else:
            self.color = 'lightblue'
        
        self.draw(self.curr_digit, theme_change = 1)


    def erase(self):
        self.t.clear()
        self.curr_digit = None

if __name__ == '__main__':
    d = SegmentDigit()
    t = turtle.Turtle()
    t.dot(3, "red")
    for i in range(1,10):
        d.draw(i)
        import time
        time.sleep(1)
    turtle.mainloop()
