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


def random_scene() -> hittable_list:
    world = hittable_list()
    ground_material = lambertian(color(0.5, 0.5, 0.5))
    world.add(sphere(point3(0, -1000, 0), 1000, ground_material))

    for a in range(-11, 11):
        for b in range(-11, 11):
            choose_mat = random_double()
            center = point3(a + 0.9 * random_double(), 0.2, b + 0.9 * random_double())

            if (center - point3(4, 0.2, 0)).length() > 0.9:
                sphere_material = material()

                if choose_mat < 0.8:
                    albedo = color.random(None) * color.random(None)
                    sphere_material = lambertian(albedo)
                    world.add(sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    albedo = color.random(0.5, 1)
                    fuzz = random_double(0, 0.5)
                    sphere_material = metal(albedo, fuzz)
                    world.add(sphere(center, 0.2, sphere_material))
                else:
                    sphere_material = dielectric(1.5)
                    world.add(sphere(center, 0.2, sphere_material))

    material1 = dielectric(1.5)
    world.add(sphere(point3(0, 1, 0), 1.0, material1))

    material2 = lambertian(color(0.4, 0.2, 0.1))
    world.add(sphere(point3(-4, 1, 0), 1.0, material2))

    material3 = metal(color(0.7, 0.6, 0.5), 0.0)
    world.add(sphere(point3(4, 1, 0), 1.0, material3))

    return world


if __name__ == '__main__':

    # image
    aspect_radio = 3.0 / 2.0
    image_width = 1200
    image_height = int(image_width / aspect_radio)
    samples_per_pixel = 500
    max_depth = 50


    # world
    world = random_scene()


    # camera
    lookfrom = point3(13, 2, 3)
    lookat = point3(0, 0, 0)
    vup = point3(0, 1, 0)
    dist_to_focuus = 10.0
    aperture = 0.1

    cam = camera(lookfrom, lookat, vup, 20, aspect_radio, aperture, dist_to_focuus)

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
