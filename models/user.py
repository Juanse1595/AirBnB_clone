#!/usr/bin/python3
'''
models/user module
Contains:
    class User
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    Public class attributes:
        +email
        +password
        +first_name
        +last_name
    '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''