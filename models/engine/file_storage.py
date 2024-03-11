#!/usr/bin/python3
"""Contains the FileStorage class"""

import json
import os.path


class FileStorage:
    """class for FileStorage"""

    def __init__(self):
        """Initialization of FileStorage instances
        Args:
                - __file_path: json file
                - __objects: dictionary representation an instance
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns all dictionary representations"""
        return self.__objects

    def new(self, obj):
        """create a new key/value pair object"""
        key = "{}.{}".format(type.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialize and store the json representation of an instance"""
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            for key, value in self.__objects.items():
                json.dump({key: value.to_dict()}, file)

    def reload(self):
        """deserialize and loads objects from the json file"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    cls_name, obj_id = key.split(".")
                    cls_ = globals()[cls_name]
                    obj = cls_(**value)
                    self.__objects[key] = obj
