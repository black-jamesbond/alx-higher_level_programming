#!/usr/bin/python3
# 6-square.py
"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size = 0, position = (0, 0)) -> None:
        """Initialize a new square.

        Args:
            __size (int): The __size of the new square.
            position (int, int): The position of the new square.
        """
        self.__size = size
        self.__position = position
    
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
            
    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            
    def area(self):
        """Return the current area of the square."""
        return self.__size**2
    
    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return
        
        [print("") for i in range(0, self.position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
                