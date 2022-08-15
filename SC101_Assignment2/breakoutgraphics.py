"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    # constructor
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.brick_amount = brick_rows*brick_cols
        self.radius = ball_radius
        self.counts = 0

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball, x=0.5*self.window_width-self.radius, y=0.5*self.window_height-self.radius)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j % 10 == 0 or j % 10 == 1:
                    self.brick.fill_color = "red"
                    self.brick.color = "red"
                if j % 10 == 2 or j % 10 == 3:
                    self.brick.fill_color = "orange"
                    self.brick.color = "orange"
                if j % 10 == 4 or j % 10 == 5:
                    self.brick.fill_color = "yellow"
                    self.brick.color = "yellow"
                if j % 10 == 6 or j % 10 == 7:
                    self.brick.fill_color = "green"
                    self.brick.color = "green"
                if j % 10 == 8 or j % 10 == 9:
                    self.brick.fill_color = "blue"
                    self.brick.color = "blue"
                self.window.add(self.brick, x=i*(brick_width+brick_spacing), y=brick_offset+j*(brick_height+brick_spacing))

        # paddle move with mouse
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

    def ball_move(self, mouse):
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def paddle_move(self, mouse):
        if mouse.x >= 0.5*self.paddle.width and mouse.x <= self.window.width - 0.5*self.paddle.width:
            self.paddle.x = mouse.x - 0.5*self.paddle.width
        self.paddle.y = self.window.height-PADDLE_OFFSET-self.paddle.height

    def get_velocity_x(self):
        return self.__dx

    def get_velocity_y(self):
        return self.__dy

    def back_y(self):
        self.__dy = -self.__dy

    def back_x(self):
        self.__dx = -self.__dx

    def bouncing_ball(self):
        maybe_object1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_object2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        maybe_object3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        maybe_object4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        if maybe_object1 is not None:
            if maybe_object1 is self.paddle:
                self.back_y()
            else:
                self.back_y()
                self.window.remove(maybe_object1)
                self.counts += 1
        elif maybe_object2 is not None:
            if maybe_object2 is self.paddle:
                self.back_y()
            else:
                self.back_y()
                self.window.remove(maybe_object2)
                self.counts += 1
        elif maybe_object3 is not None:
            if maybe_object3 is self.paddle:
                self.back_y()
            else:
                self.back_y()
                self.window.remove(maybe_object3)
                self.counts += 1
        elif maybe_object4 is not None:
            if maybe_object4 is self.paddle:
                self.back_y()
            else:
                self.back_y()
                self.window.remove(maybe_object4)
                self.counts += 1

    def reset_position(self):
        # ball contacts with lower boundary
        self.ball.x = 0.5*self.window_width-self.radius
        self.ball.y = 0.5*self.window_height-self.radius
        self.__dx = 0
        self.__dy = 0