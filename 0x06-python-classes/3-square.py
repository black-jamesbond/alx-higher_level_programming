#!/usr/bin/python3
# 3-square.py

"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size = 0) -> None:
        """Initialize a new square.

        Args:
            __size (int): The __size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer") 
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            
    def area(self):
        """Return the current area of the square."""
        return self.__size**2
    