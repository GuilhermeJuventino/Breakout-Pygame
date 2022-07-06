from random import randrange as rnd


# Dirty screen shake solution
class ScreenShake:
    def __init__(self):
        self.timer = 0
        self.offset_x = 0
        self.offset_y = 0

    def shake(self, window):
        if self.timer > 0:

            if self.timer % 5 == 0:
                self.offset_x = rnd(-8, 8)
                self.offset_y = rnd(-8, 8)

            self.timer -= 1
            window.x = self.offset_x
            window.y = self.offset_y

        else:
            self.offset_x = 0
            self.offset_y = 0
