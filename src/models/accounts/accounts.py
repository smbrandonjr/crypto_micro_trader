import uuid
import cbpro


class Accounts(object):
    def __init__(self,
                 id=None,
                 currency=None,
                 balance=None,
                 available=None,
                 hold=None,
                 profile_id=None,
                 trading_enabled=None,
                 _id=None):
        self.id = id
        self.currency = currency
        self.balance = balance
        self.available = available
        self.hold = hold
        self.profile_id = profile_id
        self.trading_enabled = trading_enabled
        self._id = uuid.uuid4().hex if _id is None else _id

    def __call__(self):
        pass

    def json(self):
        return {
            "id": self.id,
            "currency": self.currency,
            "balance": self.balance,
            "available": self.available,
            "hold": self.hold,
            "profile_id": self.profile_id,
            "trading_enabled": self.trading_enabled,
            "_id": self._id
        }