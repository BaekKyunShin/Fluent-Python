import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__=="__main__":
    vec1 = Vector(3, 4)
    vec2 = Vector(2, 1)
    print(vec1) # __repr__()
    print(vec1 + vec2) # __add__()
    print(vec1 * 3) # __mul__()
    print(abs(vec1)) # __abs__()
    print(bool(vec1)) # __bool__(), __bool__()이 없다면 __len__()을 참조하고 0이면 False, 그 외는 True 반환
    

