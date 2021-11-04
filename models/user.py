#!/usr/bin/python3
"""[models/user module for HBnB Holberton's project]
    """
from models.base_model import BaseModel


class User(BaseModel):
    """[User class]
    inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
