#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
from .base_model import BaseModel


class Place(BaseModel):
    """the Place class that defines the place
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self):
        """initialises the superclass (BaseModel)
        """
        super().__init__(self)
