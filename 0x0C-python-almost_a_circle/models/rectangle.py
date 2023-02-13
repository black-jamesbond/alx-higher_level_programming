#!/bin/bash/python3
# rectangle.py
import csv
from base import Base
import json


class Rectangle(Base):
    """ represents the rectangle model

    Args:
        Base (_type_): _description_
        
    ATTRIBUTE:
    __width(int): the width of the rectangle.
    __height(int): the height of the rectangle.
    __x(int): is x
    __y(int): is y
    """
    def __init__(self, width, height, x = 0, y = 0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        
    @property
    def width(self):
        """ this is the getter function for width

        Returns:
            the width of the rectangle
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ This is the setter function for width if sets the value of self.__width
        
        Args:
            value (int): the value of the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0 :
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """ this is the getter function for height
        
        Returns:
            the height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ This is the setter function for width if sets the value of self.__height
        
        Args:
            value (int): the value of the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0 :
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def x(self):
        """
            getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x.
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """this calculate the area of the rectangle

        Returns:
            area (int): the area of the rectangle
        """
        return self.__width * self.__height
    
    def display(self):
        Rectangle = ""
        print_symbol = "#"
        
        print("\n" * self.__y, end = "")
        
        for i in range(self.__height):
            Rectangle += (" " * self.__x) + (print_symbol * self.__width) + "\n"
        print(Rectangle, end="")
            
    def __str__(self) -> str:
        """prints the details of the rectangle

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[{}]({}) {}/{} - {}/{}".format(type(self).__name__,self.id,self.__x,self.__y,self.__width,self.__height))

    def update(self, *args, **kwargs):
        
        if len(args) == 0:
            for key,value in kwargs.items():
                self.__setattr__(key, int(value))
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2] 
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        return {'x': getattr(self,'x'),'y':getattr(self,'y'), 'id': getattr(self,'id'),'height':getattr(self,'height'), 'width':getattr(self,'width')}
    

