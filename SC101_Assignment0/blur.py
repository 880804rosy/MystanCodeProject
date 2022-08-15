"""
File: blur.py
Name: Rosy Huang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, Original picture
    :return: new_img, SimpleImage, Blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel = new_img.get_pixel(x, y)
            total_red = 0
            total_blue = 0
            total_green = 0
            total_num = 0
            # set limit for border situation
            if x == 0:
                neighbor_x0 = x
            else:
                neighbor_x0 = x - 1
            if x == img.width-1:
                neighbor_xx = x
            else:
                neighbor_xx = x + 1

            if y == 0:
                neighbor_y0 = y
            else:
                neighbor_y0 = y - 1
            if y == img.height-1:
                neighbor_yy = y
            else:
                neighbor_yy = y + 1
            # get blurred color value
            for i in range(neighbor_x0, neighbor_xx+1):
                for j in range(neighbor_y0, neighbor_yy + 1):
                    total_red += img.get_pixel(i, j).red
                    total_green += img.get_pixel(i, j).green
                    total_blue += img.get_pixel(i, j).blue
                    total_num += 1

            pixel.red = total_red / total_num
            pixel.green = total_green / total_num
            pixel.blue = total_blue / total_num
    return new_img


def main():
    """
    TODO: This program creates blurred img from old_img
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
