from flask import Blueprint, url_for, render_template, redirect, request
from models.settings.settings import Settings
from common.utilities.dict_utils import DictUtils

setting_blueprint = Blueprint('settings', __name__)


@setting_blueprint.route('/account_settings/<string:environment>', methods=['GET', 'POST'])
def account_settings(environment):
    # TODO may need to delete any _ids not in the POST request...
    if request.method == "POST":
        portfolio_name, api_key, api_base64, api_pass, base_currency, trade_currency, req_id = None, None, None, None, None, None, None
        all_settings = Settings.read_all()
        setting_name = "sandbox_portfolio" if environment == "sandbox" else "live_portfolio" if environment == "live" else None
        existing_ids = []
        submitted_ids = []
        for setting in all_settings:
            existing_ids.append(setting._id)
        # TODO validate portfolio checking by doing a len() on the portfolio_name
        form_groups = []
        form_portfolio_data = request.form.to_dict(flat=True)
        if form_portfolio_data:
            for key in form_portfolio_data:
                portfolio_data_entry = {}
                group_number = DictUtils.get_form_repeater_group_number(key)
                key_name = DictUtils.get_form_repeater_key(key)
                portfolio_data_entry['group'] = group_number
                portfolio_data_entry[key_name] = form_portfolio_data[key]
                form_groups.append(portfolio_data_entry)
            number_of_portfolios_submitted = DictUtils.get_max_value_from_list_of_dicts_by_key(form_groups, "group")
            for i in range(0, number_of_portfolios_submitted+1):
                req = Settings()
                req.name = "sandbox_portfolio" if environment == "sandbox" else "live_portfolio" if environment == "live" else None
                group_data_dict_list = DictUtils.get_dicts_from_list_by_key_and_order(form_groups, "group", i)
                for group_data_dict in group_data_dict_list:
                    if DictUtils.safe_get_value(group_data_dict, "portfolio_name"):
                        portfolio_name = group_data_dict['portfolio_name']
                    if DictUtils.safe_get_value(group_data_dict, "api_key"):
                        api_key = group_data_dict['api_key']
                    if DictUtils.safe_get_value(group_data_dict, "api_base64"):
                        api_base64 = group_data_dict['api_base64']
                    if DictUtils.safe_get_value(group_data_dict, "api_pass"):
                        api_pass = group_data_dict['api_pass']
                    if DictUtils.safe_get_value(group_data_dict, "base_currency"):
                        base_currency = group_data_dict['base_currency']
                    if DictUtils.safe_get_value(group_data_dict, "trade_currency"):
                        trade_currency = group_data_dict['trade_currency']
                    if DictUtils.safe_get_value(group_data_dict, "_id"):
                        req._id = group_data_dict['_id']
                        submitted_ids.append(req._id)
                req.payload = {"portfolio_name": portfolio_name,
                               "api_key": Settings.encode_string(api_key),
                               "api_base64": Settings.encode_string(api_base64),
                               "api_pass": Settings.encode_string(api_pass),
                               "base_currency": base_currency,
                               "trade_currency": trade_currency}
                if portfolio_name:
                    req()
        for id in existing_ids:
            if id not in submitted_ids:
                del_req = Settings.read(id)
                del_req(delete=True)
    encoded_values = ["api_key", "api_base64", "api_pass"]
    portfolios = []
    all_settings = Settings.read_all()
    setting_name = "sandbox_portfolio" if environment == "sandbox" else "live_portfolio" if environment == "live" else None
    for setting in all_settings:
        if setting.name == setting_name:
            portfolios.append(setting.json())
    # handle encoded text in GUI
    for value in portfolios:
        for val in value:
            if val == "payload":
                for v in value[val]:
                    if v in encoded_values:
                        value[val][v] = Settings.decode_string(value[val][v])
    return render_template("settings/account_settings.html", environment=environment, portfolios=portfolios)
