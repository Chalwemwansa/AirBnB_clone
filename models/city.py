#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
from .base_model import BaseModel


class City(BaseModel):
    """the City class that inherits from BaseModel
    """
    state_id = ''
    name = ''

    def __init__(self):
        """initialises the super class in the City class
        """
        super().__init__(self)
