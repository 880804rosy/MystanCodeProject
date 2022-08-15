"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 15       # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    lives = NUM_LIVES
    while True:
        graphics.ball.move(graphics.get_velocity_x(), graphics.get_velocity_y())
        pause(FRAME_RATE)
        # ball bounces back from wall
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.reset_position()
            graphics.ball.move(graphics.get_velocity_x(), graphics.get_velocity_y())
        if lives == 0:
            break
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.back_x()
        if graphics.ball.y <= 0:
            graphics.back_y()
        # balls contacts with paddle or bricks
        if graphics.counts == graphics.brick_amount:
            break
        graphics.bouncing_ball()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
