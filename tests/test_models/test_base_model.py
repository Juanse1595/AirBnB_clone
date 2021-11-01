#!/usr/bin/python3

from unittest import TestCase
from models import base_model
import pycodestyle


class Test_style(TestCase):
    """[Class created to test style and syntax requirements for base_model class]
    """

    def test_pycode(self):
        """[Function that check Syntax from Peep8 branch called pycodestyle]
        """
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/base_model.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")
