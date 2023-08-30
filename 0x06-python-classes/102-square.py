#!/usr/bin/python3
""" 9. Compare 2 squares """


class Square(object):
    """ Creating a class called Square that defines a square. """
    def __init__(self, size=0):
        """ Using the __init__ method.
        Args:
            size: private instance attribute for the class
        """
        self.size = size

    def area(self):
        """ Using a public instance method.
        Note:
            Area = bh
            Returns the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Using a private instance method.
        Note:
            Returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Using a private instance method.
        Note:
            Adding value validation
            Account for if size is not an integer
            Account for if size is a negative integer
        Args:
            value: private instance attribute for size
        """
        if (isinstance(value, int) or isinstance(value, float)) is False:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """ For x < y
        Args:
            other: comparison magic method
        """
        return self.__size < other.__size

    def __le__(self, other):
        """ For x <= y
        Args:
            other: comparison magic method
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """ For x == y
        Args:
            other: comparison magic method
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """ For x != y or x <> y
        Args:
            other: comparison magic method
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """ For x > y
        Args:
            other: comparison magic method
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """ For x >= y
        Args:
            other: comparison magic method
        """
        return self.__size >= other.__size
