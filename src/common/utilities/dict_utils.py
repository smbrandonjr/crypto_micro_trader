from functools import reduce

class DictUtils:

    @staticmethod
    def safe_get_value(dictionary, keys, default=None):
        return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)

    @staticmethod
    def get_form_repeater_group_number(key):
        start = key.index("[") + 1
        end = key.index("]")
        # print("get_form_repeater_group_number: ", key[start:end])
        return int(key[start:end])

    @staticmethod
    def get_form_repeater_key(key):
        start = key.index("]") + 2
        end = key.rfind("]")
        # print("get_form_repeater_key: ", key[start:end])
        return key[start:end]

    @staticmethod
    def get_max_value_from_list_of_dicts_by_key(dict_list, key):
        values = [x[key] for x in dict_list]
        # print("get_max_value_from_list_of_dicts_by_key: ", max(values))
        return max(values)

    @staticmethod
    def get_dicts_from_list_by_key_and_order(dict_list, key, order):
        # print("get_dicts_from_list_by_key_and_order: ", [x for x in dict_list if x[key] == order])
        return [x for x in dict_list if x[key] == order]