from operator import index, indexOf
from hittable import *


class material:
    @abstractmethod
    def scatter(self, r_in: ray, rec: hit_record, attenuation: color, scattered: ray) -> bool:
        pass


class lambertian(material):
    def __init__(self, a: color):
        self.albedo = a

    def scatter(self, r_in: ray, rec: hit_record, attenuation: color, scattered: ray) -> bool:
        scatter_direction = rec.normal + random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = rec.normal
        
        scattered.copy(ray(rec.p, scatter_direction))
        attenuation.copy(self.albedo)
        return True


class metal(material):
    def __init__(self, a: color, f: float):
        self.albedo = a
        self.fuzz = f if f < 1 else 1

    def scatter(self, r_in: ray, rec: hit_record, attenuation: color, scattered: ray) -> bool:
        reflected = reflect(unit_vector(r_in.direction()), rec.normal)
        scattered.copy(ray(rec.p, reflected + self.fuzz * random_in_unit_sphere()))
        attenuation.copy(self.albedo)
        return (dot(scattered.direction(), rec.normal) > 0)
        

class dielectric(material):
    def __init__(self, index_of_refraction=1.0) -> None:
        self.ir = index_of_refraction

    def scatter(self, r_in: ray, rec: hit_record, attenuation: color, scattered: ray) -> bool:
        attenuation.copy(color(1.0, 1.0, 1.0))
        refraction_radio = (1.0 / self.ir) if rec.front_face else self.ir

        unit_direction = unit_vector(r_in.direction())
        cos_theta = min(dot(-unit_direction, rec.normal), 1.0)
        sin_theta = (1.0 - cos_theta * cos_theta) ** 0.5

        cannot_refract = (refraction_radio * sin_theta > 1.0)
        if cannot_refract:
            direction = reflect(unit_direction, rec.normal)
        else:
            direction = refract(unit_direction, rec.normal, refraction_radio)

        scattered.copy(ray(rec.p, direction))
        return True
