#!/usr/bin/python3
import json
from os import path

class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = "{}.{}".format(self.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'w', encoding='utf-8') as f:
                json.dump(self.__objects, f)
    
    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json.load(f)
        else:
            return