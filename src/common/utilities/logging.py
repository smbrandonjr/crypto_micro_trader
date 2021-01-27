import uuid
from datetime import datetime
from common.database.database import Database

class Logging(object):
    def __init__(self,
                 caller=None,
                 payload=None,
                 _id=None):
        self.datetime = datetime.utcnow()
        self.caller = caller
        self.payload = payload
        self._id = uuid.uuid4().hex if _id is None else _id

    def __call__(self):
        Database.insert("log", self.json())

    def json(self):
        return {
            "datetime": self.datetime,
            "caller": self.caller,
            "payload": self.payload,
            "_id": self._id
        }
