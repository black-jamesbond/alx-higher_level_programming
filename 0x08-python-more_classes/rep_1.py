class Rectangle:
    
    def __init__(self, height = 0, width = 0) -> None:
        self.__height = height
        self.__width = width
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value):
        if type(value) not in(int, float):
            raise TypeError("height must be an a digit")
        
        elif value < 0:
            raise ValueError("the value of the height must not be less than 0")
        else:
            self.__height = value
            
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) not in (int, float):
            raise TypeError("width must be an a digit")
        
        elif value < 0:
            raise ValueError("the value of the width must not be less than 0")
        else:
            self.__width = value
    
    def area(self):
        return self.__width * self.__height
    
    def parameter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        parameter = (2*self.__height) + (2*self.__width)
        return parameter
    
    def display(self):
        i = self.__height
        j = self.__width
        
        # if self.__height == 0 or self.__width == 0:
        #     print("omo i cant print this rect ooo something dey miss")
        # for i in self.__height:
        #     print("#"*self.__width)
    
    
_1st_rectangle = Rectangle()

_1st_rectangle.height = int(input("what is the height of the rectangle "))
_1st_rectangle.width = int(input("what is the width of the rectangle "))

print("the area of the rect is {}".format(_1st_rectangle.area))
print("the parameter of the rect is {}".format(_1st_rectangle.parameter))
print("this is your rectangle \n {}".format(_1st_rectangle.display))

_1st_rectangle.display()