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
        my_dict = self.__objects.copy()
        if self.__objects:
            for key, value in self.__objects.items():
                tmp = (key, value.copy())
                tmp[1]['created_at'] = datetime.strptime(value["created_at\
"], "%Y-%m-%dT%H:%M:%S.%f")
                tmp[1]['updated_at'] = datetime.strptime(value["updated_at\
"], "%Y-%m-%dT%H:%M:%S.%f")
                my_dict[tmp[0]] = f"[\
{tmp[1]['__class__']}] ({tmp[1]['id']}) {tmp[1]}"
        return (my_dict)

    def new(self, obj):
        """function that adds to the objects dictionary
        """
        self.__objects[f"{obj.__class__.name}.{obj.id}"] = obj

    def save(self):
        """function that serializes objects to the json file
        """
        with open(self.__file_path, 'w', encoding='UTF-8') as json_file:
            dump(self.__objects, json_file)

    def reload(self):
        """checks if a file exists reloads from it if it does
        """
        from os.path import exists
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='UTF-8') as json_file:
                try:
                    self.__objects = load(json_file)
                except JSONDecodeError:
                    self.__objects = {}
        else:
            self.__objects = {}
