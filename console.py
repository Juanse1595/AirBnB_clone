#!/usr/bin/python3
"""[Module of HBnB console]"""

import cmd


class HBNBCommand(cmd.Cmd):
    """[Class to implement HolbertonBnB console]

    Args:
        prompt ([str]): [Prompt to show]

    Returns:
        [type]: [infinite loop]
    """
    prompt = "(hbnb) "

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
