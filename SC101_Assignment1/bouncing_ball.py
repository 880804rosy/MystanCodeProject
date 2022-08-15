"""
File: bouncing_ball
Name: Rosy Huang
-------------------------
TODO: This program creates bouncing balls.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


# Constant
VX = 10
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global variables
ball = GOval(SIZE, SIZE)
window = GWindow(width=800, height=500, title="bouncing_ball.py")
times = 0


def main():
    ball.filled = True
    ball.fill_color = "black"
    ball.color = "black"
    while True:
        window.add(ball, x=START_X, y=START_Y)
        onmouseclicked(start)
        pause(DELAY)


def start(click):
    global times
    # 為了在球動的過程中如果點按不會影響球的movement
    if ball.x == START_X and ball.y == START_Y:
        times += 1          # counts of run
        a = 0               # to simulate time(counts of while loop)
        while True:
            if ball.x >= 800-SIZE or times > 3:
                break
            a += 1
            vy = a * GRAVITY    # when the ball goes downward
            ball.move(VX, vy)
            if ball.y >= 500 - SIZE:
                a = 0
                last_vy = vy
                while True:     # when the ball is bouncing upward
                    a += 1
                    vy = -(0.9*last_vy - a*GRAVITY)
                    ball.move(VX, vy)
                    pause(DELAY)
                    if vy >= 0:
                        a = 0
                        break
            pause(DELAY)



if __name__ == "__main__":
    main()
