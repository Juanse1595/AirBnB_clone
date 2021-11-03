#!/usr/bin/python3
"""[Module of HBnB console]"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex

classes = {'BaseModel'}


class HBNBCommand(cmd.Cmd):
    """[Class to implement HolbertonBnB console]

    Args:
        prompt ([str]): [Prompt to show]

    Returns:
        [type]: [infinite loop]
    """
    prompt = "(hbnb) "

    def do_create(self, input_class):
        """[Create an instance of BaseModel, prints its id and saves
        it into de json file]
        """
        if not input_class:
            print("** class name missing **")
            return
        if input_class not in classes:
            print("** class doesn't exist **")
            return
        if input_class and input_class == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """[ Prints the string representation of an instance 
        based on the class name and id]
        """
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

    def emptyline(self) -> bool:
        """[shouldn’t execute anything]
        """
        pass

    def do_quit(self, arg):
        """[exits the program]

        Args:
            arg ([str]): [Arguments to the console]

        Returns:
            [boolean]: [True]
        """
        return True

    def do_EOF(self, arg):
        """[exits the program]

        Args:
            arg ([str]): [Arguments to the console]

        Returns:
            [boolean]: [True]
        """
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
