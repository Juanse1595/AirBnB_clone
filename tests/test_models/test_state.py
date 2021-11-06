#!/usr/bin/python3

"""[Unittest for state]
    """
from datetime import date, datetime
from unittest import TestCase
from models import state
import uuid
import pycodestyle
State = state.State


class Test_style(TestCase):
    """[Class created to test style and syntax requirements for the
    state class]
    """

    def test_pycode(self):
        """[Function that check Syntax from Peep8 branch called pycodestyle]
        """
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/state.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")


class Test_state(TestCase):
    """[Class for testing all the function of state class]
    """
    @classmethod
    def setUpClass(cls):
        """Setting up a test object"""
        cls.state1 = State()

    def test_empty_state(self):
        """[Testing if instance is correcty related]
        """
        self.assertIsNotNone(self.state1)
        self.assertIsInstance(self.state1, State)

    def test_id_value(self):
        """[Cheking if id is an uuid version 4]
        """
        state_test2 = State(id='1')
        with self.assertRaises(ValueError) as _:
            uuid.UUID(state_test2.id, version=4)
        state_test3 = State(id=['1'])
        with self.assertRaises(AttributeError) as _:
            uuid.UUID(state_test3.id, version=4)

    def test_dates(self):
        """[Cheking dates are correctly created]
        """
        self.assertIsInstance(self.state1.created_at, datetime)
        self.assertIsInstance(self.state1.updated_at, datetime)

    def test__str__(self):
        """[Cheking correct output when printing]"""
        id1 = self.state1.id
        self.assertTrue(f'[State] ({id1})' in str(self.state1))

    def test_save(self):
        """Checks if updated_at is changed with save method"""
        self.state1.save()
        self.assertNotEqual(self.state1.updated_at,
                            self.state1.created_at)

    def test_to_dict(self):
        """Checks to_dict method"""
        state_test4 = State()
        dict_state4 = state_test4.to_dict()
        self.assertIsInstance(dict_state4, dict)
        self.assertIsInstance(dict_state4['created_at'], str)
        self.assertIsInstance(dict_state4['updated_at'], str)

    def test_attributes(self):
        """Checks correct attributes assignment"""
        state5 = State(name = 'California')
        self.assertEqual(state5.name, 'California')
