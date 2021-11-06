#!/usr/bin/python3

from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest
import pycodestyle

FileStorage = file_storage.FileStorage


class Test_style(unittest.TestCase):
    """[Class created to test style and syntax requirements for the
    base_model class]
    """

    def test_pycode(self):
        """[Function that check Syntax from Peep8 branch called pycodestyle]
        """
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/base_model.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")


class TestFileStorage(unittest.TestCase):
    """Testing for FileStorage"""

    def test_dict(self):
        """Test FileStorage __objects"""
        storage = FileStorage()
        dictionary = storage.all()
        self.assertIs(dictionary, storage._FileStorage__objects)
        self.assertEqual(dict, type(dictionary))
