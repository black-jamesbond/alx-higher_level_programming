#!/bin/bash/python3
# square.py
from rectangle import Rectangle

class Square(Rectangle):
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        
                
    @property
    def size(self):
        """
            returns the size of the square
        """

        return self.width

    @size.setter
    def size(self, value):
        """
            sets the value of size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
  
    def update(self, *args, **kwargs):

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass         
            
        
    def __str__(self) -> str:
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width))
        
        


# Square.save_to_file_csv(list_squares_input)

# list_squares_output = Square.load_from_file_csv()

# for square in list_squares_input:
#     print("[{}] {}".format(id(square), square))

# print("---")

# for square in list_squares_output:
#     print("[{}] {}".format(id(square), square))

list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

Base.draw(list_rectangles, list_squares)