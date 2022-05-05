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
        