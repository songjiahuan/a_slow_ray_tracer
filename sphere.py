from vec3 import *
from hittable import *


class sphere(hittable):
    def __init__(self, cen: point3, r: float):
        self.center = cen
        self.radius = r
    
    def hit(self, r: ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        oc = r.origin() - self.center
        a = r.direction().length_squared()
        half_b = dot(oc, r.direction())
        c = oc.length_squared() - self.radius * self.radius

        discriminant = half_b * half_b - a * c
        if discriminant < 0.0:
            return False
        sqrtd = discriminant ** 0.5

        root = (-half_b - sqrtd) / a
        if root < t_min or root > t_max:
            root = (-half_b + sqrtd) / a
            if root < t_min or root > t_max:
                return False
        
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)

        return True
