#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
from .base_model import BaseModel


class State(BaseModel):
    """class that defines the state and is a subclass of BaseModel
    """
    name = ''

    def __init__(self, *args, **kwargs):
        """initialises the super class
        """
        super().__init__(self, *args, **kwargs)
