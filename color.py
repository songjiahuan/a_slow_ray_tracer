from rtweekend import clamp
from vec3 import *


def write_color(pixel_color: color, samples_per_pixel: int):
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    scale = 1.0 / samples_per_pixel
    r *= scale
    g *= scale
    b *= scale

    print(str(int(256 * clamp(r, 0.0, 0.999))) + ' ' +
          str(int(256 * clamp(g, 0.0, 0.999))) + ' ' +
          str(int(256 * clamp(b, 0.0, 0.999))))
