#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    the Amenity class that inherits from the BaseModel class
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        initialises the BaseModel
        """
        super().__init__(self, *args, **kwargs)
