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
        if kwargs:
            for key, value in kwargs.items():
                if key != "created_at" and key != "updated_at":
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self) -> str:
        """[Changing the str method expected output to :
        [<class name>] (<self.id>) <self.__dict__>]

        Returns:
            str: [description with the information changed]
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """[Function that updates the update_date]
        """
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """[Function that returns an specific information about the class in a dict]

        Returns:
            [dict]: [The atttributes with the format required]
        """
        copy = self.__dict__.copy()
        copy["__class__"] = self.__class__.__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()
        return copy
