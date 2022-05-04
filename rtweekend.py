import random


infinity = float ("inf")
pi = 3.1415926535897932385

def degrees_to_radians(degrees):
    return pi * degrees / 180.0


def random_double(min=0.0, max=1.0):
    return min + (max - min) * random.random()


def clamp(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
    return x
    