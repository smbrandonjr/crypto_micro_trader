

class NumberUtils:

    @staticmethod
    def cast_as_shortened_float(number, significant_digit_string):
        # "{0:.6f}".format(number)
        # significant_digit can be a string like the "base_increment", "quote_increment", etc...
        significant_digits = significant_digit_string.replace("0.", "").index("1") + 1
        formatter_string = "{{0:.{0}f}}".format(significant_digits)
        if type(number) == str:
            number = float(number)
            number_string = formatter_string.format(number)
            return (float(number_string))
        elif type(number) == float:
            number_string = formatter_string.format(number)
            return (float(number_string))
        else:
            number = float(number)
            number_string = formatter_string.format(number)
            return float(number_string)