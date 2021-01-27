import uuid
from common.database.database import Database
import models.orders.constants as SellConstants

class Sell(object):
    def __init__(self,
                 buy_order_id=None,
                 sell_order_id=None,
                 target_sell_price=None,
                 _id=None):
        self.buy_order_id = buy_order_id
        self.sell_order_id = sell_order_id
        self.target_sell_price = target_sell_price
        self._id = uuid.uuid4().hex if _id is None else _id

    def __call__(self, delete=False):
        if delete:
            Database.remove(SellConstants.SELL, {"_id": self._id})
        else:
            if Database.find_one(SellConstants.SELL, {"_id": self._id}):
                print("sell.call - updating sell")
                Database.update(SellConstants.SELL, {"_id": self._id}, self.json())
            else:
                print("sell.cal- inserting sell")
                Database.insert(SellConstants.SELL, self.json())

    # TODO - a buy order should trigger this object to get created
    # TODO - 1. create Sell() w/ buy_order_id and target_sell_price (size is on order)
    # TODO - 2. if buy order gets filled, create a sell order at the target_sell_price and populate the sell_order_id
    # TODO - 3. if buy order gets cancelled then delete this Sell()
    # TODO - 4. if sell order get cancelled then clear the sell_order_id

    @classmethod
    def get_by_buy_id(cls, buy_order_id):
        return cls(**Database.find_one(SellConstants.SELL, {SellConstants.BUY_ORDER_ID: buy_order_id}))

    @classmethod
    def get_by_sell_id(cls, sell_order_id):
        return cls(**Database.find_one(SellConstants.SELL, {SellConstants.SELL_ORDER_ID: sell_order_id}))

    def json(self):
        return {
            "buy_order_id": self.buy_order_id,
            "sell_order_id": self.sell_order_id,
            "target_sell_price": self.target_sell_price,
            "_id": self._id
        }