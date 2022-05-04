from vec3 import *
from ray import *


class camera:
    def __init__(self):
        aspect_radio = 16.0 / 9.0
        viewport_height = 2.0
        viewport_width = viewport_height * aspect_radio
        focal_length = 1.0

        self.origin = point3(0.0, 0.0, 0.0)
        self.horizontal = vec3(viewport_width, 0.0, 0.0)
        self.vertical = vec3(0.0, viewport_height, 0.0)
        self.lower_left_corner = self.origin - self.horizontal / 2.0 - \
                                 self.vertical / 2.0 - vec3(0.0, 0.0, focal_length)
        
    def get_ray(self, u: float, v: float) -> ray:
        return ray(self.origin, self.lower_left_corner + u * self.horizontal + v * self.vertical - self.origin)
