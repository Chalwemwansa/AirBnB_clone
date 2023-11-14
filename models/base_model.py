#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    the base class where all other classes inherit from
    """

    def __init__(self, *args, **kwargs):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        initialises the instance attributes
        """
        if kwargs:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], "\
%Y-%m-%dT%H:%M:%S.%f")
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], "\
%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if not key == "__class__":
                    setattr(self, key, value)
        if args:
            pass

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        prints an object in the format
            [<class name>] (<self.id>) <self.__dict__>
        """
        my_str = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return (my_str)

    def save(self):
        """python3 -c 'print(__import__("my_module").MyClass.my_function
        a public instance method that updates the updated at attribuute
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        return a dictionary containing all the key/values
        of the instance method
        """
        tmp = ("__class__", self.__class__.__name__)
        my_dict = {}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict[tmp[0]] = tmp[1]
        return (my_dict)
