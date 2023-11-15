#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
from json import load, dump, JSONDecodeError
from datetime import datetime


class FileStorage:
    """class responsible for storage of class insatnces
    """
    __file_path = "file.json"
    # attribute that stores the different objects as key value pairs
    __objects = {}

    @property
    def objects(self):
        """the getter function of the objects
        """
        return (self.__objects)

    def all(self):
        """function that returns the dictionary containing the different
        key/values of the different objects
        """
        return (self.__objects)

    def new(self, obj):
        """function that adds to the objects dictionary
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """function that serializes objects to the json file
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as json_file:
            dump(my_dict, json_file)

    def reload(self):
        """checks if a file exists reloads from it if it does
        """
        from .. import base_model
        from .. import user
        from .. import state
        from .. import city
        from .. import amenity
        from .. import place
        from .. import review
        from os.path import exists

        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF-8') as json_file:
                try:
                    tmp = load(json_file)
                    for key, value in tmp.items():
                        if value['__class__'] == "BaseModel":
                            self.__objects[key] = base_model.BaseModel(**value)
                        if value['__class__'] == "User":
                            self.__objects[key] = user.User(**value)
                        if value['__class__'] == "State":
                            self.__objects[key] = state.State(**value)
                        if value['__class__'] == "City":
                            self.__objects[key] = city.City(**value)
                        if value['__class__'] == "Amenity":
                            self.__objects[key] = amenity.Amenity(**value)
                        if value['__class__'] == "Place":
                            self.__objects[key] = place.Place(**value)
                        if value['__class__'] == "Review":
                            self.__objects[key] = review.Review(**value)
                except JSONDecodeError:
                    self.__objects = {}
        else:
            self.__objects = {}
