#!/usr/bin/python3
"""[Module of HBnB console]"""

import cmd
from models.base_model import BaseModel


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
        if input_class == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)

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
