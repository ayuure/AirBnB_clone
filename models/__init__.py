#!/usr/bin/python3

"""contains a global instance of the class FileStrage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
