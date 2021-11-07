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
            console.HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue(), '')

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
