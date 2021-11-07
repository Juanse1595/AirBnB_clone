#!/usr/bin/python3
"""[Module hat containts the TestFileStorage Class]
    """
from typing import Type
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
import models
import inspect

FileStorage = file_storage.FileStorage
classes = {BaseModel, User, Place, State, City, Amenity, Review}


class Test_style(unittest.TestCase):
    """[Class created to test style and syntax requirements for the
    base_model class]
    """
    @classmethod
    def setUpClass(cls) -> None:
        """[list the functions to docstring test]
        """
        cls.methods_ds = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pycode(self):
        """[Function that check Syntax from Peep8 branch called pycodestyle]
        """
        foo = pycodestyle.StyleGuide(quiet=True).check_files([
            'models/base_model.py'])
        self.assertEqual(foo.total_errors, 0,
                         "Found code style error (and warnings).")

    def test_docstring(self):
        """[Function to test docstring of the class and the module]
        """
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertIsNot(FileStorage.__doc__, None,
                         "class needs a docstring")
        self.assertTrue(len(file_storage.__doc__) > 0,
                        "file_storage.py needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) > 0,
                        "class needs a docstring")
        for method in self.methods_ds:
            self.assertIsNot(method[1].__doc__, None,
                             f"{method[0]} needs docstring")
            self.assertTrue(len(method[1].__doc__) >
                            0, f"{method[0]} needs docstring")


class TestFileStorage(unittest.TestCase):
    """Testing for FileStorage"""

    def test_all(self):
        """Test all method"""
        storage = FileStorage()
        dictionary = storage.all()
        self.assertIs(dictionary, storage._FileStorage__objects)
        self.assertEqual(dict, type(dictionary))

    def test_new(self):
        """ Testing new method
        """
        main_instance = FileStorage
        base_model = BaseModel()
        self.assertIn("{}.{}".format(base_model.__class__.__name__,
                      base_model.id), models.storage.all().keys())
        amenity = Amenity()
        self.assertIn("{}.{}".format(amenity.__class__.__name__,
                      amenity.id), models.storage.all().keys())
        user = User()
        self.assertIn("{}.{}".format(user.__class__.__name__,
                      user.id), models.storage.all().keys())
        state = State()
        self.assertIn("{}.{}".format(state.__class__.__name__,
                      state.id), models.storage.all().keys())
        city = City()
        self.assertIn("{}.{}".format(city.__class__.__name__,
                      city.id), models.storage.all().keys())
        place = Place()
        self.assertIn("{}.{}".format(place.__class__.__name__,
                      place.id), models.storage.all().keys())
        review = Review()
        self.assertIn("{}.{}".format(review.__class__.__name__,
                      review.id), models.storage.all().keys())

        new_file_storage = FileStorage()
        back_up, FileStorage._FileStorage__objects\
            = FileStorage._FileStorage__objects, {}
        dictionary = {}

        for value in classes:
            with self.subTest(value=value):
                new_instance = value()
                key = f"{new_instance.__class__.__name__}.{new_instance.id}"
                new_file_storage.new(new_instance)
                dictionary[key] = new_instance
                self.assertEqual(
                    dictionary, new_file_storage._FileStorage__objects)
        FileStorage._FileStorage__objects = back_up

    def test_new_without_args(self):
        """[Testing when not arguments provided]"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), '10')
        with self.assertRaises(TypeError):
            models.storage.new(Amenity(), '10')
        with self.assertRaises(TypeError):
            models.storage.new(User(), '10')
        with self.assertRaises(TypeError):
            models.storage.new(State(), '10')
        with self.assertRaises(TypeError):
            models.storage.new(City(), '10')
        with self.assertRaises(TypeError):
            models.storage.new(Place(), '10')

    def test_new_With_None(self):
        """[Testing when is provided a None to .all method]
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_save(self):
        """[Test implementation of save after new]
        """
        base_model = BaseModel()
        models.storage.new(base_model)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        place = Place()
        models.storage.new(place)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        models.storage.save()

        with open("file.json", mode="r", encoding="utf-8") as f:
            read_1 = f.read()
            self.assertIn(f"BaseModel.{base_model.id}", read_1)
            self.assertIn(f"User.{user.id}", read_1)
            self.assertIn(f"State.{state.id}", read_1)
            self.assertIn(f"Place.{place.id}", read_1)
            self.assertIn(f"City.{city.id}", read_1)
            self.assertIn(f"Amenity.{amenity.id}", read_1)
            self.assertIn(f"Review.{review.id}", read_1)

    def test_save_With_None(self):
        """[Test when is provided a None to .save method]
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        """[Test implementation of reload after new + save]
        """
        base_model = BaseModel()
        models.storage.new(base_model)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        place = Place()
        models.storage.new(place)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel.{base_model.id}", objects)
        self.assertIn(f"User.{user.id}", objects)
        self.assertIn(f"State.{state.id}", objects)
        self.assertIn(f"Place.{place.id}", objects)
        self.assertIn(f"City.{city.id}", objects)
        self.assertIn(f"Amenity.{amenity.id}", objects)
        self.assertIn(f"Review.{review.id}", objects)

    def test_reload_With_None(self):
        """[Test when is provided a None to .save method]
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)
