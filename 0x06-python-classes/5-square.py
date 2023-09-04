#!/usr/bin/python3
"""5. Printing a square """


class Square:
    """Creating a class called Square that defines a square. """
    def __init__(self, size=0):
        """Using the __init__ method.
        Note:
            Account for if size is not an integer
            Account for if size is a negative integer
        Args:
            size: private instance attribute for my_square
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Using a public instance method.
        Note:
            Area = bh
            Returns the current square area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Using a private instance method.
        Note:
            Returns the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Using a private instance method.
        Note:
            Adding value validation
        Args:
            value: private instance attribute for size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Using a public instance method.
        Note:
            Prints the square to stdout with #
            Account for if size is 0, then print new line
        """
        if self.__size is 0:
            print()
        else:
            for row in range(self.__size):
                for col in range(self.__size):
                    print("#", end="")
                print()
