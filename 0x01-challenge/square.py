#!/usr/bin/python3
"""Module for class square"""


class Square():
    """Square Class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Instantiation of the class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.width * 2)

    def __str__(self):
        """Print the square"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    """Create a square Object"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
