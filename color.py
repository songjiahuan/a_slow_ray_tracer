from vec3 import *


def write_color(pixel_color: color):
    print(str(int(255.999 * pixel_color.x())) + ' ' +
          str(int(255.999 * pixel_color.y())) + ' ' +
          str(int(255.999 * pixel_color.z())))
