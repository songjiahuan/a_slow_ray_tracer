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


def dot(v1: vec3, v2: vec3):
    return v1.x() * v2.x() + v1.y() * v2.y() + v1.z() * v2.z()


def cross(v1: vec3, v2: vec3):
    return vec3(v1.y() * v2.z() - v1.z() * v2.y(),
                v1.z() * v2.x() - v1.x() * v2.z(),
                v1.x() * v2.y() - v1.y() * v2.x())


def unit_vector(v: vec3):
    return v / v.length()


point3 = vec3
color = vec3
