from __future__ import annotations


class Vektor:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    def __add__(self, other: float) -> Vektor:
        return Vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other: float) -> Vektor:
        return Vektor(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int) -> Vektor:
        return Vektor(self.x * scalar, self.y * scalar)

v1 = Vektor(3.5, 2)
v2 = Vektor(5.7, 4.1)

print(v1 + v2)
print(v1 - v2)
print(v1 * 4)
