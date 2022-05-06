from math import tan


from vec3 import *
from ray import *


class camera:
    def __init__(self, lookfrom: point3, lookat: point3, vup: vec3, vfov: float, aspect_radio: float):
        theta = degrees_to_radians(vfov)
        h = tan(theta / 2)
        viewport_height = 2.0 * h
        viewport_width =  aspect_radio * viewport_height

        w = unit_vector(lookfrom - lookat)
        u = unit_vector(cross(vup, w))
        v = cross(w, u)

        self.origin = lookfrom
        self.horizontal = viewport_width * u
        self.vertical = viewport_height * v
        self.lower_left_corner = self.origin - self.horizontal / 2.0 - self.vertical / 2.0 - w
        
    def get_ray(self, s: float, t: float) -> ray:
        return ray(self.origin, self.lower_left_corner + s * self.horizontal + t * self.vertical - self.origin)
