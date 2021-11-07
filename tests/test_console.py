#!/usr/bin/python3
"""[Unittest for base_model]"""
from datetime import date, datetime
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
    @classmethod
    def setUpClass(cls):
        """Setting up a test object"""
        pass

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