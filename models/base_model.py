#!/usr/bin/python3

"""contains the BaseModel class"""

import uuid
import datetime
from models import storage


class BaseModel:
    """Class for the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel class
        Args:
                - *args: list of arguements
                - **kwargs: key/value pair arguements
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        self.__dict__[key] = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now().isoformat()
            storage.new(self)

    def save(self):
        """returns and saves the updated time"""
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns the dictionary representation of the Base class"""
        dict_class = self.__dict__.copy()
        dict_class["__class__"] = self.__class__.__name__
        dict_class["created_at"] = dict_class["created_at"].isoformat()
        dict_class["updated_at"] = dict_class["updated_at"].isoformat()
        return dict_class

    def __str__(self):
        """returns the string representation of an instance"""
        cls_name = __class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
