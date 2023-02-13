#!/bin/bash/python3
# base.py
import csv
import json
import turtle 

class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """
    __nb_object = 0
    
    def __init__(self, id = None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
    
    @staticmethod
    def to_json_string(list_dictionary):
        if list_dictionary == None:
            return []
        return json.dumps(list_dictionary)
    
    @classmethod
    def save_to_file(cls,list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs == None:
                jsonfile.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
    
    @staticmethod
    def from_json_string(json_string):
        if json_string == None:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
        
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        result = []
        try:
            with open(filename, 'r') as jsonfile:
                conv_json = Base.from_json_string(jsonfile.read())
                return [cls.create(**i) for i in conv_json]
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__+'.csv'
        with open(filename, 'w', newline="") as file:
            if list_objs == None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    fieldname = ['id', 'width', 'height', 'x','y']
                else:
                    fieldname = ["id", "size", "x", "y"]
                
                csv_writer = csv.DictWriter(file, fieldnames=fieldname)
                csv_writer.writeheader()
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())
                    
    @classmethod
    def load_from_file_csv(cls):
        # result = []
        # filename = cls.__name__+'.csv'
        # with open(filename, 'r') as file:
        #     csv_reader = csv.DictReader(file)
        #     return[cls.create(**i) for i in csv_reader]
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
            
    @staticmethod
    def draw (list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
                