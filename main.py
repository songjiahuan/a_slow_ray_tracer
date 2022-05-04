import sys


from vec3 import *
from color import *
from ray import *
from rtweekend import *
from hittable_list import *
from sphere import *
from camera import *


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
    samples_per_pixel = 100

    # world
    world = hittable_list()
    world.add(sphere(point3(0, 0, -1), 0.5))
    world.add(sphere(point3(0, -100.5, -1), 100))

    # camera
    cam = camera()

    # render
    print("P3\n" + str(image_width) + ' ' + str(image_height) + '\n255')

    for j in range(image_height-1, -1, -1):
        sys.stderr.write('\rProcessing: {:.2f}%'.format((image_height - j) / image_height * 100))
        for i in range(0, image_width):
            pixel_color = color(0.0, 0.0, 0.0)
            for s in range(0, samples_per_pixel):
                u = (i + random_double()) / (image_width - 1)
                v = (j + random_double()) / (image_height - 1)
                r = cam.get_ray(u, v)
                pixel_color += ray_color(r, world)
            
            write_color(pixel_color, samples_per_pixel)

    sys.stderr.write('\nDone.\n')
