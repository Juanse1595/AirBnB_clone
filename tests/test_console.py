#!/usr/bin/python3
"""[Unittest for base_model]"""
from datetime import date, datetime
from unittest import TestCase
from models import base_model
import uuid
import pycodestyle


class Test_style(TestCase):
    """[Class created to test style and syntax requirements for the
    console]
    """

    def test_pycode(self):
        """[Function that check Syntax from Peep8 branch called pycodestyle]
        """
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/base_model.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")


class Test_console(TestCase):
    """[Class for testing console]"""
    @classmethod
    def setUpClass(cls):
        """Setting up a test object"""
        pass
