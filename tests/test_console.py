#!/usr/bin/python3
"""[Unittest for base_model]"""
from datetime import date, datetime
from os import name
from unittest import TestCase
from models import storage
from models.base_model import BaseModel
import console
import uuid
import pycodestyle
from unittest.mock import patch
from io import StringIO


class Test_style(TestCase):
    """[Class created to test style and syntax requirements for the
    console]
    """

    def test_pycode(self):
        """[Function that check Syntax from Peep8 branch called pycodestyle]
        """
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'console.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")


class Test_console(TestCase):
    """[Class for testing console]"""

    def test_docstring(self):
        """Cheking docstring of console"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_emptyline(self):
        """Testing empty line output"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(console.HBNBCommand().onecmd(""))
            self.assertEqual(f.getvalue().strip(), '')

    def test_quit(self):
        """Testing quit method"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        """Testing EOF method"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), '\n')

    def test_all(self):
        """Testing all method"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("all BaseModel")
            self.assertIn('["[BaseModel] (', f.getvalue())

    def test_create(self):
        """Testing create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create BaseModel")
        key_id = 'BaseModel.' + f.getvalue().split('\n')[0]
        objects = storage.all()
        self.assertIn(key_id, objects)

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("create whatever")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """Testing show method"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show whatever")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseModel 123")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        base1 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("show BaseModel " + base1.id)
        base1_str = "[BaseModel] ({})".format(base1.id)
        self.assertIn(base1_str, f.getvalue())

    def test_destroy(self):
        """Test for destroy method"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy whatever")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("destroy BaseModel 123")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

    def test_update(self):
        """Test for update method"""
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("update whatever")
        self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel")
        self.assertEqual(f.getvalue(), "** instance id missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel 123")
        self.assertEqual(f.getvalue(), "** no instance found **\n")

        b2 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel {}".format(b2.id))
        self.assertEqual(f.getvalue(), "** attribute name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("update BaseModel {}".format(b2.id)
                                         + " name")
        self.assertEqual(f.getvalue(), "** value missing **\n")

    def test_count(self):
        """Testing count method"""
        counter = 0
        for obj in storage.all().values():
            if "BaseModel" == obj.__class__.__name__:
                counter += 1
        with patch('sys.stdout', new=StringIO()) as f:
            console.HBNBCommand().onecmd("count BaseModel")
        self.assertEqual(f.getvalue(), str(counter) + '\n')


class Test_console_command_help(TestCase):
    """[Unnites HBnB console dedicated to help function]
    """

    def test_help_method(self):
        """[Testing help]
        """
        expected = """Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update"""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help"))
            self.assertEqual(o.getvalue().strip(), expected)

    def test_help_quit_method(self):
        """[Testing help EOF]
        """
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help EOF"))
            self.assertEqual(o.getvalue().strip(),
                             "exits the program with a new line printed")

    def test_help_all_method(self):
        """[Testing help all]
        """
        e = """Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all."""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help all"))
            self.assertEqual(o.getvalue().strip(), e)

    def test_help_count_method(self):
        """[Testing help count]
        """
        e = """[ retrieve the number of instances of a class:
        <class name>.count().]"""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help count"))
            self.assertEqual(o.getvalue().strip(), e)

    def test_help_create_method(self):
        """[Testing help create]
        """
        e = """Create an instance of given class, prints its id and saves
        it into de json file"""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help create"))
            self.assertEqual(o.getvalue().strip(), e.strip())

    def test_help_destroy_method(self):
        """[Testing help destroy]
        """
        e = """Deletes an instance based on its id"""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help destroy"))
            self.assertEqual(o.getvalue().strip(), e.strip())

    def test_help_help_method(self):
        """[Testing help help]
        """
        e = """List available commands with "help" """
        e += """or detailed help with "help cmd"."""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help help"))
            self.assertEqual(o.getvalue().strip(), e.strip())

    def test_help_quit_method(self):
        """[Testing help quit]
        """
        e = """exits the program"""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help quit"))
            self.assertEqual(o.getvalue().strip(), e.strip())

    def test_help_show_method(self):
        """[Testing help show]
        """
        e = """Prints the string representation of an instance
        based on the class name and id"""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help show"))
            self.assertEqual(o.getvalue().strip(), e.strip())

    def test_help_update_method(self):
        """[Testing help update]
        """
        e = """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)."""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help update"))
            self.assertEqual(o.getvalue().strip(), e.strip())

    def test_help_none_implemented_method(self):
        """[Testing help none_implemented]
        """
        e = """*** No help on lkdfdfgjk"""
        with patch("sys.stdout", new=StringIO())as o:
            self.assertFalse(console.HBNBCommand().onecmd("help lkdfdfgjk"))
            self.assertEqual(o.getvalue().strip(), e.strip())
