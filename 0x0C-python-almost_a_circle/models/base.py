#!/usr/bin/python3

class Base:
    """
    Base class for managing id attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): If provided, assigns the id as the instance attribute.
                       Otherwise, increments __nb_objects and assigns the new value to the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
