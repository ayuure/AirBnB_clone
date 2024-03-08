import json
import os.path


class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = '{}.{}'.format(__class__.__name__, obj.id)
        self.__objects[key] =obj
        # self.__objects = obj
        # setattr(self, obj, self.id)

    def save(self, ):
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            for key, value in self.__objects.items():
                json.dump({key: value.to_dict()}, file)

    def reload(self):
        path = 'AirBnB_clone/file.json'
        if os.path.isfile(path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                data = json.load(file)
                for key,value in data.items():
                    cls_name, obj_id = key.split('.')
                    cls_ = eval(cls_name)
                    obj = cls_(**value)
                    self.__objects[key] = obj