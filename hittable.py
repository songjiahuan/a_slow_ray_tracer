from abc import abstractmethod
from vec3 import *
from ray import *


class hit_record:
    def __init__(self):
        self.p = point3()
        self.normal = vec3()
        self.t = 0.0
        self.front_face = True

    def copy(self, rec):
        self.p = rec.p
        self.normal = rec.normal
        self.t = rec.t
        self.front_face = rec.front_face

    def set_face_normal(self, r: ray, outward_normal: vec3):
        self.front_face = (dot(r.direction(), outward_normal) < 0.0)
        self.normal = outward_normal if self.front_face else -outward_normal


class hittable:
    @abstractmethod
    def hit(self, r: ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        pass
