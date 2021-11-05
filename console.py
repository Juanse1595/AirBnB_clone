#!/usr/bin/python3
"""[Module of HBnB console]"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex

classes = {'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review'}


class HBNBCommand(cmd.Cmd):
    """[Class to implement HolbertonBnB console]

    Args:
        prompt ([str]): [Prompt to show]

    Returns:
        [type]: [infinite loop]
    """
    prompt = "(hbnb) "

    def do_create(self, args):
        """Create an instance of given class, prints its id and saves
        it into de json file"""
        args = shlex.split(args)
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        obj = eval(args[0])()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        inputs = shlex.split(args)
        if not inputs:
            print('** class name missing **')
        elif inputs[0] not in classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif '{}.{}'.format(inputs[0], inputs[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = '{}.{}'.format(inputs[0], inputs[1])
            content = storage.all()[key]
            print(content)

    def do_destroy(self, args):
        """Deletes an instance based on its id"""
        inputs = shlex.split(args)
        if not inputs:
            print('** class name missing **')
        elif inputs[0] not in classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        elif '{}.{}'.format(inputs[0], inputs[1]) not in storage.all():
            print("** no instance found **")
        else:
            key = '{}.{}'.format(inputs[0], inputs[1])
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all. """
        args = shlex.split(args)
        dict_1 = storage.all()

        if not args:
            print(["".join(str(value)) for value in dict_1.values()])
            return
        if args[0] in classes:
            print([str(value) for key, value in dict_1.items()
                  if key.split(".")[0] == args[0]])
            return
        print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""

        integers = {'number_rooms', 'number_bathrooms',
                    'max_guest', 'price_by_night'}
        floats = {'latitude', 'longitude'}
        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            key = '{}.{}'.format(args[0], args[1])
            dict_1 = storage.all()
            content = dict_1[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            if args[2] in floats:
                try:
                    args[3] = float(args[3])
                except ValueError:
                    args[3] = 0.0
            if args[2] in integers:
                try:
                    args[3] = int(args[3])
                except ValueError:
                    args[3] = 0
            setattr(content, args[2], args[3])
            """ content.__dict__[args[2]] = args[3] """
            content.save()
        except KeyError:
            print("** no instance found **")
            return

    def emptyline(self) -> bool:
        """shouldn’t execute anything"""
        pass

    def do_quit(self, arg):
        """exits the program"""
        return True

    def do_EOF(self, arg):
        """exits the program with a new line printed"""
        print("")
        return True

    def default(self, line):
        """[Implements <>.method sintax]
        """
        args = line.split('.')
        string = "self.do_"
        if args[1] == 'all()':
            string += "all('" + args[0] + "')"
            eval(string)
        elif 'show' in args[1]:
            id_inline = line.split('"')
            string += "show('" + args[0] + " " + id_inline[1] + "')"
            eval(string)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
