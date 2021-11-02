#!/usr/bin/python3

"""[Unittest for base_model]
    """
from datetime import datetime
from unittest import TestCase
from models import base_model
import uuid
import pycodestyle
BaseModel = base_model.BaseModel


class Test_style(TestCase):
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

class Test_base(TestCase):
    """[Class for testing all the function of base class]
    """
    @classmethod
    def setUpClass(cls):
        cls.base_test1 = BaseModel()

    def test_empty_base(self):
        """[Testing if instance is correcty related]
        """
        self.assertIsNotNone(self.base_test1)
        self.assertIsInstance(self.base_test1, BaseModel)

    def test_id_value(self):
        """[Cheking if id is an uuid version 4]
        """
        base_test2 = BaseModel(id='1')
        with self.assertRaises(ValueError) as _:
            uuid.UUID(base_test2.id, version=4)
        base_test3 = BaseModel(id=['1'])
        with self.assertRaises(AttributeError) as _:
            uuid.UUID(base_test3.id, version=4)

    def test_dates(self):
        """[Cheking dates are correctly created]
        """
        self.assertIsInstance(self.base_test1.created_at, datetime)
        self.assertIsInstance(self.base_test1.updated_at, datetime)
    
    def test__str__(self):
        """[Cheking correct output when printing]
        """