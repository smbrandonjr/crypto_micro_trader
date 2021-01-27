import cbpro
from common.utilities.logging import Logging
import models.accounts.constants as AccountConstants
from models.settings.settings import Settings
import models.settings.constants as SettingConstants

class AccountAuth:

    @staticmethod
    def get_public_client(environment):
        try:
            api_url = AccountConstants.SANDBOX_URL if environment == AccountConstants.SANDBOX else AccountConstants.LIVE_URL if environment == AccountConstants.LIVE else None
            return cbpro.PublicClient(api_url=api_url)
        except BaseException as e:
            print("account_auth.get_public_client++++BaseException: {0}".format(e))
            log_entry = Logging("account_auth.get_public_client++++BaseException: {0}".format(e))
            log_entry()

    @staticmethod
    def get_authenticated_client(environment, portfolio_name):
        try:
            setting_name = SettingConstants.SANDBOX_PORTFOLIO if environment == AccountConstants.SANDBOX else SettingConstants.LIVE_PORTFOLIO if environment == AccountConstants.LIVE else None
            api_url = AccountConstants.SANDBOX_URL if environment == AccountConstants.SANDBOX else AccountConstants.LIVE_URL if environment == AccountConstants.LIVE else None
            portfolio_auth_settings = Settings.read_by_setting_name_and_portfolio_name(setting_name, portfolio_name)
            api_key = portfolio_auth_settings.payload[AccountConstants.API_KEY]
            api_base64 = portfolio_auth_settings.payload[AccountConstants.API_BASE64]
            api_pass = portfolio_auth_settings.payload[AccountConstants.API_PASS]
            return cbpro.AuthenticatedClient(api_key, api_base64, api_pass, api_url=api_url)
        except BaseException as e:
            print("account_auth.get_authenticated_client++++BaseException: {0}".format(e))
            log_entry = Logging("account_auth.get_authenticated_client++++BaseException: {0}".format(e))
            log_entry()

