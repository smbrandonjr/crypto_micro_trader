import uuid
import models.settings.constants as SettingConstants
import common.utilities.serializer as serializer
from common.database.database import Database


class Settings(object):
    def __init__(self,
                 name=None,
                 payload=None,
                 _id=None):
        self.name = name
        self.payload = payload
        self._id = uuid.uuid4().hex if _id is None else _id

    def __call__(self, delete=False):
        if delete:
            Database.remove(SettingConstants.SETTINGS, {"_id": self._id})
        else:
            if Database.find_one(SettingConstants.SETTINGS, {"_id": self._id}):
                print("settings.call - updating setting")
                Database.update(SettingConstants.SETTINGS, {"_id": self._id}, self.json())
            else:
                print("settings.call - inserting setting")
                Database.insert(SettingConstants.SETTINGS, self.json())

    @classmethod
    def read(cls, _id):
        return cls(**Database.find_one(SettingConstants.SETTINGS, {"_id": _id}))

    @classmethod
    def read_by_setting_name_and_portfolio_name(cls, name, portfolio_name):
        return cls(**Database.find_one(SettingConstants.SETTINGS, {"$and"[{"name": name}, "payload.portfolio_name": portfolio_name]}))

    @classmethod
    def read_all(cls):
        if Database.find(SettingConstants.SETTINGS, {}):
            all_settings = []
            settings = Database.find(SettingConstants.SETTINGS, {})
            for setting in settings:
                all_settings.append(cls(**setting))
            return all_settings
        return None


    @staticmethod
    def encode_string(decoded_string):
        return serializer.serialize.dumps(decoded_string)

    @staticmethod
    def decode_string(encoded_string):
        return serializer.serialize.loads(encoded_string)

    def json(self):
        return {
            "name": self.name,
            "payload": self.payload,
            "_id": self._id
        }