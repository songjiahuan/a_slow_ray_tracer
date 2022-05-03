from hittable import *


class hittable_list(hittable):
    def __init__(self, object :hittable=None):
        self.objects = []
        if object != None:
            self.objects.append(object)
    
    def clear(self):
        self.objects.clear()

    def add(self, object: hittable):
        self.objects.append(object)

    def hit(self, r: ray, t_min: float, t_max: float, rec: hit_record) -> bool:
        temp_rec = hit_record()
        hit_anything = False
        closest_so_far = t_max

        for object in self.objects:
            if object.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec.copy(temp_rec)
                
        return hit_anything
