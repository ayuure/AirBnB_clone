#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs != {} and kwargs != None:
            for attr, value in kwargs.items():
                if attr == "created_at" or attr == "updated_at":
                    setattr(self, attr, datetime.isoformat(value))
                else:
                    self.__dict__[attr] = value

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.save()

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_class = self.__dict__.copy()
        dict_class["__class__"] = self.__class__.__name__
        dict_class["created_at"] = dict_class["created_at"].isoformat()
        dict_class["updated_at"] = dict_class["updated_at"].isoformat()
        return dict_class

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
