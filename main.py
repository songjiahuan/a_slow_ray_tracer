import sys


from vec3 import *
from color import *
from ray import *
from rtweekend import *
from hittable_list import *
from sphere import *
from camera import *
from material import *


def ray_color(r: ray, world: hittable, depth: int) -> color:
    rec = hit_record()
    if depth <= 0:
        return color(0, 0, 0)

    if world.hit(r, 0.001, infinity, rec):
        scattered = ray()
        attenuation = color()
        if rec.mat_ptr.scatter(r, rec, attenuation, scattered):
            return attenuation * ray_color(scattered, world, depth - 1)
        return color(0, 0, 0)
    
    unit_direction = unit_vector(r.direction())
    t = 0.5 * (unit_direction.y() + 1.0)
    return (1.0 - t) * color(1.0, 1.0, 1.0) + t * color(0.5, 0.7, 1.0)


if __name__ == '__main__':

    # image
    aspect_radio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_radio)
    samples_per_pixel = 100
    max_depth = 50

    # world
    world = hittable_list()
    
    material_ground = lambertian(color(0.8, 0.8, 0.0))
    material_center = lambertian(color(0.7, 0.3, 0.3))
    material_left   = metal(color(0.8, 0.8, 0.8), 0.3)
    material_right  = metal(color(0.8, 0.6, 0.2), 1.0)

    world.add(sphere(point3(0, -100.5, -1), 100.0, material_ground))
    world.add(sphere(point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(sphere(point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(sphere(point3(1.0, 0.0, -1.0), 0.5, material_right))
    

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
                pixel_color += ray_color(r, world, max_depth)
            
            write_color(pixel_color, samples_per_pixel)

    sys.stderr.write('\nDone.\n')
