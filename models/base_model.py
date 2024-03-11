#!/usr/bin/python3

"""contains the BaseModel class"""

import uuid
import datetime
from models import storage


class BaseModel:
    """Class for the BaseModel (super class)"""

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel class
        Args:
                - *args: list of arguements
                - **kwargs: key/value pair arguements
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.now()
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """returns and saves the updated time"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns the dictionary representation of the Base class"""
        dict_class = self.__dict__
        dict_class["__class__"] = self.__class__.__name__
        dict_class["created_at"] = dict_class["created_at"].isoformat()
        dict_class["updated_at"] = dict_class["updated_at"].isoformat()
        return dict_class

    def __str__(self):
        """returns the string representation of an instance"""
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)
