from cv2 import norm
from rtweekend import *


class vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.__x = x
        self.__y = y
        self.__z = z

    def x(self):
        return self.__x
    
    def y(self):
        return self.__y
    
    def z(self):
        return self.__z
    
    def __call__(self, index):
        v = [self.__x, self.__y, self.__z]
        return v[index]

    def __getitem__(self, index):
        v = [self.__x, self.__y, self.__z]
        return v[index]

    def __repr__(self):
        return '(' + str(self.__x) + ',' + str(self.__y) + ',' + str(self.__z) + ')'
    
    def __neg__(self):
        return vec3(-self.__x, -self.__y, -self.__z)
    
    def __iadd__(self, v):
        return vec3(self.__x + v.x(), self.__y + v.y(), self.__z + v.z())
    
    def __imul__(self, num):
        return vec3(self.__x * num, self.__y * num, self.__z * num)
    
    def __idiv__(self, num):
        return vec3(self.__x / num, self.__y / num, self.__z / num)

    def __add__(self, v):
        return vec3(self.__x + v.x(), self.__y + v.y(), self.__z + v.z())
    
    def __sub__(self, v):
        return vec3(self.__x - v.x(), self.__y - v.y(), self.__z - v.z())
    
    def __mul__(self, v):
        if isinstance(v, vec3):
            return vec3(self.__x * v.x(), self.__y * v.y(), self.__z * v.z())
        elif isinstance(v, int) or isinstance(v, float):
            return vec3(v * self.__x, v * self.__y, v * self.__z)
        else:
            pass

    def __rmul__(self, num):
        return vec3(num * self.__x, num * self.__y, num * self.__z)

    def __truediv__(self, num):
        return vec3(self.__x / num, self.__y / num, self.__z / num)

    def length(self):
        return self.length_squared() ** 0.5
    
    def length_squared(self):
        return self.__x * self.__x + self.__y * self.__y + self.__z * self.__z

    def random(self, min=0.0, max=1.0):
        return vec3(random_double(min, max), random_double(min, max), random_double(min, max))

    def copy(self, v):
        self.__x = v.x()
        self.__y = v.y()
        self.__z = v.z()

    def near_zero(self):
        s = 1e-8
        return (abs(self.__x) < s) and (abs(self.__y) < s) and (abs(self.__z) < s)


point3 = vec3
color = vec3


def dot(v1: vec3, v2: vec3) -> float:
    return v1.x() * v2.x() + v1.y() * v2.y() + v1.z() * v2.z()


def cross(v1: vec3, v2: vec3) -> vec3:
    return vec3(v1.y() * v2.z() - v1.z() * v2.y(),
                v1.z() * v2.x() - v1.x() * v2.z(),
                v1.x() * v2.y() - v1.y() * v2.x())


def unit_vector(v: vec3) -> vec3:
    return v / v.length()


def random_in_unit_sphere() -> point3:
    while True:
        p = vec3.random(None, -1.0, 1.0)
        if p.length_squared() < 1:
            return p


def random_unit_vector() -> vec3:
    return unit_vector(random_in_unit_sphere())


def random_in_hemisphere(normal: vec3) -> point3:
    in_unit_sphere = random_in_unit_sphere()
    if dot(in_unit_sphere, normal) > 0.0:
        return in_unit_sphere
    else:
        return -in_unit_sphere


def reflect(v: vec3, n: vec3) -> vec3:
    return v - 2 * dot(v, n) * n
    
    
def refract(uv: vec3, n: vec3, etai_over_etat) -> vec3:
    cos_theta = min(dot(-uv, n), 1.0)
    r_out_perp: vec3 = etai_over_etat * (uv + cos_theta * n)
    r_out_parallel: vec3 = -(abs(1.0 - r_out_perp.length_squared())) ** 0.5 * n
    return r_out_perp + r_out_parallel
