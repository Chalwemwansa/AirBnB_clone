#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'
"""
import cmd
import fnmatch
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

    def default(self, line):
        my_list = line.split('.')
        if len(my_list) > 1:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            if my_list[1] == "count()":
                if my_list[0] not in HBNBCommand.__my_classes:
                    print("** class doesn't exist **")
                else:
                    count = 0
                    for key in storage.all().keys():
                        comp, other = key.split('.')
                        if comp == my_list[0]:
                            count += 1
                    print(count)
            if fnmatch.fnmatchcase(line, "*.show(*)"):
                self.do_show(HBNBCommand.__get_line(line))
            if fnmatch.fnmatchcase(line, "*.destroy(*)"):
                self.do_destroy(HBNBCommand.__get_line(line))
            if fnmatch.fnmatchcase(line, "*.update(*)"):
                class_name = my_list[0]
                str = my_list[1].split('(')
                str = str[1].split(')')
                str = str[0].split(',')
                for key in str:
                    tmp = key.split('"')
                    class_name += f" {tmp[1]}"
                self.do_update(class_name)

    def __get_line(line):
        my_list = line.split('.')
        str_list = my_list[1].split('(')
        str_list = str_list[1].split(')')
        if str_list[0] == '':
            return my_list[0]
        else:
            return f"{my_list[0]} {str_list[0]}"
        return (new_list)

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
        my_list = line.split(' ')
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
                    storage.save()
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
            new_list = []
            if flag == 1:
                for key, value in storage.all().items():
                    cmp, x = key.split('.')
                    if (cmp == my_list[0]):
                        new_list.append(str(value))
            if flag == 0:
                for value in storage.all().values():
                    new_list.append(str(value))
            print(new_list)

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
                elif length > 3 and not flag == 0:
                    obj = storage.all()[comp]
                    if my_list[3].startswith('"'):
                        mine = my_list[3].split('"')[1]
                    elif my_list[3].startswith("'"):
                        mine = my_list[3].split("'")[1]
                    else:
                        mine = my_list[3]
                    setattr(obj, my_list[2], mine)
                    obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
