from random import randrange as rnd


# Dirty screen shake solution
def screen_shake(window, timer):
    shake_timer = timer

    if shake_timer > 0:

        if shake_timer % 5 == 0:
            offset_x = rnd(-8, 8)
            offset_y = rnd(-8, 8)

        shake_timer -= 1
        window.x = offset_x
        window.y = offset_y
