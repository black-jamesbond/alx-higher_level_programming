#!/usr/bin/python
# 1-python.py

"""Define a class called Square"""


class Square:
    """Initializing a Square"""
   
    def __init__(self, size) -> None:
        """Intialize a new square
         Args:
            size (int): The size of the new square.
        """
        self.__size = size
        
        