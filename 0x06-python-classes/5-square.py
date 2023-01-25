#!/usr/bin/python3
# 5-square.py

"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size = 0) -> None:
        """Initialize a new square.

        Args:
            __size (int): The __size of the new square.
        """
        self.__size = size
        
    @property
    def size(self):
        """Get/set the current __size of the square."""
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0 :
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        
    def area(self):
        """Return the current area of the square."""
        return self.__size**2
    
    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#"*self.__size)
        