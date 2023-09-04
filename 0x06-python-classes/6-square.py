#!/usr/bin/python3
"""6. Coordinates of a square """


class Square:
    """Creating a class called Square that defines a square. """
    def __init__(self, size=0, position=(0, 0)):
        """Using the __init__ method.
        Note:
            Print a square at given coordinates
        Args:
            size: private instance attribute
            position: priviate instance attribute
        """
        self.size = size
        self.position = position

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
            Adding value validation for size
            Account for if size is not an integer
            Account for if size is a negative integer
        Args:
            value: private instance attribute for size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Using private instance method.
        Note:
            Returns the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Using a private instance method.
        Note:
            Adding value validation for position
            Account for if it is not a tuple
            Account for if there are less/more than two items in the tuple
            Account for if the items in the tuple are not integers
            Account for if the items in the tuple are less than zero
        Args:
            value: private instance attribute for position
        """
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(value[0], int) and isinstance(value[1], int)) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] and value[1]) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Using a public instance method.
        Note:
            Prints the square to stdout with #
            Prints space at position
            Account for if size is 0, then print new line
            Account for if position[1] > 0, then don't print space
        """
        if self.__size is 0:
            print()
        else:
            for offset in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for col1 in range(self.__position[0]):
                    print(" ", end="")
                for col2 in range(self.__size):
                    print("#", end="")
                print()
