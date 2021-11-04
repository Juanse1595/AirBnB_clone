#!/usr/bin/python3
"""[Module of HBnB console]"""

import cmd
from models.base_model import BaseModel
from models import storage
import shlex

classes = {'BaseModel', 'TestModel'}


class HBNBCommand(cmd.Cmd):
    """[Class to implement HolbertonBnB console]

    Args:
        prompt ([str]): [Prompt to show]

    Returns:
        [type]: [infinite loop]
    """
    prompt = "(hbnb) "

    def do_create(self, args):
        """[Create an instance of BaseModel, prints its id and saves
        it into de json file]
        """
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

    def do_destroy(self, args):
        """[Deletes an instance based on its id]
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
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances based
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
