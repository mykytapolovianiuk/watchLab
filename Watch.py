import turtle

class Watch():
    def __init__(self):
        self.delay = 0
        self.running = 0
        pass
    def draw_clock_face(self):
        pass
    def run(self,screen = turtle.Screen()):
        self.running = 1
        self.draw()
        self.update(screen)
    def update_time(self):
        pass
    def update(self,screen):
        if self.running:
            self.update_time()
            screen.update()
            turtle.ontimer(lambda: self.update(screen), self.delay)
    def draw(self):
        pass
    def erase(self):
        pass
    def stop(self):
        self.running = 0
        self.erase()
   
