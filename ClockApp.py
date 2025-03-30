import turtle
from DigitalWatch import DigitalWatch
from script import AnalogClock as AnalogWatch, Button as Button

class ClockApp():
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Годинник")
        self.screen.bgcolor("white")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)  # Вимикаємо автоматичне оновлення для кращої продуктивності
        self.theme = "light"
       # кнопка для зміни теми
        self.theme_button = Button(
            position=(-200, -250),
            width=120,
            height=40,
            text="Змінити тему"
        )

        # це для кнопочки, яка буде змінювати тип годинниика
        self.type_button = Button(
                position = (200, -250),
                width = 140,
                height = 40,
                text = "Змінити годинник"
        )
        self.digital_watch_mode_button = Button(
                position = (200,250),
                width = 140,
                height = 40,
                text = "Змінити формат"
        )
        
        self.analog_watch = AnalogWatch()
        self.digital_watch = DigitalWatch(mode_button = self.digital_watch_mode_button)
        self.curr_watch = self.analog_watch
        self.screen.onclick(self.handle_click)
        self.start()
    def start(self):
        self.theme_button.draw()
        self.type_button.draw()
        self.curr_watch.run()
        self.screen.mainloop()
    def set_theme(self, theme):
        self.theme = theme
        # зміна теми
        if theme == "dark":
            bg_color = "black"
            btn_bg = "darkblue"
            btn_fg = "white"
        else:
            bg_color = "white"
            btn_bg = "lightblue"
            btn_fg = "black"

        self.theme_button.update_colors(btn_bg, btn_fg)
        self.type_button.update_colors(btn_bg, btn_fg)
        #self.digital_watch_mode_button.update_colors(btn_bg,btn_fg) - changed in digital watch
        self.screen.bgcolor(bg_color)
        self.analog_watch.set_theme(theme)
        self.digital_watch.set_theme(theme)
        self.screen.update()

    def change_clock_type(self):
        self.curr_watch.stop()
        self.curr_watch = self.analog_watch if self.curr_watch == self.digital_watch else self.digital_watch
        self.curr_watch.run(self.screen)
        self.screen.update()

    def handle_click(self, x, y):
        if self.theme_button.is_pressed(x, y):
            new_theme = "dark" if self.theme == "light" else "light"
            self.set_theme(new_theme)
        if self.type_button.is_pressed(x,y):
            self.change_clock_type()
        if self.curr_watch == self.digital_watch:
            if self.digital_watch_mode_button.is_pressed(x,y):
                self.digital_watch.change_mode()
                self.screen.update()


if __name__ == '__main__':
    a1 = ClockApp()

