from xmlrpc.client import boolean

from numpy import uint
from vec3 import *
from color import *
from ray import *


def hit_sphere(center: point3, radius: float, r: ray) -> float:
    oc = r.origin() - center
    a = r.direction().length_squared()
    half_b = dot(oc, r.direction())
    c = oc.length_squared() - radius * radius
    discriminant = half_b * half_b - a * c
    if discriminant < 0.0:
        return -1.0
    else:
        return (-half_b - discriminant ** 0.5) / a


def ray_color(r: ray) -> color:
    t = hit_sphere(point3(0, 0, -1), 0.5, r)
    if t > 0.0:
        N = unit_vector(r.at(t) - point3(0, 0, -1))
        return 0.5 * color(N.x() + 1, N.y() + 1, N.z() + 1)
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * color(1.0, 1.0, 1.0) + t * color(0.5, 0.7, 1.0)


if __name__ == '__main__':

    # image
    aspect_radio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_radio)

    # camera
    viewport_height = 2.0
    viewport_width = aspect_radio * viewport_height
    focal_length = 1.0

    origin = point3(0, 0, 0)
    horizontal = vec3(viewport_width, 0, 0)
    vertical = vec3(0, viewport_height, 0)
    lower_left_corner = origin - horizontal / 2 - vertical / 2 - vec3(0, 0, focal_length)


    # render
    print("P3\n" + str(image_width) + ' ' + str(image_height) + '\n255')

    for j in range(image_height-1, -1, -1):
        for i in range(0, image_width):
            u = i / (image_width - 1)
            v = j / (image_height - 1)
            r = ray(origin, lower_left_corner + u * horizontal + v * vertical - origin)
            pixel_color = ray_color(r)
            write_color(pixel_color)
