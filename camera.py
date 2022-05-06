from math import tan


from vec3 import *
from ray import *


class camera:
    def __init__(self, lookfrom: point3, lookat: point3, vup: vec3, vfov: float, \
                 aspect_radio: float, aperture: float, focus_dist: float):
        theta = degrees_to_radians(vfov)
        h = tan(theta / 2)
        viewport_height = 2.0 * h
        viewport_width =  aspect_radio * viewport_height

        self.w = unit_vector(lookfrom - lookat)
        self.u = unit_vector(cross(vup, self.w))
        self.v = cross(self.w, self.u)

        self.origin = lookfrom
        self.horizontal = focus_dist * viewport_width * self.u
        self.vertical = focus_dist * viewport_height * self.v
        self.lower_left_corner = self.origin - self.horizontal / 2.0 - self.vertical / 2.0 - focus_dist * self.w

        self.lens_radius = aperture / 2.0
        
    def get_ray(self, s: float, t: float) -> ray:
        rd = self.lens_radius * random_in_unit_disk()
        offset = self.u * rd.x() + self.v * rd.y()
        return ray(self.origin + offset, self.lower_left_corner + s * self.horizontal + \
                   t * self.vertical - self.origin - offset)
