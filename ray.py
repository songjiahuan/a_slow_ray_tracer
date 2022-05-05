from vec3 import *


class ray:
    def __init__(self, origin: vec3=None, direction: vec3=None):
        self.__orig = origin
        self.__dir = direction
    
    def origin(self):
        return self.__orig
    
    def direction(self):
        return self.__dir
    
    def at(self, t):
        return self.__orig + t * self.__dir

    def copy(self, r):
        self.__orig = r.origin()
        self.__dir = r.direction()
