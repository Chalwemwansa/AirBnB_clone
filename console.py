#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from json import loads, dumps


class HBNBCommand(cmd.Cmd):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    the command interpreter for the AirBnb clone project
    """
    prompt = "(hbnb) "
    __my_classes = ["BaseModel", "User", "State", "City\
", "Amenity", "Place", "Review"]

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """creates an instance of an object
        """
        my_list = line.split()
        if not line:
            print("** class name missing **")
        elif my_list[0] not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        else:
            if my_list[0] == "BaseModel":
                my_obj = BaseModel()
            elif my_list[0] == "User":
                my_obj = User()
            elif my_list[0] == "Place":
                my_obj = Place()
            elif my_list[0] == "State":
                my_obj = State()
            elif my_list[0] == "City":
                my_obj = City()
            elif my_list[0] == "Amenity":
                my_obj = Amenity()
            elif my_list[0] == "Review":
                my_obj = Review()
            else:
                my_obj = null
            my_obj.save()
            print(my_obj.id)

    def do_show(self, line):
        """shows the different instances and their attributes
        """
        my_list = line.split(' ')
        if not line:
            print('** class name missing **')
        elif my_list[0] not in HBNBCommand.__my_classes:
            print('** class doesn\'t exist **')
        elif len(my_list) == 1:
            print('** instance id missing **')
        else:
            flag = 0
            comp = f"{my_list[0]}.{my_list[1]}"
            for key in storage.all().keys():
                if key == comp:
                    flag = 1
                    print(storage.all()[key])
                    break
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, line):
        """deletes a specified class key object from the json_file
        """
        my_list = line.split(' ')
        if not line:
            print('** class name missing **')
        elif my_list[0] not in HBNBCommand.__my_classes:
            print('** class doesn\'t exist **')
        elif len(my_list) == 1:
            print('** instance id missing **')
        else:
            flag = 0
            comp = f"{my_list[0]}.{my_list[1]}"
            my_dict = storage.objects
            for key in my_dict.keys():
                if key == comp:
                    flag = 1
                    del my_dict[key]
                    break
            if flag == 0:
                print('** no instance found **')

    def do_all(self, line):
        """displays all the objecs in the json_file
        """
        flag = 0
        if not line:
            pass
        elif line:
            flag = 1
            my_list = line.split(' ')
            if my_list[0] not in HBNBCommand.__my_classes:
                print('** class doesn\'t exist **')
                flag = 2
        if not flag == 2:
            my_dict = storage.objects
            for key, value in my_dict.items():
                if flag == 1:
                    if value['__class__'] == my_list[0]:
                        print(storage.all()[key])
                else:
                    print(storage.all()[key])

    def do_update(self, line):
        """updates the objects in the file
        update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        my_list = line.split(' ')
        length = len(my_list)
        if not line:
            print('** class name missing **')
        elif line:
            if my_list[0] not in HBNBCommand.__my_classes:
                print('** class doesn\'t exist **')
            else:
                if length == 1:
                    print('** instance id missing **')
                if length > 1:
                    flag = 0
                    comp = f"{my_list[0]}.{my_list[1]}"
                    for key in storage.all().keys():
                        if key == comp:
                            flag = 1
                    if flag == 0:
                        print('** no instance found **')
                    else:
                        pass
                if length == 2:
                    print('** attribute name missing **')
                if length == 3:
                    print('** value missing **')
                elif length > 3:
                    my_dict = storage.objects
                    if my_list[3].startswith('"'):
                        mine = my_list[3].split('"')[1]
                    elif my_list[3].startswith("'"):
                        mine = my_list[3].split("'")[1]
                    else:
                        mine = my_list[3]
                    my_dict[comp][my_list[2]] = mine
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
