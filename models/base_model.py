#!/usr/bin/python3
"""[Base model module for HBnB Holberton's project]
    """
import uuid
import datetime


class BaseModel:
    """[BaseModel class for the HBnB Holberton's project]
    """

    def __init__(self, *args, **kwargs) -> None:
        """[Constructor that initialize a new instance of BaseModel]
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = datetime.datetime.today()

    def __str__(self) -> str:
        """[Changing the str method expected output to : 
        [<class name>] (<self.id>) <self.__dict__>]

        Returns:
            str: [description with the information changed]
        """
        return f"[{self.__class__.__name__}]({self.id} {self.__dict__})"

    def save(self):
        """[Function that updates the update date]
        """
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        pass
