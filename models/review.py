#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
from .base_model import BaseModel


class Review(BaseModel):
    """the review class
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """initialises the superclass BaseModel
        """
        super().__init__(self, *args, **kwargs)
