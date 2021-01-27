import cbpro
from models.accounts.account_auth import AccountAuth


class Fees:

    @staticmethod
    def get_fees(authenticated_client: cbpro.AuthenticatedClient):
        '''
        Get the current maker and taker fees for authenticate account.
        :param authenticated_client: cbpro.AuthenticatedClient
        :return: {"maker_fee_rate": "0.0015", "taker_fee_rate": "0.0025", "usd_volume": "25000.00"}
        '''
        return authenticated_client.get_fees()