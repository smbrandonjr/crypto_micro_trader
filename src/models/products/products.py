import cbpro

#TODO - get buy and sell walls

class Products(object):
    def __init__(self,
                 id=None,
                 display_name=None,
                 base_currency=None,
                 quote_currency=None,
                 base_increment=None,
                 quote_increment=None,
                 base_min_size=None,
                 base_max_size=None,
                 min_market_funds=None,
                 max_market_funds=None,
                 status=None,
                 status_message=None,
                 cancel_only=None,
                 limit_only=None,
                 post_only=None,
                 trading_disabled=None):
        self.id = id
        self.display_name = display_name
        self.base_currency = base_currency
        self.quote_currency = quote_currency
        self.base_increment = base_increment
        self.quote_increment = quote_increment
        self.base_min_size = base_min_size
        self.base_max_size = base_max_size
        self.min_market_funds = min_market_funds
        self.max_market_funds = max_market_funds
        self.status = status
        self.status_message = status_message
        self.cancel_only = cancel_only
        self.limit_only = limit_only
        self.post_only = post_only
        self.trading_disabled = trading_disabled

    @staticmethod
    def get_product_history_over_window(product, start,end):
        pass


    def json(self):
        return {
            "id": self.id,
            "display_name": self.display_name,
            "base_currency": self.base_currency,
            "quote_currency": self.quote_currency,
            "base_increment": self.base_increment,
            "quote_increment": self.quote_increment,
            "base_min_size": self.base_min_size,
            "base_max_size": self.base_max_size,
            "min_market_funds": self.min_market_funds,
            "max_market_funds": self.max_market_funds,
            "status": self.status,
            "status_message": self.status_message,
            "cancel_only": self.cancel_only,
            "limit_only": self.limit_only,
            "post_only": self.post_only,
            "trading_disabled": self.trading_disabled
        }


