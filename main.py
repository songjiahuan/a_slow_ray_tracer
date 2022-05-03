from vec3 import *
from color import *
from ray import *
from rtweekend import *
from hittable_list import *
from sphere import *


def ray_color(r: ray, world: hittable) -> color:
    rec = hit_record()
    if world.hit(r, 0, infinity, rec):
        return 0.5 * (rec.normal + color(1.0, 1.0 ,1.0))
    
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * color(1.0, 1.0, 1.0) + t * color(0.5, 0.7, 1.0)


if __name__ == '__main__':

    # image
    aspect_radio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_radio)

    # world
    world = hittable_list()
    world.add(sphere(point3(0, 0, -1), 0.5))
    world.add(sphere(point3(0, -100.5, -1), 100))

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
            pixel_color = ray_color(r, world)
            write_color(pixel_color)
