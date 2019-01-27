import math
import random

class Vec2(object):
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = float(new_x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = float(new_y)

    def __add__(self, other):
        types = (int, float)
        if isinstance(self, types):
            return Vec2(self + other.x, self + other.y)
        elif isinstance(other, types):
            return Vec2(self.x + other, self.y + other)
        else:
            return Vec2(self.x + other.x, self.y + other.y)

    def __div__(self, other):
        types = (int, float)
        if isinstance(self, types):
            self = Vec2(self, self)
        elif isinstance(other, types):
            other = Vec2(other, other)
        x = self.x / other.x
        y = self.y / other.y
        return Vec2(x, y)

    def __mul__(self, other):
        types = (int, float)
        if isinstance(self, types):
            return Vec2(self * other.x, self * other.y)
        elif isinstance(other, types):
            return Vec2(self.x * other, self.y * other)
        else:
            return Vec2(self.x * other.x, self.y * other.y)

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __radd__(self, other):
        return Vec2(self.x + other, self.y + other)

    def __rdiv__(self, other):
        return Vec2(other/self.x, other/self.y)

    def __rmul__(self, other):
        return Vec2(other * self.x, other * self.y)

    def __rsub__(self, other):
        return Vec2(other - self.x, other - self.y)

    def __sub__(self, other):
        types = (int, float)
        if isinstance(self, types):
            return Vec2(self - other.x, self - other.y)
        elif isinstance(other, types):
            return Vec2(self.x - other, self.y - other)
        else:
            return Vec2(self.x - other.x, self.y - other.y)


    def get_data(self):
        return (self.x, self.y)

    def inverse(self):
        return Vec2(-1.0/self.x, -1.0/self.y)

    def length(self):
        return math.sqrt(self.square_length())

    def normalize(self):
        length = self.length()
        if length == 0.0:
            return Vec2(0, 0)
        return Vec2(self.x/length, self.y/length)

    def square_length(self):
        return (self.x * self.x) + (self.y * self.y)

    @classmethod
    def distance(cls, a, b):
        c = b - a
        return c.length()

    @classmethod
    def dot(self, a, b):
        return (a.x * b.x) + (a.y * b.y)


    @classmethod
    def square_distance(cls, a, b):
        c = b - a
        return c.square_length()
