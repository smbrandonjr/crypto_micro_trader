import uuid
from common.database.database import Database
from common.utilities.dict_utils import DictUtils
import models.orders.constants as OrderConstants
from models.orders.sell import Sell
import cbpro

# TODO - if a buy order gets partially filled and then price hits target sell price, cancel buy and sell holdings...


class Order(object):
    def __init__(self,
                 id=None,
                 price=None,
                 size=None,
                 product_id=None,
                 side=None,
                 stp=None,
                 type=None,
                 time_in_force=None,
                 post_only=None,
                 created_at=None,
                 done_at=None,
                 done_reason=None,
                 fill_fees=None,
                 filled_size=None,
                 executed_value=None,
                 status=None,
                 settled=None,
                 _calculated_fee=None,
                 _calculated_base_cost=None,
                 _calculated_total_cost=None,
                 _id=None):
        self.id = id
        self.price = price
        self.size = size
        self.product_id = product_id
        self.side = side
        self.stp = stp
        self.type = type
        self.time_in_force = time_in_force
        self.post_only = post_only
        self.created_at = created_at
        self.done_at = done_at
        self.done_reason = done_reason
        self.fill_fees = fill_fees
        self.filled_size = filled_size
        self.executed_value = executed_value
        self.status = status
        self.settled = settled
        self._calculated_fee = Order.calculate_trade_fee()
        self._calculated_base_cost = Order.get_base_cost()
        self._calculated_total_cost = _calculated_base_cost + _calculated_fee
        self._id = uuid.uuid4().hex if _id is None else _id

    def __call__(self, delete=False, target_sell_price=None):
        if delete:
            Database.remove(OrderConstants.ORDERS, {"_id": self._id})
            if Sell.get_by_buy_id(self.id):
                Database.remove(OrderConstants.SELL, {OrderConstants.BUY_ORDER_ID: self.id})
            elif Sell.get_by_sell_id(self.id):
                clear_sell = Sell.get_by_sell_id(self.id)
                clear_sell.sell_order_id = None
                clear_sell()
        else:
            if Database.find_one(OrderConstants.ORDERS, {"_id": self._id}):
                print("orders.call - updating order")
                Database.update(OrderConstants.ORDERS, {"_id": self._id}, self.json())
                if self.side == OrderConstants.BUY:
                    if self.size > 0 and self.size == self.filled_size:
                        # create a new Order() that is a sell order
                        sell = Sell.get_by_buy_id(self.id)
                        new_order = Order(price=sell.target_sell_price,
                                          size=self.size,
                                          product_id=self.product_id,
                                          side=OrderConstants.SELL,
                                          type=OrderConstants.LIMIT)
                        new_order()
            else:
                print("orders.cal- inserting order")
                Database.insert(OrderConstants.ORDERS, self.json())
                if self.side == OrderConstants.BUY:
                    # create a new Sell()
                    new_sell = Sell()
                    new_sell.buy_order_id = self.id
                    new_sell.target_sell_price = target_sell_price

    @classmethod
    def read_by_order_id(cls, order_id):
        return cls(**Database.find_one(OrderConstants.ORDERS, {"id": id}))

    @staticmethod
    def get_order_size(base_cost, price):
        return base_cost/price if price != 0 else None

    @staticmethod
    def get_base_cost(price, size):
        return size * price

    @staticmethod
    def calculate_trade_fee(base_cost, fee_percentage):
        return base_cost * fee_percentage

    @staticmethod
    def get_order_update_external(order_id, authenticated_client: cbpro.AuthenticatedClient):
        order_data_external = authenticated_client.get_order(order_id)
        order_data_internal = Order.read_by_order_id(order_id)
        order_data_internal.type = DictUtils.safe_get_value(order_data_external, "type")
        order_data_internal.done_at = DictUtils.safe_get_value(order_data_external, "done_at")
        order_data_internal.done_reason = DictUtils.safe_get_value(order_data_external, "done_reason")
        order_data_internal.fill_fees = DictUtils.safe_get_value(order_data_external, "fill_fees")
        order_data_internal.filled_size = DictUtils.safe_get_value(order_data_external, "filled_size")
        order_data_internal.executed_value = DictUtils.safe_get_value(order_data_external, "executed_value")
        order_data_internal.status = DictUtils.safe_get_value(order_data_external, "status")
        order_data_internal.settled = DictUtils.safe_get_value(order_data_external, "settled")
        order_data_internal()
        return True

    def json(self):
        return {
            "id": self.id,
            "price": self.price,
            "size": self.size,
            "product_id": self.product_id,
            "side": self.side,
            "stp": self.stp,
            "type": self.type,
            "time_in_force": self.time_in_force,
            "post_only": self.post_only,
            "created_at": self.created_at,
            "done_at": self.done_at,
            "done_reason": self.done_reason,
            "fill_fees": self.fill_fees,
            "filled_size": self.filled_size,
            "executed_value": self.executed_value,
            "status": self.status,
            "settled": self.settled,
            "_calculated_fee": self._calculated_fee,
            "_calculated_base_cost": self._calculated_base_cost,
            "_calculated_total_cost": self._calculated_total_cost,
            "_id": self._id
        }