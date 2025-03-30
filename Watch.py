import turtle

class Watch():
    def __init__(self):
        self.delay = 0
        self.running = 0
        pass
    def draw_clock_face(self):
        pass
    def run(self):
        self.running = 1
        self.draw()
        self.update()
    def update_time(self):
        pass
    def update(self):
        if self.running:
            self.update_time()
            turtle.ontimer(lambda: self.update(), self.delay)
    def draw(self):
        pass
    def erase(self):
        pass
    def stop(self):
        self.running = 0
        self.erase()
   
