"""
File: draw_line
Name: Rosy Huang
-------------------------
TODO: This program draw lines!
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause

SIZE = 10
# global variables
window = GWindow()
circle = GOval(SIZE, SIZE)
times = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    while True:
        onmouseclicked(start)
        if times % 2 == 1:
            onmouseclicked(end)
        pause(10)


def start(mouse):
    global times
    window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
    times += 1


def end(mouse):
    global times
    line = GLine(circle.x, circle.y, mouse.x, mouse.y)
    window.add(line)
    window.remove(circle)
    times += 1


if __name__ == "__main__":
    main()
