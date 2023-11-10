#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
from .base_model import BaseModel

class User(BaseModel):
    """class that inherits from base_model
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__(self)
