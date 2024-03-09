import uuid
import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(
                            self,
                            key,
                            datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"),
                        )
                    else:
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")
            storage.new(self)

    def save(self):
        self.updated_at = datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%S.%f")
        storage.save()

    def to_dict(self):
        dict_class = self.__dict__
        dict_class["__class__"] = self.__class__.__name__
        return dict_class

    def __str__(self):
        return "[{}] {} {}".format(__class__.__name__, self.id, self.__dict__)
